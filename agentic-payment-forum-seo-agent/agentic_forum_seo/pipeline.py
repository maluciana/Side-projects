import json
from datetime import datetime
from collections import defaultdict
from .sources import fetch_signals
from .config import get_config


def score_signal(s, keywords):
    score = 0
    for k in keywords:
        if k in s['title'].lower():
            score += 2
    score += len(s['summary']) / 500
    return score


def cluster_topics(signals):
    clusters = defaultdict(list)
    for s in signals:
        key = s['keyword'].split(' ')[0]
        clusters[key].append(s)
    return clusters


def build_seo_pages(clusters):
    pages = []
    for k, items in clusters.items():
        pages.append({
            "pillar_keyword": k,
            "slug": k.replace(' ', '-'),
            "title": f"{k.title()} in Agentic Payments: Guide",
            "supporting_topics": [i['title'] for i in items[:5]]
        })
    return pages


def build_internal_links(pages):
    links = []
    for p in pages:
        for other in pages:
            if p != other:
                links.append({
                    "from": p['slug'],
                    "to": other['slug'],
                    "anchor": other['pillar_keyword']
                })
    return links


def run_pipeline():
    cfg = get_config()
    keywords = cfg.get("target_keywords", [])

    signals = fetch_signals(cfg)

    ranked = sorted(signals, key=lambda s: score_signal(s, keywords), reverse=True)

    clusters = cluster_topics(ranked[:20])

    pages = build_seo_pages(clusters)

    links = build_internal_links(pages)

    outputs = {
        "generated_at": datetime.utcnow().isoformat(),
        "top_signals": ranked[:20],
        "pages": pages,
        "internal_links": links
    }

    with open("outputs.json", "w") as f:
        json.dump(outputs, f, indent=2)

    print("Autonomous SEO pipeline complete.")