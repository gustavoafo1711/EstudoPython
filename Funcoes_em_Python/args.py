"""
Entendendo o *args

- O *args é um parâmetro como outro quaquer. Isso significa que você poderá
chamar de qualquer coisa, desde que começe com asterisco.

Exemplo:
*xis

Mas por convenção, utilizamos *args para definí-lo.

Mas o que é o *args?
- O parâmetro *args utilizados em uma função, coloca os valores extras informadso como entrada
em uma tupla. Então desde já lembre-se que tuplas são imutáveis.
"""

"""
# Entendendo o *args


def soma_todos_numeros(*args):
    return sum(args)


print(soma_todos_numeros())
print(soma_todos_numeros(1))
print(soma_todos_numeros(2, 3))
print(soma_todos_numeros(2, 3, 4))
print(soma_todos_numeros(3, 4, 5, 6))
"""

"""
def verifica_info(*args):
    if 'Geek' in args and 'University' in args:
        return 'Bem-vindo Geek!'
    return 'Eu não tenho certeza que você é.....'


print(verifica_info())
print(verifica_info(1, True, 'University', 'Geek'))
print(verifica_info(1, 'University', 3.145))
"""


def soma_todos_numeros(*args):
    return sum(args)


# print(soma_todos_numeros())
# print(soma_todos_numeros(3, 4, 5, 6))

numeros = [1, 2, 3, 4, 5, 6, 7]

# Desempacotador -> usando asterisco

print(soma_todos_numeros(*numeros))

# Obs: O asterisco serve para que informemos ao Python que estamos passando como argumento uma coleção de dados
# desta forma ele saberá que precisará antes desempacotar estes dados.

