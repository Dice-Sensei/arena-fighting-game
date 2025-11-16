from arena import Arena
from hero.hero import Hero, Mage, Archer
from stats import Stats


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # define heroes
    warrior = Hero("Sir Punchalot", Stats(8, 2, 5, 1, 4))
    warrior.introduce_yourself()

    mage = Mage("Just Old Merlin", Stats(2, 2, 2, 9, 8))
    mage.introduce_yourself()

    archer = Archer("Robin the Hood", Stats(2, 8, 4, 2, 7))
    archer.introduce_yourself()

    arena = Arena()
    arena.register_heroes(warrior, archer)
    arena.introduce_heroes()
    arena.facilitate_fight()
