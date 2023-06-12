# # Esto es un comentario en Python
# print("hola mundo")


# '''
# Esto es un comentario de varias lineas
# lineas
# lineas

# '''

# print("hola mundo2")
# print("HOla mundo3")

# # Tipos de datos

# # String
# # Integer
# # Float
# # Boolean
# # List
# # Tuple
# # Dictionary

# # String - Cadena de texto

# nombre = "Juan"
# apellido = 'Perez' 

# print(nombre)

# # Integer - Entero

# numero = 10
# numero2 = 20

# print(numero + numero2)

# # Float - Decimal o flotante 

# numero3 = 10.5
# numero4 = 20.5

# print(numero3 + numero4)

# # Boolean - Verdadero o falso

# verdadero = True
# falso = False

# print(verdadero)
# print(falso)

# # List - Lista
# # una lista es un conjunto de datos que se pueden almacenar en una variable

# lista = [1,2,3,4,5,6,7,8,9,10]

# print(lista)

# # Tuple - Tupla
# # una tupla es un conjunto de datos que se pueden almacenar en una variable pero no se pueden modificar

# tupla = (1,2,3,4,5,6,7,8,9,10)

# print(tupla)

# # Dictionary - Diccionario
# # un diccionario es un conjunto de datos que se pueden almacenar en una variable pero se almacenan en pares de llave y valor

# diccionario = {
#     "nombre": "Juan",
#     "apellido": "Perez",
#     "edad": 20
# }

# # variables en Python

# # las variables en Python son dinamicas, es decir, no es necesario declarar el tipo de dato que va a almacenar

# variable = "hola mundo"

# nombre_apellido = "Juan Perez" # snake case
# nombreApellido = "Juan Perez" # camel case
# NombreApellido = "Juan Perez" # Pascal case

# #1nombre = "Juan" # no se puede iniciar con un numero

# nombre1 = "Juan" # si se puede iniciar con un numero

# # Constantes en Python

# # las constantes en Python son variables que no se pueden modificar

# PI = 3.1416

# print(PI)

# # Expresiones en Python

# # las expresiones en Python son operaciones matematicas

# # una expresion es una operacion matematica que se puede evaluar
 
# 4 + 4

# # una sentencia es una operacion matematica que se puede ejecutar

# variable = 4 + 4 + 5 + 6 # sentencia de asignacion

# # setencia de mas de una linea
# variable2 = 4 + 4 + 5 + 6 + \
# 4 + 4 + 5 + 6

# # setencia de mas de una linea
# variable3 = [1,2,3,4,5,6,7,8,9,10,11,
# 12,13,14,15,16,17,18,19,20]

# print(variable)
# print(variable2)
# print(variable3)

# # Bloques de codigo en Python

# # los bloques de codigo en Python se definen por la identacion

# def suma_numeros(numeros): # funcion bloque1
#     suma = 0 # bloque2
#     for numero in numeros: # bloque2
#         suma = suma + numero # bloque3
#     print(suma) # bloque3
#     return suma # bloque2

# print(suma_numeros([1,2,3,4,5,6,7,8,9,10]))

# # Palabras reservadas en Python

# # las palabras reservadas en Python son palabras que no se pueden utilizar como variables
# '''
# and, as, assert, break, class, continue, def, del, elif,
# else, except, False, finally, for, from, global, if,
# import, in, is, lambda, None, nonlocal, not, or, pass, 
# raise, return, True, try, yield, while, with
# '''

# # print se muestra en la consola
# # input se muestra en la consola y se puede ingresar un valor

# #nombre = input("Ingrese su nombre: ")

# print("Hola " + nombre)

# # Concatenacion de cadenas

# nombre = "Juan"
# apellido = "Perez"

# print(nombre + " " + apellido)

# # Formateo de cadenas

# nombre = "Juan"
# apellido = "Perez"

# print("Hola {} {}".format(nombre, apellido))

# # Conversion de tipos de datos

# numero = 10
# numero2 = 20

# print(str(numero) + str(numero2))

# numero = "10"
# numero2 = "20"

# print(int(numero) + int(numero2))

# numero = "10.5"
# numero2 = "20.5"

# print(float(numero) + float(numero2)) # 31.0

# # Operadores aritmeticos

# # + suma
# # - resta
# # * multiplicacion
# # / division
# # % modulo
# # ** potencia
# # // division entera

# numero = 10
# numero2 = 20

# print(numero + numero2) # 30

# print(numero - numero2) # -10

# print(numero * numero2) # 200

# print(numero / numero2) # 0.5

# print(numero % numero2) # 10

# print(numero ** numero2) # 100000000000000000000

# print(numero // numero2) # 0

# # Operadores de asignacion

# # = asignacion
# # += suma y asignacion
# # -= resta y asignacion
# # *= multiplicacion y asignacion
# # /= division y asignacion
# # %= modulo y asignacion
# # **= potencia y asignacion
# # //= division entera y asignacion

numero = 10

numero += 10 # 20


print(numero)


# operadores de pertenencia

# in
# not in

lista = [1,2,3,4,5,6,7,8,9,10]

print(1 in lista) # True

print(11 in lista) # False

# ejemplo de not in

print(1 not in lista) # False

print(11 not in lista) # True


# operadores de identidad

# is

numero = 10

numero2 = 10

print(numero is numero2) # True

# ejemplo de not is

numero = 20

numero2 = 20

print(numero is not numero2) # True

# operadores logicos

# and
# or
# not

numero = 10

numero2 = 20

print(numero == 10 and numero2 == 20) # True

print(numero == 10 or numero2 == 20) # True

print(not numero == 10) # False 

# operadores de comparacion

# == igual

numero = 10

print(numero == 10) # True

# != diferente

numero = 10

print(numero != 10) # False

# > mayor que

numero = 10

print(numero > 10) # False

# < menor que

numero = 10

print(numero < 10) # False

# >= mayor o igual que

numero = 10

print(numero >= 10) # True

# <= menor o igual que

numero = 10

print(numero <= 10) # True

# Estructuras de control en Python

# # Estructuras de control en Python

# # if

numero = 12

if numero == 10: # condicion
    print("El numero es igual a 10") # bloque de codigo
else: # condicion
    print("El numero no es igual a 10") # bloque de codigo

# # if anidado

numero = 12

if numero == 10: # condicion
    print("El numero es igual a 10") # bloque de codigo
elif numero == 11: # condicion
    print("El numero es igual a 11") # bloque de codigo
elif numero == 12: # condicion
    print("El numero es igual a 12") # bloque de codigo
else: # condicion
    print("El numero no es igual a 10, 11 o 12") # bloque de codigo











