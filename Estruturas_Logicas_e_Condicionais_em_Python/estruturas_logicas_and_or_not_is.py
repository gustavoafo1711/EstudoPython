"""
Estruturas Lógicas (and, or, not, is)

Operadores unários:
    - not
Operadores binários:
    - and, or, is

Regras de funcionamento:
Para o 'and', ambos os valores precisam ser True.
Para o 'or', umm ou outro valor precisa ser True.
para o 'not', o valor do booleano é invertido, ou seja, se for True vira False, se for False vira True.
"""
ativo = False
logado = True


"""
if ativo and logado:
    print('Bem-vindo usuário.')
else:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail.')
"""

"""
# Se não estiver ativo
if not ativo:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail.')
else:
    print('Bem-vindo usuário')


print(not True)
"""

if ativo is False:
    print('Você precisa ativar sua conta. Por favor cheque seu e-mail.')
else:
    print('Bem-vindo usuário')