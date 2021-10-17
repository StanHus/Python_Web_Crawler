# Python Web Crawler
### To launch the app, clone the repo and Run 'main'

## Files and what they do:

- link_finder.py --> creates a class LinkFinder; locates all the links and makes them a set
- domain_finder.py --> extracts domain; used when imported
- general.py --> 'housekeeping' functions, i.e. imported in multiple places and called upon
- spider.py --> defines the class Spider; the entire functionality of an individual crawler-worker
- main.py --> receives input, creates workers, creates jobs, crawls, responsible for live-progress output
