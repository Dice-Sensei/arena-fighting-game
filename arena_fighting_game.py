from arena import Arena
from heros.hero_roster import select_fighters


# Press the green button in the gutter to run the script.
if __name__ == "__main__":

    # select heroes
    heroes = select_fighters()

    arena = Arena()
    arena.register_heroes(heroes[0], heroes[1])
    arena.prepare_fight()

    input("Pres Enter to start fight ")

    arena.facilitate_fight()
