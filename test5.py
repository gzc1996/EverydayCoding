import requests
import bs4
res = requests.get("https://movie.douban.com/chart")
soup = bs4.BeautifulSoup(res.text,"html.parser")
targets = soup.find_all("div",class_="pl2")
for each in targets:
	print(each.a.text)