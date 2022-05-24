"""
Dicionários

Obs: Em algumas linguagnes de programação, os dicionários Python são conhecidos
por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

Obs: Sobre dicionários:
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave e valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

"""
# Criação de dicionários
print('Criação de Dicionários.')

# Forma 1 (Mais comum)
print("\nForma 1 (mais comum)\npaises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}")
paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))
print(paises['py'])

# Forma 2 (menos comum)
print("\nForma2 (menos comum)\npaises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')")
paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

# Acessando elementos
print('\nAcessando elementos')

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla
print("\nForma 1 - Acessando via chave, da mesma forma que lista/tupla. Ex: print(paises['eua'])")

print(paises['br'])
print(paises['eua'])

# Obs: Caso tentarmos fazer um aceso utilizando uma chave que não existe, teremos o erro KeyError

# Forma 2 - Acessando via get - Recomendado
print("\nForma 2 - Acessando via get - Recomendado. Ex: print(paises.get('br'))")

print(paises.get('br'))
print(paises.get('ru'))


# Podemos definir um valor padrão para caso não encontremos o objeto comm a chave informada.
print("\npodemos definir um valor padrão para caso não encontremos o objeto comm a chave informada."
      " EX: print(paises.get('ru', 'País não encontrado'))")
print(paises.get('ru', 'País não encontrado'))
