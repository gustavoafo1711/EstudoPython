"""
Set Comprehension

"""

numeros = {num for num in range(1, 7)}
print(numeros)
print(type(numeros))


numero = {x ** 2 for x in range(10)}
print(numero)

letras = {letra for letra in 'Gustavo Fontenele'}
print(letras)
