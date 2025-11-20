from heros.hero import Hero


class Archer(Hero):
    def __init__(self, name, stats, backstory=""):
        super().__init__(name, stats, backstory)
        self.ammunition = 15

    def calculate_attack_damage(self):
        if self.ammunition > 0:
            self.ammunition -= 1
            attack = 1.4 * self.stats.dex

            print(f"calculating attack damage...from dexterity: {attack}")

            return attack
        else:
            attack = 1.0 * self.stats.str

            print("I am out of ammo")
            print(f"calculating attack damage...from strength {attack}")

            return attack

    def calculate_defense(self):
        defense = 0.9 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense
