import random
class Pokemon:

    def __init__(self, tipo, specie, level, nome = None) -> None:
        self.tipo = tipo
        self.specie = specie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = specie

    def __str__(self) -> str:
        return "{} ({}) Level : {}".format(self.specie, self.tipo, self.level)

    def attack(self, pokemon) -> None:
        print("{} attacked {}".format(self, pokemon))

class EletricPokemon(Pokemon):
    SPECIES = ["Pikachu", "Raichu", "Electabuzz", 'Regieleki']
    def __init__(self, specie = None, level= None, nome= None) -> None:
        if not specie:
            specie = random.choice(self.SPECIES)

        super().__init__("Eletric", specie, level, nome)

    def attack(self, pokemon) -> None:
        print("{} used thundershock on {}".format(self, pokemon))

class FirePokemon(Pokemon):
    SPECIES = ["Charmander", "Flareon", "Charizard", 'Fuecoco']
    def __init__(self, specie = None, level= None, nome= None) -> None:
        if not specie:
            specie = random.choice(self.SPECIES)

        super().__init__("Fire", specie, level, nome)

    def attack(self, pokemon) -> None:
        print("{} used fire ball on {}".format(self, pokemon))

class WaterPokemon(Pokemon):
    SPECIES = ["Blastoise", "Magikarp", "Quaxly", 'Lapras']
    def __init__(self, specie = None, level= None, nome= None) -> None:
        if not specie:
            specie = random.choice(self.SPECIES)

        super().__init__("Water", specie, level, nome)