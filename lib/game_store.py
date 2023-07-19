class Game_Store:
    
    all = []

    def __init__( self, name, location ):
        self.name = name
        self.location = location
        Game_Store.all.append( self )
    
    def get_name( self ):
        return self._name

    def set_name( self, new_name ):
        if hasattr( self, "_name"):
            raise Exception( "Cannot change name.")
        elif isinstance( new_name, str ):
            self._name = new_name
        else:
            raise Exception ( "Name must be string." )

    name = property( get_name, set_name )

    def get_location( self ):
        return self._location
    

    def set_location( self, new_location ):
        if hasattr( self, "_location" ):
            raise Exception ( "Cannot change location name." )
        elif isinstance( new_location, str ):
            self._location = new_location
        else:
            raise Exception ( "Location must be string" )

    location = property( get_location, set_location )



s1= Game_Store("Game Stop", "Dallas")
s2= Game_Store("Games R Us", "Cleveland")
s3= Game_Store("The Gaming Corner", "Austin")
s4= Game_Store("The VCafe", "San Diego")
s5= Game_Store("A Game in Time", "Charlotte")
s6= Game_Store("RPG IRL", "Phoenix")
s7= Game_Store("Thr Fountain of Gaming", "Chapel Hill")
s8= Game_Store("Eternal Games", "New York City")
s9= Game_Store("Bean Gaming", "Boston")
s10= Game_Store("The Flamboyant Flamingo", "Miami")

