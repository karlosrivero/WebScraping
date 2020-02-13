import requests
from bs4 import BeautifulSoup
from datetime import datetime
import csv

headers = {
   "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) '
                 'Chrome/78.0.3904.108 Safari/537.36'}


# -- PRUNE -- #

url_Prune = 'https://www.prune.com.ar/p009883bfaa1.html'
pagePrune = requests.get(url_Prune, headers=headers)
soupPrune = BeautifulSoup(pagePrune.content,'html.parser')

titlePrune = soupPrune.find('span', attrs={'class':'base'})
pricePrune = soupPrune.find('span', attrs={'class':'price'}).text.strip('>')

# -- CAPPIO -- #

url_Cappio = 'https://www.cappio-web.com/productos/derby-cuero-negro-con-charol-negro/'
pageCappio = requests.get(url_Cappio, headers=headers)
soupCappio = BeautifulSoup(pageCappio.content,'html.parser')

titleCappio = soupCappio.find(id='titulo_producto').get_text()
priceCappio = soupCappio.find(id='price_display').get_text()

# -- PETER KENT -- #

url_Peter = 'https://www.peterkent.com.ar/shop/shopping-con-mandala/'
pagePeter = requests.get(url_Peter, headers=headers)
soupPeter = BeautifulSoup(pagePeter.content,'html.parser')

titlePeter = soupPeter.find('h1', attrs={'class':'product_title entry-title'})
pricePeter = soupPeter.find('span', attrs={'class':'woocommerce-Price-amount amount'}).text.strip('>')

# -- XL -- #

url_Xl = 'https://www.xlshop.com.ar/cartera-cagua-tote-xc9sba10c0814/p'
pageXl = requests.get(url_Xl, headers=headers)
soupXl = BeautifulSoup(pageXl.content,'html.parser')

titleXl = soupXl.find('div', attrs={'class':'productName'})
priceXl = soupXl.find('strong', attrs={'class':'skuPrice'}).text

# -- JACKIE SMITH -- #

url_JM = 'https://jackiesmith.com.ar/products/cn00763pca90v99'
pageJM = requests.get(url_JM, headers=headers)
soupJM = BeautifulSoup(pageJM.content,'html.parser')

titleJM = soupJM.find('h3', attrs={'class':'product-title page-title'})
priceJM = soupJM.find('span', attrs={'class':'mw-price'}).text.strip('>')

# -- MISHKA -- #

url_Mis = 'https://www.mishka.com.ar/m000062bnaa1.html'
pageMis = requests.get(url_Mis, headers=headers)
soupMis = BeautifulSoup(pageMis.content,'html.parser')

titleMis = soupMis.find('span', attrs={'class':'base'})
priceMis = soupMis.find('span', attrs={'class':'price'}).text.strip('>')

# -- BESHA -- #

url_Bes = 'https://www.besha.com.ar/productos/bolsa-jupiter1/'
pageBes = requests.get(url_Bes, headers=headers)
soupBes = BeautifulSoup(pageBes.content,'html.parser')

titleBes = soupBes.find('h1', attrs={'uppercase text-center text-grey-darkest text-lg mt-4'})
priceBes = soupBes.find('h4', attrs={'class':'product-price text-grey-darkest my-4'}).text.strip('>')

# ---  CSV  --- #

titulos = 'Prune, Cappio, Peter Kent, XL, Jackie Smith, Mishka, Besha\n'
nombres = (str(titlePrune.text)+','+str(titleCappio)+','+str(titlePeter.text)+','+str(titleXl.text)+','+
          str(titleJM.text)+','+str(titleMis.text)+','+str(titleBes.text)+'\n')
precios = (str(pricePrune)+','+str(priceCappio)+','+str(pricePeter)+','+str(priceXl)+','+str(priceJM)+','+
          str(priceMis)+','+str(priceBes)+'\n')

hoy = datetime.now()
fecha = hoy.strftime('%d/%m/%Y')

preciosEx = open('precios.csv','a', encoding='utf-8')

#preciosEx.write(titulos)
#preciosEx.write(nombres)
preciosEx.writelines('\n' + precios + str(fecha))


preciosEx.close()
