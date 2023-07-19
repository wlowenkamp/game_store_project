class Game:

    def __init__(self, title, genre, price):
        self.title = title
        self.genre = genre 
        self.price = price
    
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Price: ${self.price}")

game1 = Game("Super Smash Brothers Brawl", "Fighting", 67.50)
game2 = Game("The Witcher 3: Wild Hunt", "Action role-playing", 59.99)
game3 = Game("Red Dead Redemption 2", "Action-adventure", 49.99)
game4 = Game("Fortnite", "Battle royale", 0.0)
game5 = Game("Minecraft", "Sandbox", 26.95)
game6 = Game("Overwatch", "First-person shooter", 39.99)
game7 = Game("Grand Theft Auto V", "Action-adventure", 29.99)
game8 = Game("The Legend of Zelda: Breath of the Wild", "Action-adventure", 59.99)
game9 = Game("Call of Duty: Warzone", "Battle royale", 0.0)
game10 = Game("FIFA 22", "Sports", 59.99)


