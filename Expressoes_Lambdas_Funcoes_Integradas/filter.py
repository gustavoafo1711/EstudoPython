"""
Filter

filter() - serve para filtrar dados de uma determinada coleção.

"""

"""
# Biblioteca para trabalhar com dados estatísticos
import statistics

# Dados coletados de algum sensor
dados = [1.3, 2.7, 0.8, 4.1, 4.3, -0.1]

# Calculando a média dos dados utilizando a função mean()
media = statistics.mean(dados)
print(f'média: {media}')
# Obs: Assim como a função map(), a filter recebe dois parâmentros, sendo uma função e um iterável.

res = filter(lambda x: x > media, dados)
print(list(res))
"""

"""
# Remoção de dados faltantes
paises = ['', 'Argentina', '', 'Brasil', 'Chile', '', 'Colombia', '', 'Equador', '', '', 'Venezuela' ]
print(paises)

res = filter(None, paises)
print(list(res))

res = filter(lambda pais: len(pais) > 0, paises)
print(list(res))

res = filter(lambda pais: pais != '', paises)
print(list(res))


# Adiferença entre map() e filter() é:
# map() recebe dois parâmetros, uma função e um iterável e retorna um objeto mapeando a função para
# cada elemento do iterável.

# filter() recebe dois parâmetros uma função e um iterável e retorna um objeto filtrando apenas os
# elementos de acordo com a função.

"""

"""
# Exemplo mais complexo

usuarios = [
    {"username": "samuel", "tweets": ["Eu adoro bolos", "Eu adoro pizzas"]},
    {"username": "carla", "tweets": ["Eu amo meu gato"]},
    {"username": "jeff", "tweets": []},
    {"username": "bob123", "tweets": []},
    {"username": "doggo", "tweets": ["Eu gosto de cachorros", "Vou sair hoje"]},
    {"username": "gal", "tweets": []}
]

print(usuarios)
# Filtrar os usuário que estão inativos no Twiteer

# Forma 1
# inativos = list(filter(lambda u: len(u['tweets']) == 0, usuarios))

# Forma 2
inativos = list(filter(lambda u: not u['tweets'], usuarios))
print(inativos)
"""


# Combinar filte() e map()

nomes = ['Vanessa', 'Ana', 'Maria']

# Devemos criar uma lista contendo 'Sua professora é' + nome, desde que cada nome tenha menos de 5 caracteres

lista = list(map(lambda nome: f'Sua professora é {nome}', filter(lambda nome: len(nome) < 5, nomes)))
print(lista)

