n = int(input(''))

def multiplos(n):
    lista = []
    i = 0
    cinco = 5
    while i < n:
        i += 1
        if i % cinco == 0 and i % 2 != 0:
            lista.append(i)
    print(lista)
    return multiplos(n)

def tamanho_lista():
    n = 3
    s = 0
    lista = []
    while s < int(n):
        s += 1
        k = input('Digite um número: ')
        lista.append(int(k))
    return tamanho_lista()

lista= input('Inssira uma lista de valores: ')
list = lista.split()
lis = []
def exercico_3():
    i = 0
    while i < len(list):
        if int(list[i]) > 5:
            lis.append(list[i])
            i += i
        else:
            i += 1
    return len(lis)

def menu(entrada):
    fut = {'a': 'PSG', 'b': 'BAYERN'}
    if entrada == 'a':
        print(fut['a'])
    if entrada == 'b':
        print(fut['b'])
    if entrada == 'd':
    quit()
    return menu(entrada)
        quit()
    return menu(entrada)
    
