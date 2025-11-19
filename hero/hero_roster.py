from hero.archer import Archer
from hero.mage import Mage
from hero.warrior import Warrior
from stats import Stats

# define heroes
warrior = Warrior("Sir Punchalot", Stats(8, 2, 5, 1, 4))

mage = Mage("Just Old Merlin", Stats(2, 2, 2, 9, 8))

archer = Archer("Robin the Hood", Stats(2, 8, 4, 2, 7))
