def indecx(lista, numero):
    if lista.count(numero) == 1:
        return lista.index(numero)
    elif lista.count(numero) > 1:
        for i in lista:
            return lista.index(numero), lista.index(numero, lista.index(numero)+1)

lista = (5, 8, 1, 2, 2, 5, 4)
numero = int(input())



print(indecx(lista, numero))