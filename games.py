from tabulate import tabulate

class VGame:
    
    game_genre = "Shooters"

     # Cunstructor/initializer of object
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform
        self.genre = "Shooters"
        

    def __str__(self):
        return self.name + " | " + self.platform + " | " + self.genre
    
# Child class of Video Game
class MMORPG(VGame):

    game_genre = "Massively multiplayer online role-playing game"

    def __init__(self, name, platform):
        self.name = name
        self.platform = platform
        self.genre = "Massively multiplayer online role-playing game"
   
# Child class of Video Game
class RTS(VGame):

    game_genre = "Real-time strategy"
    
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform
        self.genre = "Real-time strategy"


# Child class of Video Game
class sports(VGame):

    game_genre = "sports"
    
    def __init__(self, name, platform):
        self.name = name
        self.platform = platform
        self.genre = 'sports'

# Child class of Video Game


"""""""""""""""""

class MOBA(VGame):

    game_genre = "Multiplayer online battle arena"
    
    def __init__(self, name, platform):
        self.name = name
        self.platformnre = platform
        self.type = 'Multiplayer online battle arena'
    
"""""""""""""""""""""

def main():
    pass

if __name__ == '__name__':
    main()