from tabulate import tabulate

class VGame:
    
    game_genre = "Shooters"

     # Cunstructor/initializer of object
    def __init__(self, title, platform, summary):
        self.title = title
        self.platform = platform
        self.genre = "Shooters"
        self.summary = summary
        

    def __str__(self):
        return self.title + " , " + self.platform + " , " + self.genre + ' , ' + self.summary 
    
# Child class of Video Game
class MMORPG(VGame):

    game_genre = "Massively multiplayer online role-playing game"

    def __init__(self, title, platform, summary):
        self.title = title
        self.platform = platform
        self.genre = "Massively multiplayer online role-playing game"
        self.summary = summary
   
# Child class of Video Game
class RTS(VGame):

    game_genre = "Real-time strategy"
    
    def __init__(self, title, platform, summary):
        self.title = title
        self.platform = platform
        self.genre = "Real-time strategy"
        self.summary = summary


# Child class of Video Game
class sports(VGame):

    game_genre = "Sport"
    
    def __init__(self, title, platform, summary):
        self.title = title
        self.platform = platform
        self.genre = 'Sport'
        self.summary = summary

# Child class of Video Game
class MOBA(VGame):

    game_genre = "Multiplayer online battle arena"
    
    def __init__(self, title, platform, summary):
        self.title = title
        self.platform = platform
        self.genre = 'Multiplayer online battle arena'
        self.summary = summary


def main():
    pass

if __name__ == '__name__':
    main()