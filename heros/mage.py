from abilities.fireball import Fireball
from heros.hero import Hero


class Mage(Hero):
    def __init__(self, name, stats, backstory=""):
        super().__init__(name, stats, backstory)

        self.spells = [Fireball()]

    def calculate_attack_damage(self):
        if self.spells[0].is_ready():
            return self.spells[0].use(self.stats)

        return self.calculate_basic_attack_damage()

    def calculate_basic_attack_damage(self):
        print("using basic attack")

        attack = 1.4 * self.stats.int

        print(f"calculating attack damage...from intelligence: {attack}")

        return attack

    def calculate_defense(self):
        defense = 0.7 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense

    def round_tick(self):
        for spell in self.spells:
            spell.round_tick()
