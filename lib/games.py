class Game:
    def __init__(self, title, genre, price, console):
        self.title = title
        self.genre = genre
        self.price = price
        self.console = console

    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Price: ${self.price}")
        print(f"Console: {self.console}")


game1 = Game("Halo 3", "First-person shooter", 19.99, "Xbox 360")
game2 = Game("Gears of War", "Third-person shooter", 14.99, "Xbox 360")
game3 = Game("Mass Effect", "Action role-playing", 9.99, "Xbox 360")
game4 = Game("Red Dead Redemption", "Action-adventure", 24.99, "Xbox 360")
game5 = Game("BioShock", "First-person shooter", 12.99, "Xbox 360")
game6 = Game("The Elder Scrolls V: Skyrim", "Action role-playing", 17.99, "Xbox 360")
game7 = Game("Call of Duty: Modern Warfare 2", "First-person shooter", 9.99, "Xbox 360")
game8 = Game("Fallout 3", "Action role-playing", 14.99, "Xbox 360")
game9 = Game("Grand Theft Auto V", "Action-adventure", 19.99, "Xbox 360")
game10 = Game("FIFA 14", "Sports", 7.99, "Xbox 360")


