import requests
import bs4
import json

base_url = "https://portswigger.net"

resp = requests.get(base_url+"/kb/issues")
soup = bs4.BeautifulSoup(resp.content, features="html.parser")
tbody = soup.find_all("tbody")
table = tbody[1]
issue_urls = [base_url+row.find_all("td")[0].find('a')["href"] for row in table.find_all("tr")]

entries = {}
for issue_url in issue_urls:
	print(issue_url)
	new_entry = {}
	resp = requests.get(issue_url)
	soup = bs4.BeautifulSoup(resp.content, features="html.parser")
	title_mark = soup.find("h1")
	title = title_mark.text.strip()
	marks = title_mark.find_all_next(name="h2")
	p_results = []
	for mark in marks:
		p_mark = mark.find_next()
		p_list = []
		while p_mark.name == 'p':
			p_list.append(p_mark.text.strip())
			p_mark = p_mark.find_next()
		p_results.append('\n\n'.join(p_list))
	if len(marks) == 3:
		entries[title.lower()] = {"title": title, "impact": p_results[0], "desc": p_results[1], "mitigation": p_results[2]}
	elif len(marks) == 2: 
		entries[title.lower()] = {"title": title, "impact": "", "desc": p_results[0], "mitigation": p_results[1]}
	else:
		entries[title.lower()] = {"title": title, "impact": "", "desc": p_results[0], "mitigation": ""}

with open("portswigger_results.json", 'w') as f:
	f.write(json.dumps(entries, indent=4))

