from abilities.fireball import Fireball
from abilities.invincibility_shield import InvincibilityShield
from heros.hero import Hero


class Mage(Hero):
    def __init__(self, name, stats, backstory=""):
        super().__init__(name, stats, backstory)

        self.attack_abilities = (Fireball(),)
        self.defense_abilities = (InvincibilityShield(),)

    def calculate_attack_damage(self):
        if self.attack_abilities[0].is_ready():
            return self.attack_abilities[0].use(self.stats)

        return self.calculate_basic_attack_damage()

    def calculate_basic_attack_damage(self):
        print("using basic attack")

        attack = 1.4 * self.stats.int

        print(f"calculating attack damage...from intelligence: {attack}")

        return attack

    def calculate_defense(self):
        if self.max_health / 2 > self.health and self.defense_abilities[0].is_ready():
            return self.defense_abilities[0].use(self.stats)

        return self.calculate_basic_defense()

    def calculate_basic_defense(self):
        print("using basic defense")
        defense = 0.7 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense

    def round_tick(self):
        for abilities in self.attack_abilities:
            abilities.round_tick()

        for abilities in self.defense_abilities:
            abilities.round_tick()
