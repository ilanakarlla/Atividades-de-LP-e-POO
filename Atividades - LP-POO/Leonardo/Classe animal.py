class Animal:
    def __init__(self, altura, especie, idade, nome, peso):
        self.andando = False
        self.comendo = False
        self.dormindo = False
        self.altura = altura
        self.idade = idade
        self.especie = especie
        self.nome = nome
        self.peso = peso

    def andar(self, destino):
        self.dormindo = False
        self.andando = True
        print(f"{self.nome} está andando até {destino}.")

    def comer(self, alimento):
        self.comendo = True
        self.dormindo = False
        print(f"{self.nome} está comendo {alimento}.")

    def dormir(self, onde):
        self.andando = False
        self.dormindo = True
        self.comendo = False
        print(f"{self.nome} está dormindo em {onde}.")


class Cachorro(Animal):
    def __init__(self, altura, cor, idade, nome, peso, raca, tutor):
        super().__init__(altura, "cão", idade, nome, peso)
        self.cor = cor
        self.raca = raca
        self.tutor = tutor

    def latir(self):
        print(f"{self.nome} latiu.")

    def abanar(self):
        print(f'{self.nome} abanou o rabo')


Wingard = Cachorro("1,34", "azul", "159", "Wingard", "201", "etéreo", "Rei das Dominações")
Wingard.comer("universos")
Pheephobaltazar = Cachorro("2,45", "Arco-íris", "380", "Pheephobaltazar", "1034", "etéreo", "Deus")
Pheephobaltazar.latir()