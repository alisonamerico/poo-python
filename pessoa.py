"""
Vamos criar uma classe que representa uma entidade do tipo Pessoa!

Ela deve ter os seguintes campos:

Nome como String;
Idade como Inteiro;
Altura como Decimal.
Também deve ter métodos para:

Dizer “Olá”;
Cozinhar;
Andar.
Utilizando POO e Python, podemos modelar a entidade Pessoa da seguinte forma:
"""


class Pessoa:
    def __init__(self, nome: str, idade: int, altura: float):
        self.nome = nome
        self.idade = idade
        self.altura = altura

    def dizer_ola(self):
        print(
            f'Olá nome é {self.nome}. Tenho {self.idade}'
            f' anos e minha altura é {self.altura}'
        )

    def cozinhar(self, receita: str):
        print(f'Estou cozinhando um(a): {receita}')

    def andar(self, distancia: float):
        print(
            f'Saí para andar. Volto quando tiver completado\
 {distancia} metros.'
        )


# Instancia um objeto da Classe "Pessoa"
pessoa = Pessoa(nome='João', idade=25, altura=1.88)

# Chama os métodos de "Pessoa"
pessoa.dizer_ola()
pessoa.cozinhar('Spaghetti')
pessoa.andar(750.5)


"""
Agora vamos explicar “tintim por tintim”:

Temos a definição da Classe na primeira linha com class Pessoa. 
Isso diz ao Python que vamos criar a definição de uma nova classe.

Em seguida, temos o método __init__. Ele é muito importante e é chamado de Construtor. 
Ele é chamado ao se instanciar objetos e é nele que geralmente setamos os atributos do objeto.

Em seguida temos a definição dos métodos dizer_ola(), cozinhar() e andar().

Perceba que no método dizer_ola() referenciamos os atributos do próprio objeto
 com o argumento self: self.nome, self.idade e self.altura.


Se lembra do Construtor?

Então, ele entrou em ação na linha 2 do código acima!

Quando escrevemos pessoa = Pessoa(), chamamos o método __init__ da classe Pessoa, 
passando os parâmetros nome, idade e altura.

A saída dessas linhas de código será:

Olá, meu nome é João. Tenho 25 anos e minha altura é 1.88m.
Estou cozinhando um(a): Spaghetti
Saí para andar. Volto quando completar 750.5 metros
"""
