import random
from secrets import choice
from tkinter import PROJECTING
from pokemon import *

class People:
    NAMESLIST = ["Logan Ruiz", "Rayan Donaldson", "Grady Richmond", "Hector Benitez", "Korbin Allen", "Avah Mckee", "Alejandra Davis", "Kyla Rodriguez", "Priscilla Cameron", 
            "Angela Lawson", "Maximillian Stafford", "Jamison Mccarthy", "Ellen Yates", "Tatum Bernard", "Pamela Solis", "Maddison Matthews", "Angela Randolph", "Avery Ramirez", 
            "Conor Roman", "Reagan Pittman", "Iris Bass", "Uriel Mahoney", "Jadiel Colon", "Jamya Wilkinson", "Derrick Werner", "Alexia Oliver", "Izaiah Shannon", "Kaitlyn Long", 
            "Quinn Burnett", "Brogan Key", "Landon Sherman", "Andreas Reid", "Messiah Mcpherson", "Saniya Mosley", "Bridget Salazar", "Zaniyah Trujillo", "Rodrigo Kirby", 
            "Emilio Wilson", "Branden Pope", "Delilah Lawrence", "Briley Callahan", "Kaya Kane", "Micah Stephens", "Scott Jefferson", "Asher Frey", "Deanna Beard", "Hope Hendrix", 
            "Monique Ford", "Landen Simmons", "Fabian Perry", "Mayra Foster", "Sherlyn Pittman", "Braydon Montgomery", "Amira Gross", "Gerardo Sawyer", "Devyn Cook", "Jaycee Edwards", 
            "Kolby Hatfield", "Lana Chavez", "Vincent Taylor", "Dominic Todd", "Zain Hancock", "Jimena Cantu", "Marilyn Fry", "Keely Gibbs", "Randall Campos", "Silas Garner", "Cecelia Kelly", 
            "Lauryn Roberson", "Jocelyn Hurley", "Miracle Rojas", "Lindsey Cantu", "Erica Herring", "Santiago Stout", "Leslie Beck", "Simone Cohen", "Zion Gallagher", "Gina Michael", 
            "Ruben Brooks", "Terry Blackwell", "Araceli Wells", "Haylie Davies", "Ashtyn Wyatt", "Dominick Joseph", "Cristian Ferguson", "Shawn Nash", "Landen Salinas", "Dennis Nelson", 
            "Benjamin Maddox", "Zion Dillon", "Akira Mosley", "Chasity Davila", "Tony Farmer", "Dakota Cabrera", "Janet Mcdowell", "Ben Richardson", "Ulises Sanders", "Maxwell Caldwell", 
            "Tomas Schneider", "Cohen Tucker", ]
    
    POKEMONSLIST = [EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon(), 
                EletricPokemon(), FirePokemon(), WaterPokemon()]
    
    def __init__(self, type = None, name = None, pokemons=[]) -> None:
        self.type = type

        if name:
            self.name = name
        else:
            self.name = random.choice(self.NAMESLIST)
        
        if not pokemons:
            for i in range(1, 6):
                pokemons.append(random.choice(self.POKEMONSLIST))
                
        self.pokemons = pokemons
            
    def GetRandomName() -> str:
        return random.choice(People.NAMESLIST)

    def __str__(self) -> str:
        return self.name

    def PrintPokemons(self):
        if self.pokemons:
            print("{}'s Pokemons list:".format(self))
            for index, pokemon in enumerate(self.pokemons):
                print("\t{} - {}".format(index + 1, pokemon))
        else:
            print("{} don't have any pokemons".format(self))
        
        print()

    def AddPokemon(self, pokemon):
        self.pokemons.append(pokemon)
    
    def RemovePokemon(self, pokemon):
        self.pokemons.remove(pokemon)
        

    def ChoosePokemon(self) -> Pokemon:
        index = random.randint(0, len(self.pokemons) - 1)

        print("{} chosed {}\r\n".format(self, self.pokemons[index].name))
        return self.pokemons[index]    
    
    
    def Duel(self, person):
        print("{} started a duel with {}\n".format(self, person))
        your_pokemon = self.ChoosePokemon()
        enemy_pokemon = person.ChoosePokemon()
        round = 1
        duel_result = False
        while True:
            print(">>>> Duel Round {} <<<<".format(round))
            if your_pokemon.attack(enemy_pokemon):
                print("{} defeated {}\n".format(your_pokemon.name, enemy_pokemon.name))
                duel_result = True
                break
            elif enemy_pokemon.attack(your_pokemon):
                print("{} defeated {}\n".format(enemy_pokemon.name, your_pokemon.name))
                duel_result = False
                break

            round += 1
        
        if duel_result:
            print("{}, fighting with {}, won the duel against {}, fighting with {}".format(self, your_pokemon.name, person, enemy_pokemon.name))
            print("{} earned {} from {}\n".format(self,enemy_pokemon.name, person))
            self.AddPokemon(enemy_pokemon)
            person.RemovePokemon(enemy_pokemon)
            index = self.pokemons.index(your_pokemon)
            self.pokemons[index].evolve()
        else:
            print("{}, fighting with {}, lost the duel against {}, fighting with {}".format(self, your_pokemon.name, person, enemy_pokemon.name))
            print("{} lost {} to {}".format(self,your_pokemon.name, person))
            person.AddPokemon(your_pokemon)
            self.RemovePokemon(your_pokemon)
            index = person.pokemons.index(enemy_pokemon)
            person.pokemons[index].evolve()
        
        return duel_result


class Player(People):
    
    def __init__(self, name=None, pokemons=[]) -> None:
        super().__init__("Player", name, pokemons)

    def ChoosePokemon(self) -> Pokemon:
        self.PrintPokemons()
        if self.pokemons:
            while True:
                try:
                    choice = input("Choose you pokemon: ")
                    choice = int(choice) - 1
                    chosed_pokemon = self.pokemons[choice]
                    print("{}: \"{}, I choose you!\"\r\n".format(self, chosed_pokemon.name))
                    return chosed_pokemon
                except:
                    print("Invalid input")
        else:
            return None

class Enemy(People):
    def __init__(self, type=None, name=None, pokemons=[]) -> None:
        super().__init__("Enemy", name, pokemons)
