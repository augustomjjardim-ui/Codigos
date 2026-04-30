# Programação Orientada a Objetos com Python
class Personagem:
    def __init__(self, nome, vida):
        self.__nome = nome
        self.__vida = vida

    @property
    def nome(self):
        return self.__nome
    
    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    @property
    def vida(self):
        return self.__vida
    
    @vida.setter
    def vida(self, vida):
        self.__vida = vida

    def atacar(self, personagem):
        personagem.vida -= 10
        print(f'{self.nome} atacou {personagem.nome} e {personagem.nome} perdeu 10 pontos de vida e agora esta com {personagem.vida}')


class Mago(Personagem):
    def __init__ (self, nome, vida):
        super().__init__(nome, vida)

    # polimorfismo
    def atacar(self, personagem):
        personagem.vida -= 20
        print(f'{self.nome} atacou {personagem.nome} e {personagem.nome} perdeu 20 pontos de vida e agora esta com {personagem.vida}')

    def cura(self, personagem):
        personagem.vida += 15
        print(f'{self.nome} usou o poder de cura em {personagem.nome}, agora ele tem {personagem.vida}')

frodo = Personagem('Frodo', 100)
gandof = Mago('Gandof', 100)

print(f'Nome: {frodo.nome}')
print(f'Vida: {frodo.vida}')
print(f'Nome: {gandof.nome}')
print(f'Vida: {gandof.vida}')

frodo.atacar(gandof)
gandof.cura(gandof)
gandof.atacar(frodo)