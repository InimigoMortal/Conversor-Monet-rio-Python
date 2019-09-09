import requests
from bs4 import BeautifulSoup

req = requests.get('https://br.financas.yahoo.com/trending-tickers')
sab = BeautifulSoup(req.text , 'html.parser')

re = requests.get('https://br.financas.yahoo.com/')
s = BeautifulSoup(re.text , 'html.parser')

dado = requests.get('https://www.google.com/search?client=firefox-b-d&ei=y97vXP6UO-rA5OUPyc6QyAs&q=converter+bitcoin+em+real&oq=converter+bitcoin+em+real&gs_l=psy-ab.3..0i324j0j0i22i30l6.1375569.1379057..1379248...0.0..0.144.2000.0j15......0....1..gws-wiz.......0i71j0i131j35i39.R-bUcd8uriE')
le = BeautifulSoup(dado.text , 'html.parser')



 


def jogadolar():
    ens = sab.find_all('td')[2]
    valordol = float(ens.text.replace(",","."))
    return valordol
def jogaeuro():
    esb = s.find_all("span")[29]
    valoreuro = float(esb.text.replace(",","."))
    return valoreuro
def jogabit():
    leia = le.find_all('span')[26]
    valorbit = float(leia.text.replace("R$","").replace(",00","").replace(".",""))
    return valorbit

