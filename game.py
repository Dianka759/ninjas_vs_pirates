from classes.ninja import Ninja
from classes.pirate import Pirate

michelangelo = Ninja("Michelanglo")
jack_sparrow = Pirate("Jack Sparrow")


michelangelo.show_stats()
jack_sparrow.show_stats()

print("Round one")
print()

michelangelo.attack(jack_sparrow).attack(jack_sparrow)
jack_sparrow.pirate_grunt().show_stats()

print("Next Turn")
print()


jack_sparrow.chug_rum().attack(michelangelo).attack(michelangelo)
michelangelo.ninja_grunt().show_stats()

print("Next Turn")
print()

michelangelo.super_attack(jack_sparrow)
jack_sparrow.pirate_grunt().pirate_grunt().show_stats()