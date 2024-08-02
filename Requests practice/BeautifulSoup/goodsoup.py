from bs4 import BeautifulSoup
import requests
response = requests.get("https://www.tcs.com/sitemap.xml")
# print(response.text)
tcs = response.text
soup = BeautifulSoup(tcs, features="xml")
print(soup.prettify())
# print(soup)
# print(soup.find("title"))
# print(soup.find("a")) # finds first a tag
# print(soup.find("p")) # finds first p tag
# print(soup.find("body"))
# print(soup.find_all("a")) #finds all a tags
# for lists in soup.find_all("li"):
#     print(lists)