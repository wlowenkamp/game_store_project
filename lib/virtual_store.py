from console import *
from genre import *
from game import *

platform = Genre("Platform")
fighting = Genre("Fighting")
first_person = Genre("First-Person-Shooter")
action_adventure = Genre("Action-Adventure")


xbox = Console("XBOX")
playstation = Console("PlayStation")
nintendo = Console("Nintendo")

g1= Game("Super Lucky's Tale", platform, 29.99, xbox)
g2= Game("Ori and the Will of the Wisps", platform, 39.99, xbox)
g3= Game("Cuphead", platform, 19.99, xbox)
g4= Game("Halo Infinite", first_person, 59.99, xbox)
g5= Game("Call of Duty: Modern Warfare", first_person, 49.99, xbox)
g6= Game("Titanfall 2", first_person, 39.99, xbox)
g7= Game("Street Fighter V", fighting, 39.99, xbox)
g8= Game("Tekken 7", fighting, 49.99, xbox)
g9= Game("Mortal Kombat 11", fighting, 59.99, xbox)
g10= Game("Gears of War 5", action_adventure, 39.99, xbox)
g11= Game("Assassin's Creed Valhalla", action_adventure, 59.99, xbox)
g12= Game("Ori and the Will of the Wisps", action_adventure, 29.99, xbox)
g13= Game("Street Fighter V", fighting, 39.99, playstation)
g14= Game("Tekken 7", fighting, 49.99, playstation)
g15= Game("Mortal Kombat 11", fighting, 59.99, playstation)
g16= Game("Call of Duty: Modern Warfare", first_person, 59.99, playstation)
g17= Game("DOOM Eternal", first_person, 49.99, playstation)
g18= Game("Overwatch", first_person, 39.99, playstation)
g19= Game("Crash Bandicoot N. Sane Trilogy", platform, 39.99, playstation)
g20= Game("Ratchet & Clank: Rift Apart", platform, 59.99, playstation)
g21= Game("Astro's Playroom", platform, 0.00, playstation)
g22= Game("Spider-Man: Miles Morales", action_adventure, 69.99, playstation)
g23= Game("Ghost of Tsushima", action_adventure, 59.99, playstation)
g24= Game("The Last of Us Part II", action_adventure, 49.99, playstation)
g25= Game("Super Mario Odyssey", platform, 59.99, nintendo)
g26= Game("Donkey Kong Country: Tropical Freeze", platform, 59.99, nintendo)
g27= Game("Celeste", platform, 19.99, nintendo)
g28= Game("Super Smash Bros. Ultimate", fighting, 59.99, nintendo)
g29= Game("ARMS", fighting, 59.99, nintendo)
g30= Game("Pokkén Tournament DX", fighting, 59.99, nintendo)
g31= Game("The Legend of Zelda: Breath of the Wild", action_adventure, 59.99, nintendo)
g32= Game("Luigi's Mansion 3", action_adventure, 59.99, nintendo)
g33= Game("Splatoon 2", action_adventure, 59.99, nintendo)

def display_consoles():
    print("Available Consoles:")
    for console in [xbox, playstation, nintendo]:
        print(console.name)

def display_genres():
    print ("Available Genres:")
    for genre in [platform, fighting, first_person, action_adventure]:
        print(genre.name)

def get_valid_console():
    while True:
        display_consoles()
        user_console = input("\nPlease type a console: ")
        console_names = [console.name.lower() for console in [xbox, playstation, nintendo]]
        if user_console.lower() in console_names:
            return user_console
        else:
            print("\nInvalid console name. Please choose from the available consoles.")

def get_valid_genre():
    while True:
        display_genres()
        user_genre = input("\nPlease type a genre: ")
        genre_names = [genre.name.lower().replace("-", "_") for genre in [platform, fighting, first_person, action_adventure]]
        if user_genre.lower() in genre_names:
            return user_genre
        else:
            print("\nInvalid genre name. Please choose from the available genres.")

def display_games(console_name, genre_name):
    console = globals()[console_name.lower()]
    genre = globals()[genre_name.lower().replace("-", "_")]
    print(f"\nGames for {console_name} console in the {genre_name} genre:")
    for game in [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33]:
        if game.console == console and game.genre == genre:
            print(game.title)

def run_store():
    print("\nWelcome to Games R Us!")
    # display_consoles()
    user_console = get_valid_console()
    # display_genres()
    user_genre = get_valid_genre()
    display_games(user_console, user_genre)

    selected_game = None
    while selected_game is None:
        game_title = input("\nPlease type the title of the game you'd like to select:  ")
        for game in [g1, g2, g3, g4, g5, g6, g7, g8, g9, g10, g11, g12, g13, g14, g15, g16, g17, g18, g19, g20, g21, g22, g23, g24, g25, g26, g27, g28, g29, g30, g31, g32, g33]:
            if game.title.lower() == game_title.lower():
                selected_game = game
                break

        if selected_game is None:
            print("\nInvalid game title. Maybe you should just copy and paste...")
    print(f"The price of {selected_game.title} is {selected_game.price}")

    choice = input("\nPress 'a' to select a new game, or press 'x' to exit: ")

    while choice.lower() != "x":
        if choice.lower() == "a":
            run_store()
            break
        else: 
            choice = input ("\nInvald input. Press 'a' to select a new game, or press 'x' to exit: ")

    print("\nThanks for stopping by!")
    print("""
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀██┼███▀▀▀███┼███▀█▄█▀███┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼█┼┼┼██┼██┼┼┼
██┼┼┼▄▄▄┼██▄▄▄▄▄██┼██┼┼┼▀┼┼┼██┼██▀▀▀
██┼┼┼┼██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██┼┼┼
███▄▄▄██┼██┼┼┼┼┼██┼██┼┼┼┼┼┼┼██┼██▄▄▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
███▀▀▀███┼▀███┼┼██▀┼██▀▀▀┼██▀▀▀▀██▄┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██┼┼┼┼██┼┼┼┼┼██┼
██┼┼┼┼┼██┼┼┼██┼┼██┼┼██▀▀▀┼██▄▄▄▄▄▀▀┼
██┼┼┼┼┼██┼┼┼██┼┼█▀┼┼██┼┼┼┼██┼┼┼┼┼██┼
███▄▄▄███┼┼┼─▀█▀┼┼─┼██▄▄▄┼██┼┼┼┼┼██▄
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼██┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼████▄┼┼┼▄▄▄▄▄▄▄┼┼┼▄████┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼▀▀█▄█████████▄█▀▀┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████████████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██▀▀▀███▀▀▀██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼██┼┼┼███┼┼┼██┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼█████▀▄▀█████┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼███████████┼┼┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▄▄▄██┼┼█▀█▀█┼┼██▄▄▄┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼▀▀██┼┼┼┼┼┼┼┼┼┼┼██▀▀┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼▀▀┼┼┼┼┼┼┼┼┼┼┼
┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼┼
""")

run_store()