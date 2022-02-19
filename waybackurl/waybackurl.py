import requests
import argparse
import json


def waybackurl(domain):
	waybackurl_string = "http://web.archive.org/cdx/search/cdx?url=*.%s/*&output=json&fl=original&collapse=urlkey"
	resp = requests.get(waybackurl_string % domain)
	if resp.status_code == 200:
		obj = [url[0] for url in json.loads(resp.text)[1:]]
		return obj
	else:
		return "Error getting waybackurls for %s" % domain

def main():
	parser = argparse.ArgumentParser(description="Get wayback urls for a given domain.")
	parser.add_argument("domain", metavar="domain", type=str, nargs=1)
	parser.add_argument("-o", "--output")
	args = parser.parse_args()
	results = waybackurl(args.domain[0])
	if args.output is not None:
		with open(args.output, 'w') as f:
			f.write(json.dumps(results, indent=4))
	else:
		print(results)

if __name__ == "__main__":
	main()
