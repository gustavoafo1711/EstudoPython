"""
POO - Atributos

Atributos -> representam as características do objeto. Ou seja, pelos atributos nós conseguimos
representar computacionalmente os estados de um objeto.

Em Python, dividimos os atríbutos em 3 grupos:
    - Atributos de instância;
    - Atributos de classe;
    - Atributos dinânicos;


# Atributos de instância: São atributos declarados dentro do método construtor.

obs: Método construtor, é um método especial utilizado para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos assim:

public class Lampada(){
    private int voltagem;              |
    private String cor;                |-> Declarando atributos Java
    private Boolean ligada = false;    |

    public Lampada(int voltagem, String cor){   |
        this.voltagem = voltagem;               |-> Método contrutor Java
        this.cor = cor;                         |
    }

    public int getVoltagem(){
        return this.voltagem;
    }
}



# obs: lembre-se que isso é apenas uma convenção, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe


# Exemplo


user = Acesso('user@gmail.com', '123456')

print(f'Usuário: {user.email}')
# print(f'Senha: {user.__senha}')  # AttributeError

print(f'Usuário: {user._Acesso__senha}')  # Não recomendado acessar dessa maneira
user.mostra_senha()



# O que significa atributos de instância?

# Significa que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão
# estes atributos.


user1 = Acesso('user1@gamail.com', '123456')
user2 = Acesso('user2@gamail.com', '987654')

user1.mostra_email()
user2.mostra_email()



# Atributos de Classe


# Atributos de classe são atributos que são declarados diretamente na classe,
# ou seja, fora do construtor. Geralmente já inicializamos um valor, e este
# valor é compartilhado entre todas as instâncias da classe, ou seja, ao invés
# de cada intância ter seus próprios valores como é o caso dos atributos de
# instância, com os atributos de classe todas as instâncias terão o mesmo valor
# para este atributo.

# Refatorar a classe Produto


class Produto:

    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)
        Produto.contador = self.id


p1 = Produto('Playstation', 'Video game', 2500)
p2 = Produto('Atari', 'Video game', 1345)

print(p1.valor)
print(p2.valor)

# obs: não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe
print(f'Acessando imposto sem criar instância: acesso correto atributo de classe (Produto.imposto) {Produto.imposto}')
print(f'Acessando imposto com instância: acesso incorreto (p1.imposto) {p1.imposto}')


print(f'\nid do p1: {p1.id}')
print(f'id do p2: {p2.id}')

"""


# Classes com atributos de Instância Públicos
class Lampada:

    def __init__(self, voltagem, cor):
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome  # self(objeto Usuario) no atributo nome, vai receber nome
        self.email = email
        self.senha = senha


# Classes com atributos de Instância Privado

class Acesso:

    def __init__(self, email, senha):
        self.email = email
        self.__senha = senha

    def mostra_senha(self):
        print(self.__senha)

    def mostra_email(self):
        print(self.email)


# Atributos Dinâmicos -> um atributo de instância que pode ser criado em tempo de execução

# obs: o atributo dinâmico será exclusivo da instÂncia que o criou.

p1 = Produto('Playstation', 'Video Game', 2500)
p2 = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução
p2.peso = '5Kg'  # na classe Produto não exite peso

print(f'Produto: {p2.nome}\nDescrição: {p2.descricao}\nValor: {p2.valor}\nPeso: {p2.peso}')

# print(f'Produto: {p1.nome}\nDescrição: {p1.descricao}\nValor: {p1.valor}\nPeso: {p1.peso}') #AttributeError

# Deletando atributos

print('\n')
print(p1.__dict__)
print(p2.__dict__)

del p2.peso
print(p1.__dict__)
print(p2.__dict__)

del p2.valor
print(p1.__dict__)
print(p2.__dict__)

del p2.descricao
print(p1.__dict__)
print(p2.__dict__)