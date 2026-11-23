"""Offline label lookup for a 12–23 month yogurt shelf scan."""
import json
import sys
from pathlib import Path

MATCH_FIELDS = ("brand", "style", "flavor", "milk_fat", "size_oz")
CATALOG = json.loads(Path(__file__).with_name("catalog.json").read_text())


def evaluate(candidate, allergens):
    matches = [
        row for row in CATALOG["products"]
        if all(candidate.get(field) == row[field] for field in MATCH_FIELDS)
    ]
    if len(matches) != 1:
        return {"status": "verify_product"}
    row = matches[0]
    result = {"id": row["id"], "source": row["source"]}
    if allergens.intersection(row["known_allergens"] + (row["may_contain"] or [])):
        return {**result, "status": "avoid_known_allergen"}
    if allergens:
        return {**result, "status": "verify_current_package_for_allergens"}
    if row["added_sugar_g"] is None:
        return {**result, "status": "verify_added_sugar"}
    if row["added_sugar_g"] > 0:
        return {**result, "status": "added_sugar", "added_sugar_g": row["added_sugar_g"]}
    if row["flavor"] == "plain" and row["milk_fat"] == "whole":
        return {**result, "status": "daily_candidate", "added_sugar_g": 0}
    return {**result, "status": "other_yogurt"}


def analyze(scan):
    if type(scan["age_months"]) is not int or not 12 <= scan["age_months"] <= 23:
        return {"status": "age_outside_mvp", "results": [], "picks": []}
    allergens = {name.strip().lower() for name in scan["allergens"] if name.strip()}
    results = [
        {**evaluate(candidate, allergens), "box": candidate.get("box")}
        for candidate in scan["candidates"]
    ]
    return {
        "status": "complete",
        "results": results,
        "picks": [item for item in results if item["status"] == "daily_candidate"],
    }


if __name__ == "__main__":
    print(json.dumps(analyze(json.load(sys.stdin)), indent=2))
