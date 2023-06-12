# #funciones en python

# def suma(numero1, numero2):
#     return numero1 + numero2


# #programa principal

# valor_suma = suma(5, 6)

# print(valor_suma)


def sumar_numeros_pares(inicio, fin):
    suma = 0

    while inicio <= fin:
        if inicio % 2 == 0:
            suma += inicio
        inicio += 1

    return suma


print(sumar_numeros_pares(1,10))

print("la suma es: ", sumar_numeros_pares(1,10))




