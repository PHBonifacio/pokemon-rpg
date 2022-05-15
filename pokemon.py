import random
class Pokemon:

    def __init__(self, tipo, specie, level, name = None) -> None:
        self.tipo = tipo
        self.specie = specie
        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if name:
            self.name = name
        else:
            self.name = specie

        self.attackpoints = random.randint(0, self.level * 5)
        self.defensepoints = random.randint(0, self.level * 3)
        self.lifepoints = random.randint(0, self.level * 10)

    def __str__(self) -> str:
        return "{} ({}) Level : {}".format(self.specie, self.tipo, self.level)

    def attack(self, pokemon) -> bool:
        attack = self.attackpoints * random.random()
        defense = pokemon.defensepoints * random.random()
        damage = attack - defense
        if damage > 0:
            pokemon.lifepoints -= damage
            if pokemon.lifepoints < 0:
                pokemon.lifepoints = 0
        else:
            damage = 0

        print("{} made {} damage points".format(self.name, damage))
        print("{} current {} life points\n".format(pokemon.name, pokemon.lifepoints))
        return True if pokemon.lifepoints <= 0 else False
    
    def evolve(self):
        self.level += 1
        self.attackpoints = random.randint(round(self.attackpoints), self.level * 5)
        self.defensepoints = random.randint(round(self.defensepoints), self.level * 3)
        self.lifepoints = random.randint(round(self.lifepoints), self.level * 10)

        print("{} evolved! Attack: {} Defense: {} Life: {} Level: {}\n".format(self.name, self.attackpoints, self.defensepoints, self.lifepoints, self.level))


class EletricPokemon(Pokemon):
    SPECIES = ["Pikachu", "Raichu", "Electabuzz", 'Regieleki']
    def __init__(self, specie = None, level= None, name= None) -> None:
        if not specie:
            specie = random.choice(self.SPECIES)

        super().__init__("Eletric", specie, level, name)

    def attack(self, pokemon) -> None:
        print("{} used thundershock on {}".format(self, pokemon))
        return super().attack(pokemon)

class FirePokemon(Pokemon):
    SPECIES = ["Charmander", "Flareon", "Charizard", 'Fuecoco']
    def __init__(self, specie = None, level= None, name= None) -> None:
        if not specie:
            specie = random.choice(self.SPECIES)

        super().__init__("Fire", specie, level, name)

    def attack(self, pokemon) -> None:
        print("{} used fire ball on {}".format(self, pokemon))
        return super().attack(pokemon)

class WaterPokemon(Pokemon):
    SPECIES = ["Blastoise", "Magikarp", "Quaxly", 'Lapras']
    def __init__(self, specie = None, level= None, name= None) -> None:
        if not specie:
            specie = random.choice(self.SPECIES)

        super().__init__("Water", specie, level, name)
    
    def attack(self, pokemon) -> bool:
        print("{} used water ball on {}".format(self, pokemon))
        return super().attack(pokemon)
