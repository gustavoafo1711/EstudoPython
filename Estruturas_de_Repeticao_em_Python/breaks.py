"""
Saindo de loops com breaks

Funciona da mesma forma que nas linguagens C ou Java.

Utilizamos o break para sair de loops de maneira projetada.


"""

print('Exemplo 1 - utilizando for')

for numero in range(1, 11):
    if numero == 6:
        break
    else:
        print(numero)
print('Sai do loop for')


print('\nExemplo 2 - utilizando while')

while True:
    comando = input("Digite 'sair' para sair: ")
    if comando == 'sair':
        break
print('Sai do loop while')
