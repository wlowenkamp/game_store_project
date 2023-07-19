class Game:

    def __init__(self, title, genre, price):
        self.title = title
        self.genre = genre 
        self.price = price
    
    def display_details(self):
        print(f"Title: {self.title}")
        print(f"Genre: {self.genre}")
        print(f"Price: ${self.price}")
    
    def get_title( self ):
        return self._title
    
    def set_title( self, new_title ):
        if hasattr( self, "_title" ):
            raise Exception( "Cannot change title." )
        elif isinstance( new_title, str ):
            self._title = new_title
        else:
            raise Exception( "Title must be string." )
        
    title = property( get_title, set_title )

    def get_genre( self ):
        return self._genre
    
    def set_genre( self, new_genre ):
        if hasattr( self, "_genre" ):
            raise Exception( "Cannot change genre" )
        elif isinstance( self, str ):
            self._genre = new_genre
        else:
            raise Exception( "Genre must be string" )
        
    genre = property( get_genre, set_genre )

    def get_price( self ):
        return self._price
    
    def set_price( self, new_price ):
        if hasattr( self, "_price" ):
            raise Exception( "Cannot change price." )
        elif isinstance( self, int ):
            self._price = new_price
        else:
            raise Exception( "Price must be number" )


game1 = Game("Super Smash Brothers Brawl", "Fighting", 67.50)

print(game1.genre)