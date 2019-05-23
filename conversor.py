import requests
from bs4 import BeautifulSoup

r = requests.get('https://economia.uol.com.br/cotacoes/')
sabao = BeautifulSoup(r.text , 'html.parser')






'''Dólar'''
ensaboado = sabao.find_all(class_="subtituloGrafico subtituloGraficoValor")[0]
remove = (ensaboado.text).replace("R$", "")
cotacaodolar = float(remove.replace(",", "."))
'''Euro'''
ensaboado2 = sabao.find_all(class_="subtituloGrafico subtituloGraficoValor")[2]
rem = (ensaboado2.text).replace("R$", "")
cotacaoeuro = float(rem.replace(",", "."))
'''Data de atualização'''
ensaboado3 = sabao.find(class_="section-info")
data = (ensaboado3.text).replace("Câmbio","").replace("    ", " ")
'''Bitcoin'''
ensaboado4 = sabao.find_all(class_="linhaDados")[3]
r = (ensaboado4.text).replace("Bitcoin","").replace("%US$","")
l = r.split()
cotacaobitcoin = cotacaodolar*float(str(l.pop(1)).replace(".","").replace(",","."))
cotacaobitcoindol = cotacaodolar/cotacaobitcoin
cotacaobitcoineur = cotacaoeuro/cotacaobitcoin
'''Notícia'''
ensaboado5 = sabao.find_all('h1')[0]
noticia = ensaboado5.text
	


def conversor(x,carac1):
	if carac1 == "real dollar":
		valor_real = cotacaoeuro*float(x)
		valor_dollar = (cotacaoeuro/cotacaodolar)*float(x)
		valor_bitcoin = cotacaobitcoineur*float(x)
		print("")
		print(str(round(valor_real , 2)) + " Reais")
		print(str(round(valor_dollar , 2)) + " Dólares")
		print(str(round(valor_bitcoin , 5)) + " Bitcoins")
	if carac1 == "real euro":
		valor_real = cotacaodolar*float(x)
		valor_euro = (cotacaodolar/cotacaoeuro)*float(x)
		valor_bitcoin = cotacaobitcoindol*float(x)
		
		print("")
		print(str(round(valor_real , 2)) + " Reais")
		print(str(round(valor_euro , 2)) + " Euros")
		print(str(round(valor_bitcoin , 5)) + " Bitcoins")
	if carac1 == "euro dollar":
		valor_euro = (1/cotacaoeuro)*float(x)
		valor_dollar = (1/cotacaodolar)*float(x)
		valor_bitcoin = (1/cotacaobitcoin)*float(x)
		print("")
		print(str(round(valor_euro , 2)) + " Euros")
		print(str(round(valor_dollar , 2)) + " Dólares")
		print(str(round(valor_bitcoin , 5)) + " Bitcoins")
	if carac1 == "real euro dollar":
		valor_real = cotacaobitcoin*float(x)
		valor_dollar = (cotacaobitcoin/cotacaodolar)*float(x)
		valor_euro = (cotacaobitcoin/cotacaoeuro)*float(x)
		print("")
		print(str(round(valor_real , 2)) + " Reais")
		print(str(round(valor_euro , 2)) + " Euros")
		print(str(round(valor_dollar , 2)) + " Dólares")






print("Conversor monetário desenvolvido por InimigoMortal")
print("Os valores são tirados em tempo real do https://economia.uol.com.br/cotacoes ")
print("Dólar: " + str(cotacaodolar) + " Euro: " + str(cotacaoeuro) + " Bitcoin: " + str(round(cotacaobitcoin, 2)) + data)
print("Notícia: " + noticia)
print("")

res = input("Qual moeda? (euro/dólar/real/bitcoin) ")
while res != "sair":
	if res == "converte euro" or res == "euro":
		res = input("valor em Euro: ")
		conversor(res,"real dollar")
	if res == "converte dólar" or res == "dólar" or res == "dollar" :
		res = input("valor em Dólar: ")
		conversor(res,"real euro")
	if res == "converte real" or res == "real":
		res = input("valor em Real: ")
		conversor(res,"euro dollar")
	if res == "converte bitcoin" or res == "bitcoin":
		res = input("valor em Bitcoin: ")
		conversor(res,"real euro dollar")
	print("")
	res = input("Qual moeda? (euro/dólar/real/bitcoin) ")

	

	
