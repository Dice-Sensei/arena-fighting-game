from hero.hero import Hero


class Warrior(Hero):
    def calculate_attack_damage(self):
        attack = 1.2 * self.stats.str

        print(f"calculating attack damage...from strength: {attack}")

        return attack

    def calculate_defense(self):
        defense = 1.2 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense
