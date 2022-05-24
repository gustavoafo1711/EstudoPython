"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;


"""

"""
# Refatorando uma função


def quadrado(numero):
    return numero ** 2


print(quadrado(7))
print(quadrado(5))
"""

"""
def cantar_parabens(aniversariante):
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print(f'Viva o/a {aniversariante}')


cantar_parabens('João')
"""

# Obs: Funções podem ter n parâmetros de entrada, ou seja, podemos receber como entrada
# em uma função quantos parâmetros forem necessários. Eles são separados por vírgula.

"""
def soma(a, b):
    return a + b


def multiplica(num1, num2):
    return num1 * num2


def outra(num1, b, msg):
    return (num1 + b) * msg


print(soma(2, 5))
print(soma(10, 20))

print(multiplica(4, 5))
print(multiplica(2, 8))

print(outra(3, 2, 'geek '))
print(outra(5, 4, 'python '))


# Obs: Se a gente informar um número errado de parâmetro ou argumentos, teremos TypeError
# print(soma(2, 3, 4))  TypeError - Passando argumentos a mais
# print(soma(2))  TypeError - Passando argumentos a menos
"""

# Diferença entre Parâmetro e Argumentos

# Parâmetros são variáveis declaradas na definição de uma função.
# Argumentos são dados passados durante a execução de uma função.

# A ordem dos parâmetros importa
