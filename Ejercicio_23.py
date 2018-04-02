



def main():
    lista = list(range(2,31,2))
    print(lista)
    b = lista[5:]
    print(b)
    c = lista[:7]
    print(c)
    d = lista[::4]
    print(d)
    e = lista[3:len(lista)-3]
    print(e)
    f = lista[::-1]
    print(f)
main()
