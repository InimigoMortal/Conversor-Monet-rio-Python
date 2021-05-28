import requests
from bs4 import BeautifulSoup

r = requests.get('https://economia.uol.com.br/cotacoes/')
sabao = BeautifulSoup(r.text , 'html.parser')


req = requests.get('https://www.infomoney.com.br/ferramentas/cambio/')                                           
sab = BeautifulSoup(req.text , 'html.parser')

re = requests.get('https://br.financas.yahoo.com/')
s = BeautifulSoup(re.text , 'html.parser')

dado = requests.get('https://www.google.com/search?client=firefox-b-d&ei=y97vXP6UO-rA5OUPyc6QyAs&q=converter+bitcoin+em+real&oq=converter+bitcoin+em+real&gs_l=psy-ab.3..0i324j0j0i22i30l6.1375569.1379057..1379248...0.0..0.144.2000.0j15......0....1..gws-wiz.......0i71j0i131j35i39.R-bUcd8uriE')
le = BeautifulSoup(dado.text , 'html.parser')



 


def jogadolar():
    ens = sab.find_all('td')[22].text.replace(",",".")
    valordol = float(ens)
    return valordol
def jogaeuro():
    esb = sab.find_all('td')[32].text.replace(",",".")
    valoreuro = float(esb)
    return valoreuro
def jogabit():
    leia = le.find_all('span')[30]       
    valorbit = float(leia.text.replace("R$","").replace(",00","").replace(".",""))
    return valorbit



'''Dólar'''
try:
	ensaboado = sabao.find_all(class_="subtituloGrafico subtituloGraficoValor")[0]
	remove = (ensaboado.text).replace("R$", "")
	cotacaodolar = float(remove.replace(",", "."))
except Exception:
	
	cotacaodolar = jogadolar()



'''Euro'''
try:
	ensaboado2 = sabao.find_all(class_="subtituloGrafico subtituloGraficoValor")[2]
	rem = (ensaboado2.text).replace("R$", "")
	cotacaoeuro = float(rem.replace(",", "."))
except Exception:
	
	cotacaoeuro = jogaeuro()


'''Bitcoin'''

try:
	ensaboado4 = sabao.find_all('tr',class_="linhaDados")[3]
	r = ensaboado4.text[16::].replace('.',"")
	r2 = r[:-4]
	cotacaobitcoin = int(r2)
	
except Exception:
	
	cotacaobitcoin = jogabit()



'''Data de atualização'''

try:
	ensaboado3 = sabao.find(class_="section-info")
	data = (ensaboado3.text).replace("Câmbio","").replace("    ", " ")
except Exception:
	data = " Atualizado em não encontrado "


	



cotacaobitcoindol = cotacaodolar/cotacaobitcoin
cotacaobitcoineur = cotacaoeuro/cotacaobitcoin



'''Notícia'''

try:
	ensaboado5 = sabao.find_all('h2')[0]
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



	'''Interface'''


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
print("Conversor monetário desenvolvido por InimigoMortal.")
print("Os valores são tirados em tempo real no momento em que o arquivo é executado. \n" + data[1:] + "\n")
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



	

	
