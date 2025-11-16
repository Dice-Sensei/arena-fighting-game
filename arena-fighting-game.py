from arena import Arena
from hero.hero_roster import warrior, archer


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    arena = Arena()
    arena.register_heroes(warrior, archer)
    arena.introduce_heroes()
    arena.facilitate_fight()
