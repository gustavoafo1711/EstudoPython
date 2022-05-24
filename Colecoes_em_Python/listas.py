"""
Listas

Listas em Python funcionam como vetores ou matrizes (arrays em outras linguagens), com
a diferença de serem dinâmicos e também de podermos colocar qualquer tipo de dado.

Linguagem C/Java: Arrays:
    - Possuem tamanho e tipo de dado fixo;
    Ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este
    array será sempre do tipo inteiro e poderá ter sempre no máximo 5 valores.

Já em Python:

- Dinâmico: Não possui tamanho fixo; Ou seja, podemos criar a lista e simplesmente ir adicionando elementos;
- Qualquer tipo de dado: Não possui tipo de ddo fixo, ou seja, podemos colocar qualquer tipo de dado;

As listas em python são representadas por colchetes: []


"""

type([])

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista.
num = 7
if num in lista4:
    print(f'Encontrei o número {num}')
else:
    print(f'Não encontrei o número {num}')


# Podemos facilmente ordenar uma lista.
lista1.sort()
print(f'\nOrdenando a lista1')
print(lista1)


# Podemos facilmente contar o número de ocorrencias de uma valor em uma lista.

print(f"\nEncontrei {lista1.count(1)} números '1' na lista1")

print(f"Encontrei {lista5.count('e')} letras 'e' na lista5")


# Adicionar elementos em listas

"""
Para adicionar valores em listas, utilizamos a função append

Obs: Com appen nós só conseguimos adicionar 1 elemento por vez.
"""
print(f'\nAdicionando elementos na lista.')
print(lista1)
lista1.append(42)
print(lista1)


print('\ninserindo uma lista dentro de outra lista')
print(lista1)
print(lista4)
lista1.append(lista4)  # Coloca a lista como elemento único
print(lista1)

if [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10] in lista1:
    print('Encontrei lista4 dentro da lista1')


print('\nInserindo elementos de uma lista dentro da lista')
lista1.extend([1973, 2021, 1974])  # Coloca cada elemento da lista como valor adicional a lista
print(lista1)


# podemos inserir um novo elemento na lista informando a posição do índice.
# Isso não substitui o valor inicial, o mesmo será deslocado para a direita da lista.
print('\nInserindo um valor informando sua posição no índice')
lista1 = list(range(6))
print(lista1)
lista1.insert(2, 'Novo valor')
print(lista1)


# Podemos facilmente juntar duas lista.
lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]
lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

print('\nPodemos juntar facilmente duas listas.')
lista6 = lista1 + lista2
print(lista6)


# Podemos facilmente inverter uma lista
print('\nPodemos facilmente iverter uma lista utilizando a função reverse()')
lista1.reverse()
lista2.reverse()
print(lista1)
print(lista2)

print('Ou usando o slice ex: print(lista1[::-1])')
print(lista1[::-1])
print(lista2[::-1])


# Podemos contar quantos elementos existem dentro da lista.
print('\nPodemos contar quantos elementos existem dentro da lista: len()')
print(f'A lista2 tem {len(lista2)} elementos.')


# Podemos remover facilmente o último elemento de uma lista.
# Obs: O pop() não somente remove o último elemento, mas também o retorna.
print('\nPodemos remover o último elemento de uma lista: pop().')
print(lista5)
lista5.pop()
print(lista5)

# Podemos remover um elemento pelo índice.
# Obs: Os elementos a direta do índice serão deslocados para a esquerda.
# Obs: Se não houver elemento no índice informado, teremos o erro IndexError.
print('Podemos remover o elemtno pelo seu índice')
lista5.pop(2)
print(lista5)


# Podemos remover todos os elementos (zerar a lista)
print('\nPodemos remover todos os elementos da lista (zerar a lista): clear()')
print(lista5)
lista5.clear()
print(lista5)


# Podemos facilmente repetir elementos em uma lista
print('\nPodemos facilmente repetir elementos em uma lista. Ex: lista = lista * 3')
nova = [1, 2, 3]
print(nova)
nova = nova * 3
print(nova)


# Podemos facilmente converter uma string para uma lista.
print('\nPodemos facilmente converter uma string para uma lista: split()')
print('Exemplo 1')
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
print(curso)
# Por padrão o split() separa os elementos da lista pelo espaço entre elas.

print('Exemplo 2: usando separador')
curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',')
print(curso)


# Convertendo uma lista numa string: join().
print('\nConvertendo uma lista numa string: join().')
lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma string.
curso = ' '.join(lista6)
print(curso)

curso = ':separador que quiser:'.join(lista6)
print(curso)

"""
# Iterando sobre listas.
lista1 = [1, 3, 10, 35, 7]
print("\nIterando sobre listas.\nExemplo 1: Utilizando 'for'")
print(lista1)
soma = 0
for elemento in lista1:
    print(elemento)
    soma = soma + elemento
print(f'O toral da soma da lista é: {soma}')

print(f"\nExemplo 2: Utilizando 'while'")
carrinho = []
produto = ''

while produto != 'sair':
    print("Adicione um produto na lista ou digite 'sair' para sair: ")
    produto = input()
    if produto != 'sair':
        carrinho.append(produto)

for produto in carrinho:
    print(produto)

"""

# Utilizando variáveis em listas
print('\nUtilizando variáveis em listas.')
numeros = [1, 2, 3, 4, 5]
print(numeros)

num1 = 1
num2 = 2
num3 = 3
num4 = 4
num5 = 5
numeros = [num1, num2, num3, num4, num5]
print(numeros)


