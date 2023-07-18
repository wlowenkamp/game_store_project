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

print(game1.genre)