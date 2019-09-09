import requests
from bs4 import BeautifulSoup

r = requests.get('https://economia.uol.com.br/cotacoes/')
sabao = BeautifulSoup(r.text , 'html.parser')






'''Dólar'''
try:
	ensaboado = sabao.find_all(class_="subtituloGrafico subtituloGraficoValor")[0]
	remove = (ensaboado.text).replace("R$", "")
	cotacaodolar = float(remove.replace(",", "."))
except Exception:
	from dolareuro import jogadolar
	cotacaodolar = jogadolar()



'''Euro'''
try:
	ensaboado2 = sabao.find_all(class_="subtituloGrafico subtituloGraficoValor")[2]
	rem = (ensaboado2.text).replace("R$", "")
	cotacaoeuro = float(rem.replace(",", "."))
except Exception:
	from dolareuro import jogaeuro
	cotacaoeuro = jogaeuro()



'''Data de atualização'''
try:
	ensaboado3 = sabao.find(class_="section-info")
	data = (ensaboado3.text).replace("Câmbio","").replace("    ", " ")
except Exception:
	data = " Atualizado em não encontrado "

'''Bitcoin'''
try:
	ensaboado4 = sabao.find_all(class_="linhaDados")[3]
	r = (ensaboado4.text).replace("Bitcoin","").replace("%US$","")
	l = r.split()
	cotacaobitcoin = cotacaodolar*float(str(l.pop(1)).replace(".","").replace(",","."))
except Exception:
	from dolareuro import jogabit
	cotacaobitcoin = jogabit()


cotacaobitcoindol = cotacaodolar/cotacaobitcoin
cotacaobitcoineur = cotacaoeuro/cotacaobitcoin


'''Notícia'''
try:
	ensaboado5 = sabao.find_all('h1')[0]
	noticia = ensaboado5.text
except Exception:
	noticia = "Não encontrado"


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


print('''████▀░░░░░░░░░░░░░░░░░▀████
███│░░░░░░░░░░░░░░░░░░░│███
██▌│░░░░░░░░░░░░░░░░░░░│▐██
██░└┐░░░░░░░░░░░░░░░░░┌┘░██
██░░└┐░░░░░░░░░░░░░░░┌┘░░██
██░░┌┘▄▄▄▄▄░░░░░▄▄▄▄▄└┐░░██
██▌░│██████▌░░░▐██████│░▐██
███░│▐███▀▀░░▄░░▀▀███▌│░███
██▀─┘░░░░░░░▐█▌░░░░░░░└─▀██
██▄░░░▄▄▄▓░░▀█▀░░▓▄▄▄░░░▄██
████▄─┘██▌░░░░░░░▐██└─▄████
█████░░▐█─┬┬┬┬┬┬┬─█▌░░█████
████▌░░░▀┬┼┼┼┼┼┼┼┬▀░░░▐████
█████▄░░░└┴┴┴┴┴┴┴┘░░░▄█████
███████▄░░░░░░░░░░░▄███████				
''')
print("_____________________________Sobre_______________________________________\n")
print("Conversor monetário desenvolvido por InimigoMortal")
print("Os valores são tirados em tempo real do https://economia.uol.com.br/cotacoes\nEm caso de erro os valores são tirados do Yahoo/Google! \n" + data[1:] + "\n")
print("_____________________________Cotações____________________________________\n")
print("Dólar: " + str(cotacaodolar) + " Euro: " + str(cotacaoeuro) + " Bitcoin: " + str(round(cotacaobitcoin, 2)) +'\n')
print("_____________________________Notícia_____________________________________\n")
print(noticia)
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


	

	