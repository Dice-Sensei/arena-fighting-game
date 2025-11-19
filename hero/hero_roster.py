from hero.hero import Hero
from hero.archer import Archer
from hero.mage import Mage
from stats import Stats

# define heroes
warrior = Hero("Sir Punchalot", Stats(8, 2, 5, 1, 4))

mage = Mage("Just Old Merlin", Stats(2, 2, 2, 9, 8))

archer = Archer("Robin the Hood", Stats(2, 8, 4, 2, 7))
