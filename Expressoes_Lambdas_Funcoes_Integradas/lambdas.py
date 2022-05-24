"""
Utilizando Lambdas

Conhecidas por Expressões Lambdas ou simplesmente Lambdas, são funçõwes sem nome, ou seja,
funções anônimas.


"""

"""
# Função em Python
print('Função em Python')

def funcao(x):
    return 3 * x + 1


print(funcao(4))
print(funcao(7))


# Expressão Lambda
print('\nExpressão Lambda')

# Como utilizar a Expressão Lambda
calc = lambda x: 3 * x + 1


print(calc(4))
print(calc(7))
"""

"""
# Podemos ter expressões lambdas com multiplas entradas

nome_completo = lambda nome, sobrenome: nome.strip().title() + ' ' + sobrenome.strip().title()

print(nome_completo('gustavo      ', '   fontENELE'))
"""


"""
# Em funções Python podemos ter nenhuma ou várias entradas, em lambdas também

amar = lambda: 'Como não mar Python? '

uma = lambda x: 3 * x + 1

duas = lambda x, y: (x * y) ** 0.5

tres = lambda x, y, z: 3 / (1 / x + 1 / y + 1 / z)

# n = lambda x1, x2, .... xn: <expressão>

print(amar())
print(uma(6))
print(duas(5, 7))
print(tres(3, 6, 9))

# Obs: Se passarmos mais argumentos que parâmetros esperados teremos TypeError
"""


"""
# Outro exemplo

autores = ['Isaac Asimov', 'Ray Bradbury', 'Agata Crhistie', 'R. R. Tolken', 'Helen Morin']
print(autores)

autores.sort(key=lambda sobrenome: sobrenome.split(' ')[-1].lower())

print(autores)
"""


# Função Quadratica
# f(x) = a * x ** 2 + b * x + c

# Definindo a função


def geradora_funcao_quadratica(a, b, c):
    """Retorna a função f(x) = a * x ** 2 + b * x + c"""
    return lambda x: a * x ** 2 + b * x + c


teste = geradora_funcao_quadratica(2, 3, -5)

print(teste(0))
print(teste(1))
print(teste(2))

print(geradora_funcao_quadratica(3, 0, 1)(4))
