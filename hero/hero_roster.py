from hero.archer import Archer
from hero.mage import Mage
from hero.warrior import Warrior
from stats import Stats

# define heroes
warrior_punchalot = Warrior(
    "Sir Punchalot",
    Stats(8, 2, 5, 1, 4),
    "If punching people was discipline this would be a champion.",
)

mage_merlin = Mage(
    "Just Old Merlin",
    Stats(2, 2, 2, 9, 8),
    "Once everywhere know for his intelligence and wisdom, now just old senile husk.",
)

archer_robin = Archer(
    "Robin the Hood",
    Stats(2, 8, 4, 2, 7),
    "Taking from rich and giving everything to himself.",
)
