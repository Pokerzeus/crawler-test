import requests
from bs4 import BeautifulSoup


def get_data_from_url(max_pages):
	page = 1
	while page <= max_pages:
		url = "https://www.thesius.de/offeringssearch?page=" + str(page) + "&q=&field=wirtschaftswissenschaften"
		r = requests.get(url)
		soup = BeautifulSoup(r.content)
		g_data = soup.find_all("div", {"class": "row offering-item spacing-bottom-zero"})

		for item in g_data:
			print item.contents[1].find_all("div", {"class": "offering-title word-break"})[0].text
		page += 1

print get_data_from_url(10)