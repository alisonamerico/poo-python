# poo-python

## PROGRAMAÇÃO ORIENTADA A OBJETOS NO PYTHON: INTRODUÇÃO

A Programação Orientada a Objetos (POO) é um paradigma de programação baseado no conceito de Classes e Objetos.

**Classes** podem conter dados e código:

- **Dados** na forma de campos (também chamamos de atributos ou propriedades); e
- **Código**, na forma de procedimentos (frequentemente conhecido como métodos).

Uma importante característica dos objetos é que seus próprios métodos podem acessar e frequentemente modificar seus campos de dados: objetos mantém uma referência para si mesmo, o atributo **self** no Python.

Python já nasceu sendo uma linguagem de programação multi-paradigma, isto é: é possível programar de maneira Imperativa, Funcional e também Orientada a Objectos.

Conceitos muito importante da Programação Orientada a Objetos que todo programador Python DEVE dominar:

```bash
- [x] Classes;
- [x] Objetos;
- [x] Herança;
- [x] Polimorfismo;
- [x] Encapsulamento.
```

---

### Classes, Objetos, Métodos e Atributos

Esses conceitos são os pilares da Programação Orientada a Objetos então é muito importante que você os DOMINE:

- As **Classes** são tipos de dados definidos pelo desenvolvedor que atuam como um modelo para objetos. Pra não esquecer mais: Classes são fôrmas de bolo e bolos são objetos :wink:

- **Objetos** são instâncias de uma Classe. Objetos podem modelar entidades do mundo real (Carro, Pessoa, Usuário) ou entidades abstratas (Temperatura, Umidade, Medição, Configuração).

- **Métodos** são funções definidas dentro de uma classe que descreve os comportamentos de um objeto. Em Python, o primeiro parâmetro dos métodos é sempre uma referência ao próprio objeto.

- Os **Atributos** são definidos na Classe e representam o estado de um objeto. Os objetos terão dados armazenados nos campos de atributos. Também existe o conceito de atributos de classe, mas veremos isso mais pra frente.

---

### Princípios Básicos de POO

A programação orientada a objetos é baseada nos seguintes princípios:

**Encapsulamento**
Usamos esse princípio para juntar, ou encapsular, dados e comportamentos relacionados em entidades únicas, que chamamos de objetos.

Por exemplo, se quisermos modelar uma entidade do mundo real, por exemplo Computador.

Encapsular é agregar todos os atributos e comportamentos referentes à essa Entidade dentro de sua Classe.

Dessa forma, o mundo exterior não precisa saber como um Computador liga e desliga, ou como ele realiza cálculos matemáticos!

Basta instanciar um objeto da Classe Computador, e utilizá-lo! :wink:

O princípio do Encapsulamento também afirma que informações importantes devem ser contidas dentro do objeto de maneira privada e apenas informações selecionadas devem ser expostas publicamente.

A implementação e o estado de cada objeto são mantidos de forma privada dentro da definição da Classe.

Outros objetos não têm acesso a esta classe ou autoridade para fazer alterações.

Eles só podem chamar uma lista de funções ou métodos públicos.

Essa característica de ocultação de dados fornece maior segurança ao programa e evita corrupção de dados não intencional.

---

**Abstração**

Pense em um Tocador de DVD.

Ele tem uma placa lógica bastante complexa com diversos circuitos, transistores, capacitores e etc do lado de dentro e apenas alguns botões do lado de fora.

Você apenas clica no botão de “Play” e não se importa com o que acontece lá dentro: o tocador apenas… Toca.

Ou seja, a complexidade foi “escondida” de você: isto é Abstração na prática!

O Tocador de DVD abstraiu toda a lógica de como tocar o DVD, expondo apenas botões de controle para o usuário.

O mesmo se aplica à Classes e Objetos: nós podemos esconder atributos e métodos do mundo exterior. E isso nos traz alguns benefícios!

Primeiro, a interface para utilização desses objetos é muito mais simples, basta saber quais “botões” utilizar.

Também reduz o que chamamos de “Impacto da mudança”, isto é: ao se alterar as propriedades internas da classes, nada será alterado no mundo exterior, já que a interface já foi definida e deve ser respeitada.

---

**Herança**
Herança é a característica da POO que possibilita a reutilização de código comum em uma relação de hierarquia entre Classes.

Vamos utilizar a entidade Carro como exemplo. :car:

Agora imagine uma Caminhonete, um Caminhão e uma Moto.

Todos eles são Automóveis, correto? Todos possuem característica semelhantes, não é mesmo?

Podemos pensar que Automóveis aceleram, freiam, possuem mecanismo de acionamento de faróis, entre outros.

---

**Polimorfismo**
Quando utilizamos Herança, teremos Classes filhas utilizando código comum da Classe acima, ou Classe pai.

Ou seja, as Classes vão compartilhar atributos e comportamentos (herdados da Classe acima).

Assim, Objetos de Classes diferentes, terão métodos e atributos compartilhados que podem ter implementações diferentes, ou seja, um método pode possuir várias formas e atributos podem adquirir valores diferentes.

Daí o nome: Poli (muitas) morfismo (formas).

Para entendermos melhor, vamos utilizar novamente o exemplo da entidade Carro que herda de Automóvel.

Suponha agora que Automóvel possua a definição do método acelerar().

Por conta do conceito de Polimorfismo, objetos da Classe Moto terão uma implementação do método acelerar() que será diferente da implementação desse métodos em instâncias da Classe Carro!

---

**Programação Orientada a Objetos no Python**

Python possui palavras reservadas (keywords) para criarmos Classes e Objetos.

:point_right: Primeiro, temos a keyword _class_ que utilizamos para criar uma classe.

:point_right: Também temos a keyword _self_, utilizada para guardar a referência ao próprio objeto.

---

Conteúdo retirado da [Python Academy](https://pythonacademy.com.br/blog/introducao-a-programacao-orientada-a-objetos-no-python)
