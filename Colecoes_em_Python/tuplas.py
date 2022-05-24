"""
Tuplas (tuple)

Tuplas são bastante parecidas com listas, existem basicamente duas diferenças básicas.

1 - As tuplas são representadas por parênteses ().

2 - As tuplas são imutáveis, isso significa que ao se criar uma tupla, ela não muda. Toda
operação em uma tupla gera uma nova tupla.


"""

# CUIDADO 1: As tuplas são representadas por (), mas veja:
print('# CUIDADO 1: As tuplas são representadas por (), mas veja:')
tupla1 = (1, 2, 3, 4, 5, 6)
print(tupla1)

print(type(tupla1))

tupla2 = 1, 2, 3, 4, 5, 6
print(tupla2)
print(type(tupla2))


# CUIDADO 2: Tuplas com 1 elemento
print('\n# CUIDADO 2: Tuplas com 1 elemento')
tupla3 = (4)  # Isso não é uma tupla
print(tupla3)

print(type(tupla3))

tupla4 = (4,)  # Isso é uma tupla
print(tupla4)

print(type(tupla4))

# COMCLUSÃO: Podemos concluir que tuplas são definidas pela vírgula e não pelo uso do parênteses.

print('\nGerando tuplas com range: Ex. tupla = tuple(range(11))')
tupla = tuple(range(11))
print(tupla)
print(type(tupla))


print('\nDesempacotamento de tupla')
tupla = ('Geek University', 'Programação em Python: Essenmcial')

escola, curso = tupla
print(escola)
print(curso)
# obs: Gera erro (ValueError) se colocarmos um número diferente de elementos para desempacotar.

# Métodos para adição e remoção de elementos nas tuplas não existem, dado o fato das tuplas serem imutáveis.

print('\nconcatenação de tuplas.')
tupla1 = 1, 2, 3
print(tupla1)
tupla2 = 4, 5, 6
print(tupla2)

print(tupla1 + tupla2)
print(tupla1)
print(tupla2)

# Tuplas são imutáveis, mas podemos sobrescrever seus valores.
print('\nTuplas são imutáveis, mas podemos sobrescrever seus valores. Ex. tupla1 = tupla1 + tupla2')
tupla1 = tupla1 + tupla2
print(tupla1)
print(type(tupla1))


"""
Dicas na utilização de tuplas:
- Devemos utilizar tyuplas sempre que não precisarmos modificar os dados contidos em uma coleção.
Ex: meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
             'outubro', 'novembro', 'dezembro')
             
- O acesso a elementos de uam tupla também é semelhante a de uma lista:
Ex: print(meses[5]) --> 'junho'

"""

print('\n Verificamos em qual índice um elemento está na tupla.')
meses = ('janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro',
         'outubro', 'novembro', 'dezembro')

print(meses)
print(f"Junho está no índice {meses.index('junho')}")


"""
Por quê utilizar tuplas?

- Tuplas são mais rápidas do que listas.
- Tuplas deixam seu código mais seguro, pois trabalhar com elementos imutáveis tras segurança para o código.


"""

print('\nCopiando uma tupla para outra.')

tupla = (1, 2, 3)
print(tupla)

nova = tupla  # Na tupla não temos o problema de Shallow Copy
print(nova)
print(tupla)

outra = (4, 5, 6)
nova = nova + outra
print(nova)
print(tupla)





