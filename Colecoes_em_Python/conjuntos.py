"""
Conjuntos

- Conjuntos em qualquer linguagem de programação, estamos fazendo referência à Teoria dos Conjuntos
da matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na matemática:
- Sets (conjuntos) não possuem valores duplicados;
- Sets (conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjunto não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos mas não nos importamos
com a ordenação deles. Quando não precisamos se preocupar com chaves, valores e itens duplicados.

Os conjuntos (sets) são referenciados com chaves {}

Diferença entre conjuntos (set) e mapas(dicionáios) em Python.
    - Um dicionário tem chave/valor;
    - Um conjunto tem apenas valor;

"""


"""
# Definindo um conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repetidos

print(s)
print(type(s))

# Obs: Ao criar um conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar erros e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))


# Podemos verificar se determinado elemento está contido no conjunto
print('\nPodemos verificar se determinado elemento está contido no conjunto')
if 3 in s:
    print('Tem o 3')
else:
    print('Não tem o 3')


# Importante lembrar que além de não termos valores duplicados, não temos ordem
lista = [99, 2, 2, 34, 34, 23, 12, 1, 44, 5]
print(f'Lista: {lista}')

tupla = 99, 2, 2, 34, 34, 23, 12, 1, 44, 5
print(f'Tupla: {tupla}')

dicionario = {}.fromkeys([99, 2, 2, 34, 34, 23, 12, 1, 44, 5], 'dict')
print(f'Dicionário: {dicionario}')

conjunto = {99, 2, 2, 34, 34, 23, 12, 1, 44, 5}
print(f'Conjunto: {conjunto}')


# Assim como todo outro conjunto Python, podemos colocar tipos de dados misturados em Sets

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente
for valor in s:
    print(valor)
    
    
# Usos interessantes com sets

# Imagine que fizemos um formulário de cadastro de visitantes em uma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiaba', 'Campo Grande', 'São Paulo', 'Cuiaba']

print(cidades)
print(len(cidades))

# Agora precisamos saber quantas cidade distintas temos.

print(len(set(cidades)))


# Adicionando elementos em um conjunto.
s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro, simplesmente é ignorado e não adiciona.
print(s)


# Remover elementos em um conjunto.
s = {1, 2, 3}
print(s)

# Forma 1
s.remove(3)  # NÃO é índice! Informamos o valor a ser removido.
print(s)

# OBS: Caso o valor não seja encontrado, será gerado o erro KeyError. Nenhum valor é retornado

# Forma 2
s.discard(2)
s.discard(22)
print(s)

# OBS: Se o valor não for encontrado, nenhum erro é gerado

# Copiando um conjunto para outro...

s = {1, 2, 3}
print(s)

# Forma 1 - Deep Copy

novo = s.copy()
print(novo)

novo.add(4)
print(novo)
print(s)

# Forma 2 - Shallow copy

novo = s
novo.add(4)

print(novo)
print(s)

# Podemos remover todos os elementos de um conjunto
s.clear()
print(s)


# Métodos Matemáticos de Conjuntos

# Imagine que temos dois conjuntos: Um contendo estudantes do curso Pyton e um
# contendo estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patrícia', 'Ellen', 'Pedro', 'Julia', 'Guilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patrícia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando Union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# Forma 2 - Utilizando o caractere pipe |

unicos2 = estudantes_java | estudantes_python
print(unicos2)


# Gerar um conjunto de estudantes que estão em ambos os cursos.

# Forma 1 - Utilizando intersection
ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizando o &
ambos2 = estudantes_python & estudantes_java
print(ambos2)


# Gerar um conjunto de estudantes que não estão no outro curso
so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

"""

# Soma*, Valor_Máximo*, Valor_Mínimo, Tamanho

# *Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
