"""
Funções com Parâmetro Padrão (Default Parameters)

- Funções onde a passagem de parâmetro seja opcional;
"""

"""
def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 *2 = 8
print(exponencial(3, 2))  # 3 * 3 *3 = 9
print(exponencial(5))  # Por padrão eleva ao quadrado
"""

"""
def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'


print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao(True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))
"""

"""
def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))
"""

"""
# escopo - Evitar problemas e confusões

# Variáveis Globais
# Variáveis Locais

instrutor = 'Geek'  #Variável global


def diz_oi():
    instrutor = 'Python'  # Variável local
    return f' Oi {instrutor}'


print(diz_oi())

# Obs: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.


def diz_oi():
    prof = 'Geek'  # Variavel local
    return f'Olá {prof}'
    
    
print(diz_oi())

print(prof) # NameError, pois a variǘel só existe localmente.
"""

"""
# ATENÇÃO com variáveis globais (se puder evitar, evite!!!)

total = 0


def incrementa():
    total = total +1  # UnboundLocalError ( A variável local está sendo utilizada para processamento ser ter sido inicializada)
    return total


print(incrementa())
"""

"""
# Refatorando para utilizar a variável global e não dar erro
total = 0


def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total = total + 1
    return total


print(incrementa())
print(incrementa())
print(incrementa())
"""

# Podemos ter funções que são declaradas dentro de funções, e també tem uma forma especial de escopo de variável


def fora():
    contador = 0

    def dentro():
        nonlocal contador
        contador = contador + 1
        return contador
    return dentro()


print(fora())
print(fora())
print(fora())
