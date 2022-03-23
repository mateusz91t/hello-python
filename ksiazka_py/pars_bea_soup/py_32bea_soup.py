import requests as req
from bs4 import BeautifulSoup


# strona = req.get('https://mateusz-siema.pl.tl/Kontakt.htm')
strona = req.get('http://dareczko26.prv.pl/fotki.html')
strona.encoding = '1250'
zupa = BeautifulSoup(strona.text, 'html.parser')
