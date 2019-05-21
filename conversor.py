import requests
from bs4 import BeautifulSoup

r = requests.get('https://economia.uol.com.br/cotacoes/')
sabao = BeautifulSoup(r.text , 'html.parser')

def conversordolar(x,y):
	resultado = x/y
	print(" ")
	print(str(round(resultado, 2)) + " Dólares")

def conversoreuro(x,y):
	resultado = x/y
	print(str(round(resultado, 2)) + " Euros")

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



print("Conversor monetário desenvolvido por InimigoMortal")
print("Os valores são tirados em tempo real do https://economia.uol.com.br/cotacoes ")
print("Dólar: " + str(cotacaodolar) + " Euro: " + str(cotacaoeuro) + data)


real = input("valor em Real: ")
while real != "sair":
	conversordolar(float(real),cotacaodolar)
	conversoreuro(float(real),cotacaoeuro)
	real = input("valor em Real: ")
	