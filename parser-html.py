from bottle import get, post, request, route, Bottle, run, redirect
from bs4 import BeautifulSoup
import urllib3
import re


@get('/link')
def link():
	return '''
		<form action="/link" method="post">
			Giriş değeri: <input name="link" type="text" />
			<input value="Gönder" type="submit">
		<form/>
	'''

	
@post('/link')
def fiyat():
	link = request.forms.get('link')
	http = urllib3.PoolManager()
	response = http.request('GET', link)
	soup = BeautifulSoup(response.data, 'html.parser')
	PriceBeforePoint = soup.find(attrs={"data-bind":"markupText:'currentPriceBeforePoint'"}).text
	PriceAfterPoint = soup.find(attrs={"data-bind":"markupText:'currentPriceAfterPoint'"}).text
	PriceCurrency = soup.find(attrs={"itemprop":"priceCurrency"}).text
	output = PriceBeforePoint + "," + PriceAfterPoint + " " + PriceCurrency
	return '''<h3>Sonuç: %s </h3></br>
			<input type="button" value="Giris" onclick="window.location.href='/link'" />
			'''  %  output
	redirect('/link')
	
			
run()
