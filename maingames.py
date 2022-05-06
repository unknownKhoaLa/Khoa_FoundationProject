import re
import games
from pymongo import MongoClient
import json
import pandas as pd


# Setting db_week4 to the game project db on MongoDB
client = MongoClient("127.0.0.1", 27017)
db_week4 = client.week4
GameProject = db_week4.GameProject


# Type (1): Adding Video Game info to the list of a genre
def add_game() -> games.VGame:
    
    # Selecting a genre
    while True:
        try:
            print('')
            print("Enter a genre of video game to add: ")
            print("\t a) Shooter")
            print("\t b) MMORPG")
            print("\t c) RTS")
            print("\t d) MOBA")
            print("\t e) Sport")
            selectGame= input(">>>")

            if not selectGame == 'a' and not selectGame == 'b' and not selectGame == 'c' and not selectGame == 'd' and not selectGame == 'e':
                raise ValueError
            else:
                break
        except ValueError:
            print("Invalid input for game genre. Please enter an appropriatea input.")
            
    # Typing a name of the video game
    while True:
        try:
            print("\nWrite a new game title: ")
            title = input(">>>")
            if not re.search(r"[\@\#\$\%\^\&\~\_\+\=\`\\\*]", title) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print("\nPlease do not use special characters.")
    
    # Typing a platform of the video game
    while True:
        try:
            print("\nType a platform - 'PC', 'Console', or 'PC & Console': ")
            platform = (input(">>>"))
        
            if not platform == 'PC' and not platform == 'Console' and not platform == 'PC & Console':
                raise ValueError
            else:
                break
        except ValueError:
            print('\nInvalid input for game platform. Please type an platform')

    # Typing a summary of the video game
    while True:
        try:
            print("\nWrite a summary about the video game: ")
            summary = (input(">>>"))
        
            if not re.search(r"[\@\#\$\%\^\&\~\_\+\=\`\\\*]", summary) == None:
                raise ValueError
            else:
                break
        except ValueError:
            print('\nPlease do not use special characters.')

    print('')
    print( '"' +  title  +  '"' + " is added to the Encyclopedia.")

    # Childen of parent games.py
    if selectGame == 'a':
        new_Game = games.VGame(title, platform, summary)
    elif selectGame == 'b':
        new_Game = games.MMORPG(title, platform, summary)
    elif selectGame == 'c':
        new_Game = games.RTS(title, platform, summary)
    elif selectGame == 'd':
        new_Game = games.MOBA(title, platform, summary)
    else:
        new_Game = games.sports(title, platform, summary)

    return new_Game

# Type (2): Updating the edited video game information to the database
def update_game_db():

    while True:
        try:
            print('')
            print("Enter a title from above to update: ")
            type_title= input(">>>")

            find_game = GameProject.find_one({"title" : type_title})

            if  find_game == None:
                raise ValueError
            else:
                break
        
        # The error will occur when the title does not exist in the database. 
        except ValueError:
            print('')
            print('"' + type_title + '"' + " does not exist in the database.")
            print("Please enter the title again.")


    # Updating the edited platfrom of the video game
    while True:
        name_game = {"title": type_title}

        try:
            print("\nEnter below to edit: ")
            print("\t a) platform")
            print("\t b) summary")
            print("\t c) quit")
            type_update = input(">>>")            
            

            # Updating the edited platform of the video game
            if type_update == 'a': 
                    
                print("\nEnter 'PC', 'Console', or 'PC & Console' to update:")
                update_platform = input(">>>")
                    
                if not update_platform == 'PC' and not update_platform == 'Console' and not update_platform == 'PC & Console':
                    raise ValueError
                else:
                    update_info = {"$set": {"platform" : update_platform}}
                    GameProject.update_one(name_game, update_info)
                    print(type_title + " is updated with new information to the platfrom.")

            # Updating the edited summary of the video game
            elif type_update == 'b':

                print("\nWrite a new summary to update:")
                update_summary = input(">>>")
                    
                if not re.search(r"[\@\#\$\%\^\&\~\_\+\=\`\\\*]", update_summary) == None:
                    raise ValueError
                else:
                    update_info2 = {"$set": {"summary" : update_summary}}
                    GameProject.update_one(name_game, update_info2)
                    print(type_title + " is updated with new information to the summary.")

            # No edited and quiting to go back to the main menu
            elif type_update == 'c' :
                print("\nNo edits made to the video game encyclopedia.")
                break
            else:
                raise ValueError

        except ValueError:
            print("\nInvalid input.")

