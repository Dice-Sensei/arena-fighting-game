from abilities.stat_boost import StatBoost
from heros.hero import Hero
from abilities.heal import Heal


class Priest(Hero):
    def __init__(self, name, stats, backstory=""):
        super().__init__(name, stats, backstory)

        self.heal_spell = Heal()
        self.stat_boost_spell = StatBoost()

    def round_tick(self):
        self.heal_spell.round_tick()
        self.stat_boost_spell.round_tick()

    def calculate_attack_damage(self):
        attack = 1.0 * self.stats.int

        print(f"calculating attack damage...from intelligence: {attack}")

        return attack

    def calculate_basic_defense(self):
        print("using basic defense")
        defense = 0.9 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense

    def calculate_defense(self):
        # check if healing is needed

        max_health_health_difference = self.max_health - self.health

        if (
            self.heal_spell.is_ready()
            and self.heal_spell.calculate_ability_strength(self.stats)
            < max_health_health_difference
        ):
            old_health = self.health
            self.health += self.heal_spell.use(self.stats)

            print(f"healing myself from {old_health:.2f} to {self.health:.2f}")
            return 0  # exposed

        if self.stat_boost_spell.is_ready():
            self.stat_boost_spell.use(self.stats)
            return 0  # exposed

        return self.calculate_basic_defense()
