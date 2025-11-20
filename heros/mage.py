from heros.hero import Hero


class Mage(Hero):
    def calculate_attack_damage(self):
        attack = 1.4 * self.stats.int

        print(f"calculating attack damage...from intelligence: {attack}")

        return attack

    def calculate_defense(self):
        defense = 0.7 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense
