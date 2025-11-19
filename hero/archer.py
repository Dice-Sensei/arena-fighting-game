from hero.hero import Hero


class Archer(Hero):
    def __init__(self, name, stats, backstory=""):
        super().__init__(name, stats, backstory)
        self.ammunition = 15

    def calculate_attack_damage(self):

        if self.ammunition > 0:
            print("calculating attack damage...from dexterity")

            self.ammunition -= 1

            return self.stats.dex
        else:
            return super().calculate_attack_damage()
