import feedparser

FEEDS = [
    "https://hnrss.org/frontpage"
]


def fetch_signals(cfg):
    results = []

    for url in FEEDS:
        feed = feedparser.parse(url)
        for entry in feed.entries[:cfg['max_items']]:
            results.append({
                "title": entry.title,
                "summary": entry.get("summary", ""),
                "keyword": entry.title.lower()[:50],
                "source": url
            })

    return results