from scrapy.crawler import CrawlerProcess
import argparse
import scrapy
import json


class MySpider(scrapy.Spider):
    pass

def crawl(root_url):
	process = CrawlerProcess(settings={
    	"FEEDS": {
        	"items.json": {"format": "json"},
    	},
	})
	process.crawl(MySpider)
	process.start() # the script will block here until the crawling is finished

def main():
	parser = argparse.ArgumentParser(description="Crawl URL for in-scope links.")
	parser.add_argument("root_url", metavar="root_url", type=str, nargs=1)
	parser.add_argument("-o", "--output")
	args = parser.parse_args()
	results = crawl(args.root_url[0])
	if args.output is not None:
		with open(args.output, 'w') as f:
			f.write(json.dumps(results, indent=4))
	else:
		print(results)

if __name__ == "__main__":
	main()
