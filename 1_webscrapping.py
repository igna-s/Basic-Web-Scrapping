import urllib.request

web = open('Caida_Nviia.html', 'wb')

consulta= urllib.request.urlopen('https://es.investing.com/news/stock-market-news/brutal-nvidia-pierde-hoy-mas-de-medio-billon-de-dolares-en-horas-oportunidad-2989963')
consulta=consulta.read()

web.write(consulta)
web.close()