import os


def get_config():
    return {
        "site_name": os.getenv("SITE_NAME", "Agentic Payment Forum"),
        "site_url": os.getenv("SITE_URL", ""),
        "max_items": int(os.getenv("MAX_ITEMS", 10))
    }