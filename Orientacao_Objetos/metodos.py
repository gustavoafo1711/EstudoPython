"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto, ou seja, as ações
que este objeto pode realizar no seu sistema.

Em Python, dividimos os métodos em 2 grupos, métodos de instância e métodos de classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua
função é construir o objeto a partir da classe.

# Os métodos dunder em Python são chamados de métodos mágicos.

ATENÇÃO: Por mais que possamos criar nossas próprias funções utilizando dunder, não é aconselhado. Python
possui vários métodos com esta forma de nomenclatura e pode ser que mudemos o comporamento dessas funções
mágicas internas da linguagem. Então evite o máximo, de preferência nunca o faça.


p1 = Produto('Playstation', 'video game', 2000)

print(p1.desconto(50))



user1 = Usuario('Angelina', 'Jolie', 'angelina@gmail.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '789456')

print(user1.nome_completo())
print(Usuario.nome_completo(user1))
print(user2.nome_completo())

print(f'Senha: {user1._Usuario__senha}')  #Acesso de forma errada de um atributo de classe
print(f'Senha: {user2._Usuario__senha}')  #Acesso de forma errada de um atributo de classe

# Instalar criptografia: pip install passlib


nome = input('Informe o nome: ')
sobrenome = input('Informe o sobrenome: ')
email = input('Informe o email: ')
senha = input('Informe o senha: ')
confirmasenha = input('Confirme a senha: ')

if senha == confirmasenha:
    user = Usuario(nome, sobrenome, email, senha)
else:
    print('Senha não confere.')
    exit(42)

print('Usuário criado com sucesso!')

senha = input('Informe a senha para acesso: ')

if user.checa_senha(senha):
    print('Acesso permitido')
else:
    print('Acesso negado')
    exit(42)

print(f'Senha User Criptografada: {user._Usuario__senha}')

# Métodos de Classe em Python são conhecidos como métodos estáticos em outras linguagens


# Métodos de Classe

user1 = Usuario('Felicity', 'Jones', 'felicity@gmail.com', '12345')

Usuario.conta_usuario()  # Forma correta
user1.conta_usuario()  # Possível, mas incorreta

Usuario.ver()
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.__numero = ContaCorrente.contador + 1
        self.__limite = limite
        self.__saldo = saldo
        ContaCorrente.contador = self.__numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.__id = Produto.contador + 1
        self.__nome = nome
        self.__descricao = descricao
        self.__valor = valor
        Produto.contador = self.__id

    def desconto(self, pocentagem):
        """Retorna o valor do produto com o desconto"""
        return (self.__valor * (100 - pocentagem)) / 100



from passlib.hash import pbkdf2_sha256 as cryp


class Usuario:

    contador = 0

    @classmethod
    def conta_usuario(cls):
        print(f'Classe: {cls}')
        print(f'Temos {cls.contador} usuário(s) no sistema')

    @classmethod
    def ver(cls):
        print('Acesso a Classe')

    @staticmethod
    def definicao():
        return 'URX344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        self.__nome = nome
        self.__sobrenome = sobrenome
        self.__email = email
        self.__senha = cryp.hash(senha, rounds=20000, salt_size=16)
        Usuario.contador = self.__id
        print(f'Usuario criado: {self.__gera_usuario()}')

    def nome_completo(self):
        return f'{self.__nome} {self.__sobrenome}'

    def checa_senha(self, senha):
        if cryp.verify(senha, self.__senha):
            return True
        return False

    def __gera_usuario(self):
        return self.__email.split('@')[0]


# Metodo Estatico

print(Usuario.contador)

print(Usuario.definicao())

user = Usuario('Joao', 'de Deus', 'usuario@gmail.com', '123456')
print(user.contador)
print(user.definicao())

