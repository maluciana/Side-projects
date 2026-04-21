import json
from datetime import datetime
from .sources import fetch_signals
from .config import get_config


def run_pipeline():
    cfg = get_config()

    signals = fetch_signals(cfg)

    seo_briefs = []
    for s in signals:
        seo_briefs.append({
            "title": f"What is {s['keyword']}?",
            "slug": s['keyword'].replace(' ', '-'),
            "why_now": s['summary'],
            "source": s['source']
        })

    outputs = {
        "generated_at": datetime.utcnow().isoformat(),
        "signals": signals,
        "seo_briefs": seo_briefs
    }

    with open("outputs.json", "w") as f:
        json.dump(outputs, f, indent=2)

    print("Pipeline complete.")