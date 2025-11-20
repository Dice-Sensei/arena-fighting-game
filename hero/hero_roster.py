from hero.archer import Archer
from hero.mage import Mage
from hero.warrior import Warrior
from stats import Stats
from input_handler import request_number_input

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


all_heroes = [warrior_punchalot, mage_merlin, archer_robin]


def introduce_all_heroes():
    for index, hero in enumerate(all_heroes):
        print(f"{index + 1})")
        hero.introduce_yourself()
        print()


def select_hero():
    print("Select what hero you want to represent you")

    introduce_all_heroes()

    hero_index = request_number_input("Select hero:", 1, len(all_heroes))

    selected_hero = all_heroes[hero_index - 1]

    print(f"Hero selected: {selected_hero.name}")

    return selected_hero


def select_opponent():
    print("Select opponent")

    introduce_all_heroes()

    hero_index = request_number_input("Select opponent:", 1, len(all_heroes))

    selected_hero = all_heroes[hero_index - 1]

    print(f"Opponent selected: {selected_hero.name}")

    return selected_hero


def select_fighters():
    hero = select_hero()
    print()

    while True:
        opponent = select_opponent()

        if opponent == hero:
            print("Opponent can't be same as hero, select again")
            continue

        break

    print()
    return hero, opponent
