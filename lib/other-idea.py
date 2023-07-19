class Genre:
    def __init__(self, name):
        self.name = name


class Console:
    def __init__(self, name):
        self.name = name


class Game:
    def __init__(self, title, genre, price, console):
        self.title = title
        self.genre = genre
        self.price = price
        self.console = console


genres = [
    Genre("Platform"),
    Genre("Fighting"),
    Genre("First Person Shooter"),
    Genre("Action-Adventure"),
]

consoles = [
    Console("Xbox"),
    Console("PlayStation"),
    Console("Nintendo"),
]

games = [
    Game("Super Lucky's Tale", genres[0], 29.99, consoles[0]),
    Game("Ori and the Will of the Wisps", genres[0], 39.99, consoles[0]),
    Game("Cuphead", genres[0], 19.99, consoles[0]),
    Game("Halo Infinite", genres[2], 59.99, consoles[0]),
    Game("Call of Duty: Modern Warfare", genres[2], 49.99, consoles[0]),
    Game("Titanfall 2", genres[2], 39.99, consoles[0]),
    Game("Street Fighter V", genres[1], 39.99, consoles[0]),
    Game("Tekken 7", genres[1], 49.99, consoles[0]),
    Game("Mortal Kombat 11", genres[1], 59.99, consoles[0]),
    Game("Gears of War 5", genres[3], 39.99, consoles[0]),
    Game("Assassin's Creed Valhalla", genres[3], 59.99, consoles[0]),
    Game("Ori and the Will of the Wisps", genres[3], 29.99, consoles[0]),
    Game("Street Fighter V", genres[1], 39.99, consoles[1]),
    Game("Tekken 7", genres[1], 49.99, consoles[1]),
    Game("Mortal Kombat 11", genres[1], 59.99, consoles[1]),
    Game("Call of Duty: Modern Warfare", genres[2], 59.99, consoles[1]),
    Game("DOOM Eternal", genres[2], 49.99, consoles[1]),
    Game("Overwatch", genres[2], 39.99, consoles[1]),
    Game("Crash Bandicoot N. Sane Trilogy", genres[0], 39.99, consoles[1]),
    Game("Ratchet & Clank: Rift Apart", genres[0], 59.99, consoles[1]),
    Game("Astro's Playroom", genres[0], 0.00, consoles[1]),
    Game("Spider-Man: Miles Morales", genres[3], 69.99, consoles[1]),
    Game("Ghost of Tsushima", genres[3], 59.99, consoles[1]),
    Game("The Last of Us Part II", genres[3], 49.99, consoles[1]),
    Game("Super Mario Odyssey", genres[0], 59.99, consoles[2]),
    Game("Donkey Kong Country: Tropical Freeze", genres[0], 59.99, consoles[2]),
    Game("Celeste", genres[0], 19.99, consoles[2]),
    Game("Super Smash Bros. Ultimate", genres[1], 59.99, consoles[2]),
    Game("ARMS", genres[1], 59.99, consoles[2]),
    Game("Pokkén Tournament DX", genres[1], 59.99, consoles[2]),
    Game("The Legend of Zelda: Breath of the Wild", genres[3], 59.99, consoles[2]),
    Game("Luigi's Mansion 3", genres[3], 59.99, consoles[2]),
    Game("Splatoon 2", genres[3], 59.99, consoles[2]),
]


def welcome_to_games_r_us():
    print("Welcome to Games R Us!")


def select_model(options, model_name):
    while True:
        print(f"Select a {model_name}:")
        for index, option in enumerate(options, start=1):
            print(f"{index}. {option.name}")
        selection = input("Enter the number of the selection: ")
        if selection.isdigit():
            selection_index = int(selection) - 1
            if 0 <= selection_index < len(options):
                return options[selection_index]
        print("Invalid selection. Please try again.")


def get_matching_games(console, genre):
    matching_games = [game for game in games if game.console == console and game.genre == genre]
    return matching_games


def main():
    welcome_to_games_r_us()
    console = select_model(consoles, "console")
    genre = select_model(genres, "genre")

    matching_games = get_matching_games(console, genre)

    while not matching_games:
        print("\nNo matching games found. Please make another selection.")
        console = select_model(consoles, "console")
        genre = select_model(genres, "genre")
        matching_games = get_matching_games(console, genre)

    print("\nHere are the matching games:")
    for index, game in enumerate(matching_games, start=1):
        print(f"{index}. {game.title}")

    selected_game = int(input("\nEnter the number of the game you want to select: ")) - 1

    if 0 <= selected_game < len(matching_games):
        game = matching_games[selected_game]
        print(f"\nYou selected '{game.title}'. The price is ${game.price:.2f}.")
    else:
        print("\nInvalid game selection.")


if __name__ == "__main__":
    main()

