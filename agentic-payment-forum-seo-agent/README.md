# Agentic Payment Forum SEO Agent

A daily-running Python pipeline that helps grow **Agentic Payment Forum** by:

1. discovering fresh agentic payment topics
2. clustering them into SEO opportunities
3. generating structured article briefs
4. producing homepage / post metadata
5. emitting internal linking suggestions
6. saving outputs as versioned artifacts in the repo

## What this project does today

- Pulls signals from configurable RSS feeds
- Scores items using keyword and recency heuristics
- Generates:
  - `outputs/signals.json`
  - `outputs/seo_briefs.json`
  - `outputs/internal_links.json`
  - `outputs/homepage_blocks.json`
- Runs automatically every day via GitHub Actions
- Can also be triggered manually

## Repo structure

```text
agentic-payment-forum-seo-agent/
  agentic_forum_seo/
    __init__.py
    config.py
    pipeline.py
    sources.py
  main.py
  requirements.txt
  .env.example
.github/workflows/
  agentic-payment-forum-seo-daily.yml
```

## Environment variables

Create repository secrets for:

- `SITE_NAME` — default `Agentic Payment Forum`
- `SITE_URL` — your canonical site URL
- `TARGET_KEYWORDS` — comma-separated keywords to prioritize
- `MAX_ITEMS` — optional, default `25`

Optional:
- `OPENAI_API_KEY` — reserved for later LLM enrichment
- `X_BEARER_TOKEN` — reserved for later social signal ingest

## Local run

```bash
cd agentic-payment-forum-seo-agent
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
python main.py
```

## GitHub Actions

The workflow runs daily and on manual dispatch.

Default cron:

```cron
17 15 * * *
```

That is **8:17 AM Los Angeles time during PST** and **8:17 AM or 7:17 AM depending on daylight shifts**, because GitHub Actions cron uses UTC.

## Next upgrades

- add sitemap crawler for your own site
- generate slug/title/meta description suggestions per topic
- integrate OpenAI for article outlines and FAQ blocks
- auto-open PRs with new content drafts
- auto-submit sitemap ping after publish

## Important truth

This is the operational backend for SEO intelligence. It does **not** directly publish into Hashnode or your CMS yet because that requires the exact publishing API or repo integration path. But the daily signal + brief engine is now set up so your content machine has a real foundation.
