# Toddler Shelf MVP

The first slice is a versioned US yogurt catalog and offline decision logic for ages 12–23 months. Run `python3 rank.py < example.json` with Python 3. No credentials or network calls are needed.

The sample contains synthetic detector output and illustrative boxes. A future single vision call should return brand, style, flavor, milk fat, pack size, and an optional normalized [left, top, right, bottom] position for each package. An unreadable field can be null. The UI can draw boxes on the original image and show the returned status and source. Exact field matching is deliberately conservative. Catalog coverage, barcode identity, packaging versions, camera UI, and the vision integration are pending.

The catalog separates the Walmart discovery list from manufacturer label facts. Retailer discovery does not establish local store stock. A null advisory field means unknown. Online label facts do not establish the current package or rule out cross-contact. With a saved allergy, the prototype flags known ingredients and returns a package-check status for other matched products. Use only synthetic profiles in fixtures.

Rules based on [CDC dairy guidance](https://www.cdc.gov/infant-toddler-nutrition/foods-and-drinks/cows-milk-and-milk-alternatives.html), [CDC foods to limit](https://www.cdc.gov/infant-toddler-nutrition/foods-and-drinks/foods-and-drinks-to-avoid-or-limit.html), and [FDA food allergies](https://www.fda.gov/food/nutrition-food-labeling-and-critical-foods/food-allergies).
