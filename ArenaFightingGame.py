class Hero:
    def __init__(self, name, stats, backstory=""):
        self.name = name
        self.stats = stats
        self.backstory = backstory
        self.health = 100

    def introduce_yourself(self):
        print(
            f"I am {self.name} and my backstory is {"ups I dont have any" if self.backstory == "" else self.backstory}"
        )
        self.stats.print_values()

    def calculate_attack_damage(self):
        print("calculating attack damage...")
        return self.stats.str

    def calculate_defense(self):
        print("calculating defense...")
        return self.stats.end

    def is_dead(self):
        return self.health <= 0

    def get_hurt(self, damage):
        self.health -= damage
        print(f"health after damage: {self.health}")


class Stats:
    def __init__(self, str, dex, end, int, cha):
        self.str = str
        self.dex = dex
        self.end = end
        self.int = int
        self.cha = cha

    def print_values(self):
        print(f"Strength: {self.str}")
        print(f"Dexterity: {self.dex}")
        print(f"Endurance: {self.end}")
        print(f"Intelligence: {self.int}")
        print(f"Charisma: {self.cha}")


# Press the green button in the gutter to run the script.
if __name__ == "__main__":
    # define heroes
    warrior = Hero("Sir Punchalot", Stats(8, 2, 5, 1, 4))
    warrior.introduce_yourself()

    mage = Hero("Just Old Merlin", Stats(2, 2, 2, 9, 8))
    mage.introduce_yourself()

    fighting_round = 1
    # arena
    while True:
        print(f"Fighting round {fighting_round}")

        warrior_damage = warrior.calculate_attack_damage()
        mage_defense = mage.calculate_defense()

        damage = warrior_damage - mage_defense
        if damage > 0:
            mage.get_hurt(damage)

        # check death
        if mage.is_dead():
            print("mage is dead")
            break

        mage_damage = mage.calculate_attack_damage()
        warrior_defense = warrior.calculate_defense()

        damage = mage_damage - warrior_defense
        if damage > 0:
            warrior.get_hurt(damage)

        # check death
        if warrior.is_dead():
            print("warrior is dead")
            break

        fighting_round += 1

    print("Fight ended!")