# Type (4): Deleting a video game information from the database
def delete_game_db() :
    
    while True:
        try:
            print('')
            print("Enter a title from above to delete: ")
            type_title2= input(">>>")
            
            find_game2 = GameProject.find_one({"title" : type_title2})

            if find_game2 == None:
                raise ValueError
            else:
                delete_game = {"title": type_title2}
                GameProject.delete_one(delete_game)
                break

        # The error will occur when the title does not exist in the database. 
        except ValueError:
            print('')
            print('"' + type_title2 + '"' + " does not exist in the database.")
            print("Please enter a title existed in the database.")

    print('')
    print('"' + type_title2 + '"' +" is deleted from the encyclopedia.")
    

# Type (1): Writing a video game information to the JSON file
def save_game_JSON(game2):
    
    # JSON data input
    game_dict2 = {
        "title" : game2.title,
        "platform" : game2.platform,
        "genre" : game2.genre,
        "summary" : game2.summary       
        }

    with open("gamelist2.json",'r+') as f:
        # First load existing data into a dict.
        games_list = json.load(f)
        # Join game2 with file_data inside [] list
        games_list.append(game_dict2)
        # Sets file's current position at offset.
        f.seek(0)
        # convert back to json.
        json.dump(games_list, f, indent = 4)  # indent = 4 for pretty-printed
    

# Type (1): Writing a video game information to the database
def save_game_db(game):

    # Database data input
    game_dict = {
        "title" : game.title,
        "platform" : game.platform,
        "genre" : game.genre,
        "summary" : game.summary       
        }
    
    # Inserting the new data into the database
    GameProject.insert_one(game_dict)


# Type (2 and 4): Reading the list from the database.
def load_gameslist():

    game = GameProject.find()

    # old way to print the list
    '''   
    lst_games = []
    for line in game:
        lst_games.append(line)
    return lst_games
    '''
    # Use Pandas to print the table
    df = pd.DataFrame(list(game))           
    print(df.loc[:, df.columns != '_id'])

# Reading the list from the JSON file
def load_gameslist2():


    # old way to print the list
    '''
    with open("gamelist2.json") as game_list:
        data = json.load(game_list)
        pprint.pprint(data, sort_dicts=False) # pprint for pretty list and no ordered.
    '''
    # Use Pandas to print the table
    df2 = pd.read_json("gamelist2.json")
    print(df2)

# Main function
def main():
    print("The Video Games Encyclopedia")

    # Loading the list from the database.
    ''' 
    lst_Games = load_gameslist()
    '''

    # Select a number from the menu
    while True:
        try:
            print('')
            print("The menu to enter:")
            print("\t1) Add a video game")
            print("\t2) Edit a new info to the game in the database")
            print("\t3) View the list of video games")
            print("\t4) Delete a video game from the database")
            print("\t5) Quit to save" )

            menu = input(">>>")

            # Quitting the application to save the data
            if menu == '5':
                print("It is saved!")
                break

            # Adding a new video game to the list in the database and JSON file
            elif menu == '1':
                newGame = add_game()
                save_game_JSON(newGame) # for adding to the JSON 
                save_game_db(newGame)   # for adding to the databae

            # Updating the edited video game information to the database
            elif menu == '2':

                #Loading the list from the database
                load_gameslist()
                '''
                for games in lst_Games:      
                    pprint.pprint(games, sort_dicts=False)
                '''
                update_game_db()

            # Reading the video game list from the JSON file
            elif menu == '3':
                
                #Loading the list from the JSON file
                load_gameslist2()
                
                # this will not be used for the presentation. It is for reading the list from the database
                '''
                for games in lst_Games:      
                    print(games)
                '''

                
            # Deleting a video game information from the database
            elif menu == '4':
                
                #Loading the list from the database
                load_gameslist()
                '''
                for games in lst_Games:      
                    pprint.pprint(games, sort_dicts=False)
                '''

                delete_game_db()

            # The error will occur if the user does not enter any nunmber from the menu. 
            else:
                raise ValueError 
            
        except ValueError:
            print("Invalid intput. Please enter a number from the menu.")

if __name__ == "__main__":
    main()



