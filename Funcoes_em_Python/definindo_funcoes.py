"""
Definindo Funções.

- Funções são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entrada de dados e retornar uma saída de dados;
- Muito úteis para executar procedimentos similares por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela, é bom
fazer uma verificação para que a função seja simplificada.

Já utilizamos várias funções desde que iniciamos este curso:
- print()
- len()
- count()
- max()


"""


"""
# Exemplo de utilização de funções:

cores = ['verde', 'amarelo', 'azul', 'branco']

# Utulizando a função integrada (Built-in) do Python
print(cores)

curso = 'Programação em Python essencial'
print(curso)

cores.append('roxo')
print(cores)

# curso.append('mais texto...')  #AttributeError

cores.clear()
print(cores)
"""



# DRY - don't repeat yourself - não repita seu código

# Como definir funções?

"""
Em Python, a forma geral de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao

Onde:

- nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto separado por underline (SnakeCase);
- parametros_de_entrada -> Opcionais, onde tendo mais de um, cada um separado por vírgula, podendo sedr opcionais 
ou não;
- bloco_da_funcao -> Também chamado de corpo da função, ou implementação, é onde o processamento da função acontece,
neste bloco pode ter ou não retorno da função;

OBS: Veja que para dedfinir uma funçaõ, usamos a palavra reservada 'def', informando ao Python
que estamos definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos (:) que é 
utilizado em Python para definir blocos.

"""

# Definindo a primeira função


def diz_oi():
    print('Oi!')


"""
OBS:
1 - Veja que dentro das nossas funções, podemos utilizar outras funções.
2 - Veja que nossa função só executa uma tarefa, ou seja, a única coisa que ela faz é dizer oi.
3 - Veja que esta função no recebe nenhum parâmetro de entrada.
4 - Veja que esta função não retorna nada.
"""

# Utilizando funções

# Chamada de uxucução
diz_oi()


# Exemplo 2

def cantar_parabens():
    print('Parabéns pra você')
    print('Nesta data querida')
    print('Muitas felicidades')
    print('Muitos anos de vida')
    print('Viva o aniversariante')


# for n in range(3):
#    cantar_parabens()


# Em Python podemos inclusive criar variáveis do tipo  de uma função e executar
# esta função através da variável.


canta = cantar_parabens

canta()
