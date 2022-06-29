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


# obs: lembre-se que isso é apenas uma convenção, a linguagem Python não
# vai impedir que façamos acesso aos atributos sinalizados como privados fora da classe


# Exemplo


user = Acesso('user@gmail.com', '123456')

print(f'Usuário: {user.email}')
# print(f'Senha: {user.__senha}')  # AttributeError

print(f'Usuário: {user._Acesso__senha}')  # Não recomendado acessar dessa maneira
user.mostra_senha()


