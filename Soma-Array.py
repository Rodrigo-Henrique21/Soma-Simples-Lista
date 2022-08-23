#Definindo as listas

lista = [1,2,3,4,5]
lista2 = [5]

#Somando os elementos contidos na 1º lista

def soma_1():
    contador = 0 
    for i in lista:
        contador += i
    valor = print(str(contador))
    return 
    valor
     
soma_1()

#Somando os elementos contidos na 1º e 2º lista

def soma_2():
    lista3 = lista+lista2
    cont = 0
    for item in lista3:
        cont+=item
    valor_2 = print(str(cont))
    return 
    valor_2 

soma_2()