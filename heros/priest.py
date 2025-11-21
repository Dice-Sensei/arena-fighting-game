from heros.hero import Hero


class Priest(Hero):
    def calculate_attack_damage(self):
        attack = 1.0 * self.stats.int

        print(f"calculating attack damage...from intelligence: {attack}")

        return attack

    def calculate_defense(self):
        defense = 0.9 * self.stats.end

        print(f"calculating defense: {defense}")

        return defense
