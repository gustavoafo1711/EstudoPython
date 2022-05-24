"""
List Comprehension

- Podemos adicionar estruturas condicionais lógicas as nossas list comprehensions
"""

# 1
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [numero for numero in numeros if numero % 2 == 0]
impares = [numero for numero in numeros if numero % 2 != 0]

print(pares)
print(impares)

# Refatorando
print(f'pares: {[numero for numero in range(1, 11) if numero % 2 == 0]}')
print(f'impares: {[numero for numero in range(1, 11) if numero % 2 != 0]}')


# 2

res = [numero * 2 if numero % 2 == 0 else numero / 2 for numero in numeros]
print(res)
