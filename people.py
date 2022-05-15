import random
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
            

    def __str__(self) -> str:
        return self.name

    def PrintPokemons(self):
        if self.pokemons:
            print("{}'s Pokemons list:".format(self))
            for pokemon in self.pokemons:
                print("\t{}".format(pokemon))
        else:
            print("{} don't have any pokemons".format(self))

    def AddPokemon(self, pokemon):
        self.pokemons.append(pokemon)
    
    def RemovePokemon(self, pokemon):
        self.pokemons.remove(pokemon)


class Player(People):
    
    def __init__(self, name=None, pokemons=[]) -> None:
        super().__init__("Player", name, pokemons)

class Enemy(People):
    def __init__(self, type=None, name=None, pokemons=[]) -> None:
        super().__init__("Enemy", name, pokemons)
