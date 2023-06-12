#Estructuras de control iterativas o bucles o loops

#WHILE

variable = 1
while variable <= 10:
    print(variable)
    variable += 1 #variable = variable + 1

print("fin del ciclo while")


cont = 1
# suma = 0
# while cont <= 5: # Bloque de codigo 1
#     num = int(input("Ingrese un numero: ")) # Bloque de codigo 2
#     print(num)
#     suma += num #suma = suma + num
#     cont += 1 #num = num + 1
#     print("La suma es: ", suma)

# print("fin del ciclo while")


sum = 0
while True:  #bloque de codigo 1
    ingreso = int (input("ingrese un numero")) #bloque de codigo 2
    sum += ingreso

    if ingreso == 0: #condicion de
        break #rompe el ciclo

print ( f" la suma es {sum}")
