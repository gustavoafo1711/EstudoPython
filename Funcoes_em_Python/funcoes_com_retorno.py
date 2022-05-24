"""
Funções com retorno

Obs: Em Python quando uma função não retorna nenhum valor, o retorno é None

Obs: Funções Python que retornam valorem, devem retornar estes valores com a palavra
reservada return

Obs: Não precisamos necessariamente criar uma variável para receber o retorno de uma
função. Podemos passar a execução d função para outras funções.

"""

"""
# Exemplo função


def quadrado_de_7():
    print(7 * 7)


ret = quadrado_de_7()

print(f'Retorno {ret}')


# Refatorando a função  para que ela retorne o valor


def quadrado_de_7():
    return 7 * 7


# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno {ret}')

print(f'Retorno {quadrado_de_7()}')


# Refatorando o primeira função


def diz_oi():
    return 'Oi!'


print(diz_oi())


Obs: Sobre a palavra resevada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter em uma função diferentes returns;
3 - Podemos em uma função retornar qualquer tipo de dado e até mesmo multiplos valores;

# Exemplo 1


def diz_oi():
    print('Estou sendo executado antes do retorno...')
    return 'Oi! '
    print('Estou sendo executado após o retorno...')


print(diz_oi())

# Exemplos 2


def nova_função():
    variavel = False
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'


print(nova_função())


# Exemplos 3


def outra_funcao():
    return 2, 3, 4, 5


num1, num2, num3, num4 = outra_funcao()

print(num1, num2, num3, num4)

"""

# vamos criar uma função para cara ou coroa

from random import random


def joga_moeda():
    # Gera um número pseudo-ramdômico entre 0 e 1
    if random() > 0.5:
        return 'Cara'
    return 'Coroa'


print(joga_moeda())


