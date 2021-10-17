# Python Web Crawler
This Project does not use external libraries to do the actual crawling. The 'Spiders' are created in-house, and so is the 'work'. 
The number of threads (Spiders) is pre-set in main.py (currently set at 8) but can easily be changed manually.

## How it works
##### Firstly, workers (Spiders) are created
##### Secondly, the first spider creates a singular queue of links is by pulling all the links contained inside the attribute tags from the inputted url. 
##### Finally, the Spiders all check if there are any links to crawl in the queue, and actually crawl them (go inside, extract, note down).
##### The links are separated in two files, which all spiders use simultaneously:
  - queue.txt, where the found, but not yet crawled links are stored as a set
  - and crawled.txt, to which the crawled links and their origins are ammended to
  
## Files and what are for:

- link_finder.py --> creates a class LinkFinder; locates all the links and makes them a set
- domain_finder.py --> extracts domain; used when imported
- general.py --> 'housekeeping' functions, i.e. imported in multiple places and called upon
- spider.py --> defines the class Spider; the entire functionality of an individual crawler-worker
- main.py --> receives input, creates workers, creates jobs, crawls, responsible for live-progress output
### To launch the app, clone the repo and Run 'main'
