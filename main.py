from email.policy import default
from pokemon import *
from people import *

def GetName() -> str:
    print("Hello, type you name or press enter to choose a random name:")
    name = input()
    if not name:
        name = People.GetRandomName()
    
    print("Welcome, {}".format(name))
    return name

player = Player(GetName(), pokemons=[random.choice(People.POKEMONSLIST), random.choice(People.POKEMONSLIST), random.choice(People.POKEMONSLIST)])
enemy = Enemy(name=None, pokemons=[random.choice(People.POKEMONSLIST), random.choice(People.POKEMONSLIST), random.choice(People.POKEMONSLIST)])

while True:
    choice = input("1 - Print Enemy Pokemons\r\n2 - Print Your Pokemons\r\n3 - Start Duel\r\n")
    match choice:
        case "1":
            print("-------------")
            enemy.PrintPokemons()
        
        case "2":
            print("-------------")
            player.PrintPokemons()
        
        case "3":
            print("-------------")
            result = player.Duel(enemy)
            if result == False:
                if len(player.pokemons) == 0:
                    newpokemon = random.choice(People.POKEMONSLIST)
                    print("You lost all your pokemons, but you catch a new one: {}\n".format(newpokemon))
                    player.AddPokemon(newpokemon)
            elif len(enemy.pokemons) == 0:
                    print("Your enemy, {}, lost all pokemons. Looking for a new enemy...".format(enemy))
                    enemy = Enemy(name=None, pokemons=[random.choice(People.POKEMONSLIST)])
                    print("Your new enemy is {}\n".format(enemy))
                    enemy.PrintPokemons()
        case _:
            break
        