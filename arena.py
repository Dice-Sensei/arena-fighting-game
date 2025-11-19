class Arena:
    def __init__(self):
        self.hero2 = None
        self.hero1 = None

    def register_heroes(self, hero1, hero2):
        self.hero1 = hero1
        self.hero2 = hero2

    def introduce_heroes(self):
        self.hero1.introduce_yourself()
        self.hero2.introduce_yourself()

    @staticmethod
    def perform_one_sided_attack(attacker, defender):
        attacker_damage = attacker.calculate_attack_damage()
        defender_defense = defender.calculate_defense()

        damage = attacker_damage - defender_defense
        if damage > 0:
            defender.take_damage(damage)

    @staticmethod
    def perform_one_sided_attack_and_check_for_death(attacker, defender):
        Arena.perform_one_sided_attack(attacker, defender)
        if defender.is_dead():
            print(f"{defender.name} is dead")
            return True
        return False

    def facilitate_fight(self):
        if self.hero1 is None or self.hero2 is None:
            raise ValueError("Heroes must be registered before starting the fight")

        fighting_round = 1

        while True:
            print(f"Fighting round {fighting_round}")

            if Arena.perform_one_sided_attack_and_check_for_death(
                self.hero1, self.hero2
            ):
                break

            if Arena.perform_one_sided_attack_and_check_for_death(
                self.hero2, self.hero1
            ):
                break

            fighting_round += 1

        print(f"Fight ended in {fighting_round} rounds!")
