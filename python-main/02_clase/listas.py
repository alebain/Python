#lista en python es una estructura de datos que nos permite almacenar valores

lista = [1,2,3,4,5,6,7,8,9,10] #lista de numeros

lista2 = ["hola", "mundo", "desde", "python"] #lista de strings

lista3 = [1,2,3,4,5,6,7,8,9,10, "hola", "mundo", "desde", "python"] #lista de numeros y strings

#print(lista)

#print(lista[0]) #imprime el primer elemento de la lista

#print(lista[3]) #imprime el cuarto elemento de la lista

for elemento in lista: #recorre la lista
    print("el valor de elemento es: ", elemento)

for elemento in lista2: #recorre la lista
    print("la posicion de elemento es: ", lista2.index(elemento))
    print("el valor de elemento es: ", elemento)




