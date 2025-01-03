import requests
from bs4 import BeautifulSoup
import re

#base_url = "https://books.toscrape.com/"
base_url = "https://books.toscrape.com/catalogue/category/books_1/page-1.html"

home_page = requests.get(base_url)


if home_page.status_code == 200:
  print("Success")
else:
  print(f"Failed, status code: {home_page.status_code}")

soup = BeautifulSoup(home_page.content,"html.parser")

firstbook = soup.find_all(name = "li", class_= "col-xs-6 col-sm-4 col-md-3 col-lg-3")
result=[]
for i in range(len(firstbook)):
  sub=[]
  pricetag=firstbook[i].find(name= "p", class_="price_color").get_text().strip()
  title=firstbook[i].find(name= "h3").find('a')['title'].strip()
  price = float(re.sub(r'[^\d.]', '', pricetag))
  status=firstbook[i].find(name= "p", class_="instock availability").get_text().strip()
  sub.append(title)
  sub.append(pricetag)
  sub.append(status)
  result.append(sub)

print(result)
