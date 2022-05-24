"""
Listas Aninhadas (Nested Lists)

- algumas linguagens de programação possuem uma estrutura de dados chamadas de arrays:
    - Unidimendionais;
    - Multidimendionais;

Em Python nós temos as Listas

numero = [1, 2, 3, 4, 5, 'b', False, 3.567]
"""

"""
# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

print(listas)
print(type(listas))


# Como fazemos para acessar os dados

print(listas[0][1])  # Acesso número 2
print(listas[2][2])  # Acesso número 9
print(listas[-2][-3])  # Acesso número 4 índice negativo
"""


# Iterando com loops com listas aninhadas
listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 x 3

# for lista in listas:
#     for numero in lista:
#        print(numero)


# List comprehension
[[print(valor) for valor in lista] for lista in listas]

# outros exemplo

# Gerando matriz 3x3
tabuleiro = [[numero for numero in range(1, 4)] for valor in range(1, 4)]
print(tabuleiro)

