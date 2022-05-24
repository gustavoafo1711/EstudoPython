"""
Documentando funções com docstrings

Obs> Podemos ter acesso a documentação de uma função em python, utilizando
o propriedade especial __doc__

Podemos ainda fazer acesso a documentação com o função help()

"""


def diz_oi():
    """Uma função simples que retorna a string 'Oi!'"""
    return 'Oi!'


def exponencial(numero, potencia=2):
    """
    Função que retorna por padrão o quadrado de 'numero' ou 'numero' a 'potenciaa' informada'
    :param numero: Número que desejamos elevar ao exponencial
    :param potencia: Pôtenci que queremos gerar o exponencial. Por padrão 2.
    :return: Retiorna o exponencial de 'numero'   por 'potencia'.
    """

    return numero ** potencia



