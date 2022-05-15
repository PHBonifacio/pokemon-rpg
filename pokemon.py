class Pokemon:

    def __init__(self, tipo, especie, level = 1, nome = None) -> None:
        self.tipo = tipo
        self.especie = especie
        self.level = level

        if nome:
            self.nome = nome
        else:
            self.nome = especie

    def __str__(self) -> str:
        return "{} ({}) Level : {}".format(self.especie, self.tipo, self.level)

    def attack(self, pokemon) -> None:
        print("{} attacked {}".format(self, pokemon))

class EletricPokemon(Pokemon):
    def __init__(self, especie, level=1, nome= None) -> None:
        super().__init__("eletric", especie, level, nome)

    def attack(self, pokemon) -> None:
        print("{} used thundershock on {}".format(self, pokemon))

class FirePokemon(Pokemon):
    def __init__(self, tipo, especie, level=1, nome=None) -> None:
        super().__init__("fire", especie, level, nome)

    def attack(self, pokemon) -> None:
        print("{} used fire ball on {}".format(self, pokemon))
