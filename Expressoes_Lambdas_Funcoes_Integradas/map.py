"""
map()

Com map, fazemos mapeamento de valores para função.

"""


"""
import math


def area(r):
    # Calcula a área de um circulo com raio 'r'
    return math.pi * (r ** 2)


print(area(2))
print(area(5.3))


raios = [2, 5, 7.1, 0.3, 10, 44]

# Forma comum
areas = []
for r in raios:
    areas.append(area(r))

print(areas)


# Utilizando Map
# Map é uma função que recebe dois parâmetros: O primeiro a função, o segundo um iterável

areas = map(area, raios)
print(list(areas))


# map() com lambda
print(list(map(lambda r: math.pi * (r ** 2), raios)))

# Após utilizar a função map(), depois da primeira utilização do resultado, ele zera.
"""


cidades = [('Berlin', 29), ('Cairo', 36), ('Buenos Aires', 19), ('Los Angeles', 26), ('Tokio', 27), ('Nova York', 28),
           ('Londres', 22)]

print(cidades)

# f = 9/5 * c + 32

c_para_f = lambda dado: (dado[0], (9/5) * dado[1] + 32)

print(list(map(c_para_f, cidades)))
