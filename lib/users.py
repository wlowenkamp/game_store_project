class User:
    
#Potentially add list of consoles to validate through

    def __init__(self, name, console):
        self.name = name
        self.console = console 
    
    def get_name( self ):
        return self._name
    
    def set_name( self, new_name ):
        if hasattr( self, "_name" ):
            raise Exception( "Cannot change name" )
        elif isinstance( self, str ):
            self._name = new_name
        else:
            raise Exception( "Name must be a string." )
    
    name = property( get_name, set_name )


u1 = User("Will", "PS4")
u2 = User("Robert", "PS5")
u3 = User("Andrew", "XBOX One")
u4 = User("Michael", "XBOX 360")