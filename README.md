This is the repository to generate rrs feeds for the sites that it does not have rss.
According to the advise from Claude, we should not generate the feeds that has their own rss
because the website already optimized it better than our scrapping method. Below are the files to understand

Questions:
1/ What are required filed in rss feed to make it work and import to feedly or any rss reader?


- generate_feeds.py: runner, loops over every site
- feed_builder.py : shared RSS writer, should not be touched
sites/
    __init__.py: empty, just make it as a package
    alignment_anthropic.py : for anthropic alignment blog

.github/workflows/update-feed.yml: to auto work for github, update every 8 hours