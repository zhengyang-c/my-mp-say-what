from bs4 import BeautifulSoup

with open("devel/home_page_dump.html", "r") as f:
	soup = BeautifulSoup(f)

print(soup)