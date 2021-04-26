def maior_numero(num1, num2, num3):
    if (num1 > num2 and num1 > num3):
        print(num1)
    elif (num2 > num1 and num2 > num3):
        print(num2)
    else:
        print(num3)
        
        
def depara_palavras(frase):
    frase.split()
    return(frase.split())        
  

def soma_lista():
    lista = [3, 6, 3, 2, 1]
    return(sum(lista))


def junta_palavras():
    lista = ['seu', 'joao', 'esta', 'aqui']
    return (" ".join(lista))

  
# Página 2


def numeros_pares():
    lista_numeros = [3, 8, 9, 1, 0, 2]
    i = 0
    numeoros_pares = []
    while i < len(lista_numeros):
        if lista_numeros[i] % 2 == 0:
            numeoros_pares.append(lista_numeros[i])
        i += 1
    return(numeoros_pares)


def maiores_4():
    lista_numeros = [3, 8, 9, 1, 0, 2]
    i = 0
    soma = 0
    numeros_pares = []
    x = 0
    while i < len(lista_numeros):
        if lista_numeros[i] > 4:
            numeros_pares.append(lista_numeros[i])
        i += 1
    return(sum(numeros_pares))


def media():
    lista_numeros = [3, 8, 9, 1, 0, 2]
    return(sum(lista_numeros)/len(lista_numeros))


lista_numeros = [3, 8, 9, 1, 0, 2]
print("|".join(str(lista_numeros)))


def ordena():
    lista_numeros = [3, 8, 9, 1, 0, 2]
    lista_numeros.sort()
    print(lista_numeros)
    return ordena()
  
  
def decrescente():  
    lista_numeros = [3, 8, 9, 1, 0, 2]
    lista_numeros.sort(key=int, reverse=True)
    return derescente()

  
# Página 3

lista_numeros = [4, 5, 2, 0, 9]
print(lista_numeros)


lista_numeros = [4, 5, 2, 0, 9]
print(lista_numeros[0 : -2])


lista_numeros = [4, 5, 2, 0, 9]
lista_numeros.sort(key=int)
print(lista_numeros[0 : -2])



lista_numeros = [4, 5, 2, 0, 9]
lista_numeros.sort(key=int, reverse=True)
print(lista_numeros[0 : -2])


#Página 4


print(list(range(11)))


print([2*x for x in range(11)])


from random import randint
print( [randint(0, 20) for x in range(20)])


#Página 5


lista = ["alo", "Alo", "aLO", "alO"]
nova_lista = []
palavra0 = lista[0]
palavra1 = lista[1]
palavra2 = lista[2]
palavra3 = lista[3]
palavras = palavra0.lower(), palavra1.lower(), palavra2.lower(), palavra3.lower()
nova_lista.append(palavras)
print(nova_lista)


lista = ["alo", "Alo", "aLO", "alO"]
nova_lista = []
palavra0 = lista[0]
palavra1 = lista[1]
palavra2 = lista[2]
palavra3 = lista[3]
palavras = palavra0.upper(), palavra1.upper(), palavra2.upper(), palavra3.upper()
nova_lista.append(palavras)
print(nova_lista)
