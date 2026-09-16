"""
generate_feeds.py
 
Loops over every site adapter in SITES, builds a feed for each, and writes
one .xml file per site. Add a new site by writing an adapter module in
sites/ (see sites/alignment_anthropic.py for a working example, and
sites/pi_website.py for one you're filling in) and adding it to the list
below.
 
A failure in one site's scraper does NOT stop the others -- it's logged,
that site's feed is simply left unchanged, and the run exits non-zero at
the end so GitHub Actions flags it (and, if you haven't turned off Actions
email notifications, you'll get an email).
"""

import sys
from feed_builder import build_feed
from sites import pi_website, alignment_anthropic

SITES = [
    alignment_anthropic,
    #pi_website,
    # add more site adapters here as you write them
]


def main():
    failures = []

    for site in SITES:
        try:
            articles = site.fetch_articles()
            if not articles:
                raise RuntimeError("no articles found")
            build_feed(
                source_url=site.SOURCE_URL,
                feed_title=site.FEED_TITLE,
                description=f"Unofficial auto-generated feed for {site.FEED_TITLE}",
                articles=articles,
                output_file=site.OUTPUT_FILE
            )
            print(f"{site.OUTPUT_FILE}: wrote {len(articles)} articles")
        except Exception as exc:
            failures.append((site.__name__, exc))
            print(f"FAILED {site.__name__} : {exc}", file=sys.stderr)

    if failures:
        sys.exit(1)

if __name__ == "__main__":
    main()