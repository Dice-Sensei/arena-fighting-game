from arena import Arena
from hero.hero_roster import warrior_punchalot, archer_robin


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    arena = Arena()
    arena.register_heroes(warrior_punchalot, archer_robin)
    arena.pre_fight_announcements()

    input("Pres Enter to start fight")

    arena.facilitate_fight()
