from urllib.request import urlopen

plugin = urlopen("https://kijam.com/tienda/producto/mercadopago-para-woocommerce/")
pagina = urlopen("https://amaleather.com/store/?v=5b61a1b298a0")

html=plugin.read().decode("utf8")
htmls=pagina.read().decode("utf8")

hoy = html.find("CHANGE LOG")
texto = html[hoy+44:hoy+51]
hoy2 = texto.find('"')

version = htmls.find("www.mercadopago.com/org-img/jsapi/mptools/buttons/render.js?ver=")
texto2 = htmls[version+64:version+70]


print("Versión Kijam: "+texto[:hoy2])
print("Versión A mà: "+texto2[:version])
