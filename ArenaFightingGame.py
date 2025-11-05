from stats import Stats
from hero.hero import Hero, Mage, Archer


def perform_one_sided_attack(attacker, defender):
    attacker_damage = attacker.calculate_attack_damage()
    defender_defense = defender.calculate_defense()

    damage = attacker_damage - defender_defense
    if damage > 0:
        defender.get_hurt(damage)


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # define heroes
    warrior = Hero("Sir Punchalot", Stats(8, 2, 5, 1, 4))
    warrior.introduce_yourself()

    mage = Mage("Just Old Merlin", Stats(2, 2, 2, 9, 8))
    mage.introduce_yourself()

    archer = Archer("Robin the Hood", Stats(2, 8, 4, 2, 7))
    archer.introduce_yourself()

    fighting_round = 1
    # arena
    while True:
        print(f"Fighting round {fighting_round}")

        perform_one_sided_attack(warrior, archer)

        # check death
        if archer.is_dead():
            print("archer is dead")
            break

        perform_one_sided_attack(archer, warrior)

        # check death
        if warrior.is_dead():
            print("warrior is dead")
            break

        fighting_round += 1

    print("Fight ended!")
