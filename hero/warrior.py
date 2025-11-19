from hero.hero import Hero


class Warrior(Hero):
    def calculate_attack_damage(self):
        print("calculating attack damage...from strength")
        return self.stats.str

    def calculate_defense(self):
        defense = 1.2 * self.stats.end

        print(f"calculating defense: {defense}")
        return defense
