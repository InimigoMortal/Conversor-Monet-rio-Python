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

ensaboado3 = sabao.find(class_="section-info")
data = (ensaboado3.text).replace("Câmbio","")

def conversor(x,carac1):
	if carac1 == "real dollar":
		valor_real = cotacaoeuro*float(x)
		valor_dollar = (cotacaoeuro/cotacaodolar)*float(x)
		print("")
		print(str(round(valor_real , 2)) + " Reais")
		print(str(round(valor_dollar , 2)) + " Dólares")
	if carac1 == "real euro":
		valor_real = cotacaodolar*float(x)
		valor_euro = (cotacaodolar/cotacaoeuro)*float(x)
		print("")
		print(str(round(valor_real , 2)) + " Reais")
		print(str(round(valor_euro , 2)) + " Euros")
	if carac1 == "euro dollar":
		valor_euro = (1/cotacaoeuro)*float(x)
		valor_dollar = (1/cotacaodolar)*float(x)
		print("")
		print(str(round(valor_euro , 2)) + " Euros")
		print(str(round(valor_dollar , 2)) + " Dólares")






print("Conversor monetário desenvolvido por InimigoMortal")
print("Os valores são tirados em tempo real do https://economia.uol.com.br/cotacoes ")
print("Dólar: " + str(cotacaodolar) + " Euro: " + str(cotacaoeuro) + data)
print("")

res = input("Qual moeda? (euro/dólar/real) ")
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
	print("")
	res = input("Qual moeda? (euro/dólar/real) ")
	

	

	