# Fazemos acesso aos elementos de forma indexada.
print('\nFazemos acesso aos elementos de forma indexada.')
#           0         1         2         3
cores = ['verde', 'amarelo', 'azul', 'branco']
print(cores[0])  # verde -- index [0]
print(cores[1])  # amarelo -- index [1]
print(cores[2])  # azul -- index [2]
print(cores[3])  # branco -- index [3]

# Fazer acesso aos elementos de forma indexada inversa.
print('Fazer acesso aos elementos de forma indexada inversa.')
print(cores[-1])  # branco
print(cores[-4])  # verde


# Gerar índice em um for.
print('\nGerar índice em um for.')
for indice, cor in enumerate(cores):
    print(indice, cor)


# Outros métodos não tão importantes mas também úteis.
print('\nOutros métodos não tão importantes mas também úteis.')

# Encontrar o índice de um elemento na lista.
print('\nEncontrar o índice de um elemento na lista: .index()')
numeros = [5, 6, 7, 8, 5, 9, 10]
print(numeros)
print(f'O número 6 está no índice {numeros.index(6)}.')
print(f'O número 9 está no índice {numeros.index(9)}.')

# Obs: Caso não tenha esta elemento na lista, será apresentado erro. ValueError

print(f'Com elementos repetidos, retorna o índice do primeiro encontrado, '
      f'logo o número 5 terá o índice {numeros.index(5)}.')


# Podemos fazer busca dentro de um range, ou seja, qual índice começar a buscar.
print("Buscando a partir do índice 1 'numeros.index(5, 1)'. Dessa maneira, iniciando a busca pelo índice 1,"
      f"o índice do número 5 será {numeros.index(5, 1)}.")
print("Podemos fazer busca dentro de um range início/fim. Buscar o valor 8 entre os índices 3 e 6"
      f" 'numeros.index(8, 3, 6): {numeros.index(8, 3, 6)}")


# Revisão slicing --- lista[início:fim:passo]

# Trabalhando com slice de lista com o parâmetro 'início'.
print(f"\nTrabalhando com slice de lista com o parâmetro 'início'.")
lista = [1, 2, 3, 4]
print(lista)
print("Iniciando no índice 1 e pegando todos os elementos restantes: 'print(lista[1:])'")
print(lista[1:])

print(f"\nTrabalhando com slice de lista com o parâmetro 'fim'.")
print(lista)
print("Começa em 0, e pega até o índice 2 -1: 'print(lista[:2])'")
print(lista[:2])
print("Começa em 0, e pega até o índice 4 -1: 'print(lista[:4])'")
print(lista[:4])

print(f"\nTrabalhando com slice de lista com o parâmetro 'início:fim'.")
print(lista)
print("Começa em 1, e pega até o índice 3 -1: 'print(lista[1:3])'")
print(lista[1:3])

print(f"\nTrabalhando com slice de lista com o parâmetro 'passo'.")
print(lista)
print("Começa em 1, vai até o final, de 2 em 2: 'print(lista[1::2])'")
print(lista[1::2])

print("Começa em 0, vai até o final, de 2 em 2: 'print(lista[::2])'")
print(lista[::2])

print("Se usar o passo negativo, a lista fica invertida: 'print(lista[1::-1])'")
print(lista[::-1])


# Soma*, Valor Máximo*, Valor Mínimo*, Tamanho: Obs: *Se os valores forem todos inteiros ou reais
print('\nSoma*, Valor Máximo*, Valor Mínimo*, Tamanho: Obs: *Se os valores forem todos inteiros ou reais')

lista = [1, 2, 3, 4, 5, 6]
print(lista)
print("Soma: print(sum(lista))")
print(sum(lista))
print("Valor Máximo: print(max(lista))")
print(max(lista))
print("Valor Mínimo: print(min(lista))")
print(min(lista))
print("Tamanho da Lista: print(len(lista))")
print(len(lista))


print('\nTransformar uma lista em tupla: tuple().')
print(lista)
print(type(lista))

tupla = tuple(lista)
print(tupla)
print(type(tupla))


# Desempacotando listas
print('\nDesempacotando listas. Ex: num1, num2, num3 = lista')
lista = [1, 2, 3]
print(f'lista = {lista}')
num1, num2, num3 = lista

print(f'num1 = {num1}')
print(f'num2 = {num2}')
print(f'num3 = {num3}')

# Obs: Se tivermos um número dioferente de elementos na lista ou variáveis para
# receber os dados, teremos ValueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)
print('\nCopiando uma lista para outra (Shallow Copy e Deep Copy)')

print('\nForma 1 -- Deep Copy')

lista = [1, 2, 3]
print(f'lista: {lista}')

nova = lista.copy()
print(f'nova depois do copy(lista): {nova}')

nova.append(4)
print(f'lista depois do appen(4): {lista}')
print(f'nova depois do appen(4): {nova}')

# Ao utilizarmos lista.copy(), copiamos os dados da lista para uma nova lista, mas elas
# ficaram  totalmente independentes, ou seja, mofificando uma lista não afeta a outra.
# Isso em Python é chamado de Deep Copy (Cópia Profunda).

print('\nForma 2 -- Shallow Copy')

lista = [1, 2, 3]
print(f'lista: {lista}')

nova = lista
print(f'nova depois de: nova = lista: {nova}')

nova.append(4)
print(f'lista depois do append(4): {lista}')
print(f'nova depois do appen(4): {nova}')

# Veja que utilizamos a copia via atribuição e copiamos os dados da lista para a nova lista, mas
# após realizar modificação em uma das listas, essa modificação se refletiu em ambas as listas.
# Isso em Python é chamado Shallow Copy (cópia rasa).
