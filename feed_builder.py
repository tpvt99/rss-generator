"""
feed_builder.py
 
Site-agnostic. Takes a normalized list of articles and writes an RSS file.
Every site adapter (see sites/) produces articles in this same shape:
 
    {"title": str, "url": str, "date": datetime (timezone-aware, UTC)}
 
so this function never needs to know which site it came from.
"""

from feedgen.feed import FeedGenerator


def build_feed(source_url, feed_title, description, articles, output_file):
    fg = FeedGenerator()
    fg.id(source_url)
    fg.title(feed_title)
    fg.link(href=source_url, rel="alternate")
    fg.description(description)
    fg.language("en")

    for article in articles:
        fe = fg.add_entry(order='append')
        fe.id(article["url"])
        fe.title(article["title"])
        fe.link(href=article["url"])
        fe.description(article["description"])
        fe.pubDate(article["date"])

    fg.rss_file(output_file)