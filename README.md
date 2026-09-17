This is the repository to generate rrs feeds for the sites that it does not have rss.
According to the advise from Claude, we should not generate the feeds that has their own rss
because the website already optimized it better than our scrapping method. Below are the files to understand

Questions:
1/ What are required filed in rss feed to make it work and import to feedly or any rss reader?


- generate_feeds.py: runner, loops over every site
- feed_builder.py : shared RSS writer, should not be touched
- sites/
    __init__.py: empty, just make it as a package
    alignment_anthropic.py : for anthropic alignment blog

.github/workflows/update-feed.yml: to auto work for github, update every 8 hours

Step-by-step to generate the feed and autowork on github:
1/ Create a public repository on Github
2/ Push the code to the repository, rememeber there must be .github/workflows/update-feed.yml so Github knows how to run the script automatically
3/ Turn on write permission: Settings -> Actions -> General -> Workflow permissions and select 'Read and write permissions' (Well actually I just select Read option and somehow bot still able to update the .xml files)
4/ Trigger it once to check if everything works: Go to Actions tab and click 'Update Blog Feeds' and press 'Run workflow'. It should have new commit with .xml files
5/ Go to your rss-reader and copy URL: https://raw.githubusercontent.com/YOUR_USERNAME/YOUR_REPO/main/feed.xml 