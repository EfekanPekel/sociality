from bs4 import BeautifulSoup
import urllib3
import re

link = input("Giriş değeri: ")
http = urllib3.PoolManager()
response = http.request('GET', link)
soup = BeautifulSoup(response.data, 'html.parser')

PriceBeforePoint = soup.find(attrs={"data-bind":"markupText:'currentPriceBeforePoint'"}).text
PriceAfterPoint = soup.find(attrs={"data-bind":"markupText:'currentPriceAfterPoint'"}).text
PriceCurrency = soup.find(attrs={"itemprop":"priceCurrency"}).text

print("Sonuç: " + PriceBeforePoint+ "," + PriceAfterPoint + " " + PriceCurrency)
