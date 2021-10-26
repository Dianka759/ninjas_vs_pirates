class Ninja:

    def __init__( self , name ):
        self.name = name
        self.strength = 30
        self.speed = 5
        self.health = 100
    
    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        if self.health < 0:
            print("I will have my revenge......*dies*")
            print("The pirate has won this round!")

    def attack( self , pirate ):
        pirate.health -= self.strength
        print("ninja attacks pirate")
        return self

    def ninja_grunt(self):
        print("ninja: OOOF!")
        return self
    
    def super_attack(self, pirate):
        pirate.health -= self.strength + 50
        print("entering super sayan mode, dmg +50")
        return self