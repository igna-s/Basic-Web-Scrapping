def main():
    f = open('web.html', 'rb')
    inicio = '<title>'
    fin = '</title>'
    for linea in f.readlines():
        linea = str(linea)
        if inicio in linea:
             x = linea.find(inicio)
             x = x + len(inicio)
             y = linea.find(fin)
             print(linea[x:y])


if __name__ == '__main__':
    main()
