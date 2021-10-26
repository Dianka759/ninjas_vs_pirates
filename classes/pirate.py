class Pirate:

    def __init__( self , name ):
        self.name = name
        self.strength = 25
        self.speed = 3
        self.health = 100

    def show_stats( self ):
        print(f"Name: {self.name}\nStrength: {self.strength}\nSpeed: {self.speed}\nHealth: {self.health}\n")
        if self.health < 0:
            print("I will remember this! ar ar ar......*pirate dies*")
            print("The ninja has won this round!")

    def attack ( self , ninja ):
        ninja.health -= self.strength
        print("pirate attacks ninja")
        return self

    def pirate_grunt(self):
        print("pirate: ARRRRRRGGhhhh!")
        return self

    def chug_rum(self):
        self.health += 10
        print("pirate +10 health, ar ar ar!")
        return self
