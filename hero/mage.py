from hero.hero import Hero


class Mage(Hero):
    def calculate_attack_damage(self):
        print("calculating attack damage...from intelligence")
        return self.stats.int
