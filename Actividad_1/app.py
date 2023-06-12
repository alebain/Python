#1. escribe un programa que escriba en pantalla la frase Hello World
print("Hello World")

#2. escribe en pantalla resultado de sumas 3+5
resultado = 3 + 5
print("El resultado de la suma es:", resultado)

#3. Escribe un programa que pida el nombre del usuario y escriba un texto que diga “Hola nombreUsuario”
nombreUsuario = input("Ingrese su nombre: ")
print("¡Hola", nombreUsuario + "!") 

#4. Escribe un programa que pida un número, pida otro número y escriba el resultado de sumar estos dos números.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

resultado = num1 + num2
print("El resultado de la suma es:", resultado)

#5. Escribe un programa que pida dos números y escriba en la pantalla cual es el mayor.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))

if num1 > num2:
    print("El mayor número es:", num1)
elif num2 > num1:
    print("El mayor número es:", num2)
else:
    print("Ambos números son iguales.")

#6 Escribe un programa que pida 3 números y escriba en la pantalla el mayor de los tres.
num1 = float(input("Ingrese el primer número: "))
num2 = float(input("Ingrese el segundo número: "))
num3 = float(input("Ingrese el tercer número: "))

mayor = num1

if num2 > mayor:
    mayor = num2

if num3 > mayor:
    mayor = num3

print("El mayor número es:", mayor)

#7 Escribe un programa que pida un número y diga si es divisible por 2
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número", numero, "es divisible por 2.")
else:
    print("El número", numero, "no es divisible por 2.")

#8 Escribe un programa que pida un número y nos diga si es divisible por 2, 3, 5 o 7 (sólo hay que comprobar si lo es por uno de los cuatro)
numero = int(input("Ingrese un número: "))

if numero % 2 == 0:
    print("El número", numero, "es divisible por 2.")
elif numero % 3 == 0:
    print("El número", numero, "es divisible por 3.")
elif numero % 5 == 0:
    print("El número", numero, "es divisible por 5.")
elif numero % 7 == 0:
    print("El número", numero, "es divisible por 7.")
else:
    print("El número", numero, "no es divisible por 2, 3, 5 ni 7.")

#9 Añadir al ejercicio anterior que nos diga por cuál de los cuatro es divisible (hay que decir todos por los que es divisible)
numero = int(input("Ingrese un número: "))

divisibles = []

if numero % 2 == 0:
    divisibles.append(2)
if numero % 3 == 0:
    divisibles.append(3)
if numero % 5 == 0:
    divisibles.append(5)
if numero % 7 == 0:
    divisibles.append(7)

if len(divisibles) > 0:
    print("El número", numero, "es divisible por", ', '.join(map(str, divisibles)))
else:
    print("El número", numero, "no es divisible por 2, 3, 5 ni 7.")

#10 Escribir un programa que escriba en pantalla los divisores de un número dado
numero = int(input("Ingrese un número: "))

divisores = []

for i in range(1, numero + 1):
    if numero % i == 0:
        divisores.append(i)

print("Los divisores de", numero, "son:", divisores)

#11 Escribir un programa que nos diga si un número dado es primo (no es divisible por ninguno otro número que no sea él mismo o la unidad)
numero = int(input("Ingrese un número: "))

es_primo = True

if numero < 2:
    es_primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            es_primo = False
            break

if es_primo:
    print(numero, "es un número primo.")
else:
    print(numero, "no es un número primo.")

#12 Pide una nota (número). Muestra la calificación según la nota: 0-3: Muy deficiente 3-5: Insuficiente 5-6: Suficiente 6-7: Bien 7-9: Notable 9-10: Sobresaliente

nota = float(input("Ingrese la nota: "))

if nota >= 0 and nota < 3:
    calificacion = "Muy deficiente"
elif nota >= 3 and nota < 5:
    calificacion = "Insuficiente"
elif nota >= 5 and nota < 6:
    calificacion = "Suficiente"
elif nota >= 6 and nota < 7:
    calificacion = "Bien"
elif nota >= 7 and nota < 9:
    calificacion = "Notable"
elif nota >= 9 and nota <= 10:
    calificacion = "Sobresaliente"
else:
    calificacion = "Nota inválida"

print("La calificación correspondiente a la nota", nota, "es:", calificacion)


#13 Realiza un programa que escriba una pirámide del 1 al 30 de la siguiente forma: 1 / 22 / 333 / 4444 / 55555 / 666666


for i in range(1, 31):
    linea = str(i) * i
    print(linea)

#14 Haz un programa que escriba una pirámide inversa de los números del 1 al número que indique el usuario de la siguiente forma (suponiendo que indica 6):
666666

55555
 
4444

333

22

1

numero = int(input("Ingrese un número: "))

for i in range(numero, 0, -1):
    linea = str(i) * i
    print(linea)

#15 Crear un programa que escriba los números del 1 al 500, y que indique cuales son múltiplos de 4 y de 9 y que cada 5 líneas muestre una línea horizontal. Por ejemplo: 1/ 2  / 3 / 4 (Múltiplo de 4) / 5 / 6 / 7 / 8	(Múltiplo de 4) / 9	(Múltiplo de 9) / 10

for i in range(1, 501):
    if i % 4 == 0 and i % 9 == 0:
        print(i, "(Múltiplo de 4 y de 9)")
    elif i % 4 == 0:
        print(i, "(Múltiplo de 4)")
    elif i % 9 == 0:
        print(i, "(Múltiplo de 9)")
    else:
        print(i)
    
    if i % 5 == 0:
        print("-" * 10)
