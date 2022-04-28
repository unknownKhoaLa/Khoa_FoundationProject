import re
import games
import json
from pymongo import MongoClient


# Setting db_week4 to the game project db on MongoDB
client = MongoClient()
db_week4 = client.week4
GameProject = db_week4.GameProject


# Add Video Game info to the list of a genre
def add_game() -> games.VGame:
    
    while True:
        try:
            print("Hello! Please select a genre of video game to input: ")
            print("\t a) Shoots")
            print("\t b) MMORPG")
            print("\t c) RTS")
            selectGame= input(">>>")

            if not selectGame == 'a' and not selectGame == 'b' and not selectGame == 'c':
                raise ValueError
            else:
                break
        except ValueError:
            print('Invalid input for game genre')
            print("Please enter an appropriatea input. ")
            pass

    while True:
        try:
            print("\n\nType a new game name: ")
            name = input(">>>")
            # \ . * \-
            if not re.search(r"[,\,\\\*\-]", name) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("Please do not use special characters.")
    
    while True:
        try:
            print("\n\nType a platform 'PC' or 'Console': ")
            platform = (input(">>>"))
        
            if not platform == 'PC' and not platform == 'Console':
                raise ValueError('Invalid input for game platform')
            else:
                break

        except ValueError:
            print("")

    if selectGame == 'a':
        newGame = games.VGame(name, platform)
    elif selectGame == 'b':
        newGame = games.MMORPG(name, platform)
    else:
        newGame = games.RTS(name, platform)

    return newGame

# Save games list to gamelist.json
def save_games(game):

    game_dict = {
        "name" : game.name,
        "platform" : game.platform,
        "genre" : game.genre       
        }
    
    GameProject.insert_one(game_dict)


# Load data from gamelist.json
def load_gameslist():
 #   f  = open('gamelist1.json', 'r')

    game = GameProject.find()
    
 #   list_games = json.load(f)

    lst_games = []
    
    for line in game:

      #  print(line)

 #       if line == '':
 #           break

 #       game_data = line.split(',')

  #      if game_data[2].strip() == 'Shoots':
   #         newGame = games.VGame(game_data[0], game_data[1])
  #      elif game_data[2].strip() == 'Massively multiplayer online role-playing game':
  #          newGame = games.MMORPG(game_data[0], game_data[1])
   #     else:
    #        newGame = games.RTS(game_data[0], game_data[1])

        lst_games.append(line)


 #   f.close()
    return lst_games



# Main function
def main():
    print("The Video Games Wiki")

    lst_Games = load_gameslist()

    while True:
        try:
            print("Display the Video Games List:")
            print("\ta) Type 'a' to add the video game to the list")
            print("\ts) Type 's' to see the video games' list")

            option = input(">>>")

            if option == 's':
                break
            elif option == 'a':
                #lst_Games.append(add_game())
                newGame = add_game()
                # Here's what we need to do: Let's save a game one game at a time, instead of creating a list. this way, we can still
                # use the list when we load the games to populate our list.
            else:
                raise ValueError("Invalid input") 

        except ValueError:
            print("Invalid intput! Please try again!")
            

    save_games(newGame)
    lst_Games = load_gameslist()

    for games in lst_Games:
        print(games)


if __name__ == "__main__":
    main()



