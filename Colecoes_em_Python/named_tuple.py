"""
Módulo Collections - Named Tuple

# Named Tuple -> São tuplas diferenciadas onde especificamos um nome a mesma e também parâmetros.
"""

# Fazendo import
from collections import namedtuple

# Precisamos definir o nome e parâmetros

# Forma 1 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade raca nome')

# Forma 2 - Declaração Named Tuple

cachorro = namedtuple('cachorro', 'idade, raca, nome')

# Forma 3 - Declaração Named Tuple

cachorro = namedtuple('cachorro', ['idade', 'raca', 'nome'])


# Utilizando

ray = cachorro(idade=2, raca='Chow-Chow', nome='Ray')
print(ray)

#Acessando os dados

# Forma 1
print(ray[0])  # Idade
print(ray[1])  # Nome
print(ray[2])  # Raça


# Forma 2
print(f'\n{ray.idade}')  # Idade
print(ray.raca)  # Raça
print(ray.nome)  # Nome

print(ray.index('Chow-Chow'))

print(ray.count('Chow-Chow'))
