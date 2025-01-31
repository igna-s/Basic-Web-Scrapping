def main():
    web = open('web.html', 'rb')
    inicio = '<li>'
    fin = '</li>'
    for linea in web.readlines():
        linea = str(linea)
        if inicio in linea:
            if not '<a href' in linea:
                x = linea.find(inicio)
                x = x + len(inicio)
                y = linea.find(fin)
                print(linea[x:y])

if __name__ == '__main__':
    main()
