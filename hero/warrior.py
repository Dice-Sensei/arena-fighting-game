from hero.hero import Hero


class Warrior(Hero):
    def calculate_attack_damage(self):
        print("calculating attack damage...from strength")
        return self.stats.str
