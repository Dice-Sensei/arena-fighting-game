from hero.hero import Hero


class Mage(Hero):
    def calculate_attack_damage(self):
        print("calculating attack damage...from intelligence")
        return self.stats.int

    def calculate_defense(self):
        defense = 0.7 * self.stats.end

        print(f"calculating defense: {defense}")
        return defense
