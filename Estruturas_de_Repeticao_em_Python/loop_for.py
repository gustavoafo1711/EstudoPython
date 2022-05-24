"""
Loop for

Loop -> estrutura de repetição.
For -> Uma dessas estruturas.

# Python

for item in interável:
    //execução do loop


Utilizamos loops para iterar sobre sequências ou sobre valores iteráveis.

Exemplos de iteráveis:
- String:
    nome = 'Geek University'
- Lista:
    lista = [1, 3, 5, 7, 9]
-Range:
    range = range(1, 10)

"""


nome = 'Geek University'
lista = [1, 3, 5, 7, 9]
numeros = range(1, 10)  # Temos que transformar em uma lista

"""
# Exemplo de for 1 (Iterando em uma string)
for letra in nome:
    print(letra)
"""

"""
# Exemplo de for 2 (Iterando sobre uma lista)
for numero in lista:
    print(numero)
"""

"""
# Exemplo de for 3 (Iterando sobre um range)

# range(valor_inicial, valor_final)
# Obs: O valor final não é inclusive.

for numero in range(1, 10):
    print(numero)
"""

"""
enumerate:

(0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U'), .....


for indice, letra in enumerate(nome):
    print(nome[indice])

for indice, letra in enumerate(nome):
    print(letra)


for _, letra in enumerate(nome):  # _ se usa para quando tivermos 2 valores descartar um
    print(letra)

# imprime a tupla do enumerate: ex: (0, 'G'), (1, 'e'), (2, 'e'), (3, 'k'), (4, ' '), (5, 'U')
for valor in enumerate(nome):
    print(valor)

"""

"""
qtd = int(input('Quantas vezes esse loop deve rodar?'))

for n in range(1, qtd + 1):
    print(f'Imprimindo {n}')
"""

"""
# Imprimindo sem pular linha
for letra in nome:
    print(letra, end='')  # por padrão o print usa como end=/n e pula linha
"""

emoji = '\U0001F611'
for num in range(1, 11):
    print(f'{emoji * num}')
