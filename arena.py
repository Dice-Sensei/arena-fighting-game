class Arena:
    def __init__(self):
        self.hero2 = None
        self.hero1 = None

    def register_heroes(self, hero1, hero2):
        self.hero1 = hero1
        self.hero2 = hero2

    def introduce_heroes(self):
        print("In first corner is - ")
        self.hero1.introduce_yourself()

        print()

        print("On opposite side is standing - ")
        self.hero2.introduce_yourself()

        print()

    @staticmethod
    def introduce_arena():
        print("Welcome welcome!")
        print("Ladies and gentleman's - I will be your PA for today.")
        print("And let me introduce you today's arena!")
        print()

    @staticmethod
    def introduce_fight_format():
        print("Fight will be in format 1 : 1!")
        print()

    def pre_fight_announcements(self):
        self.introduce_arena()
        self.introduce_fight_format()
        self.introduce_heroes()

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
            print(f"Fighting round {fighting_round} starts")

            if Arena.perform_one_sided_attack_and_check_for_death(
                self.hero1, self.hero2
            ):
                break

            if Arena.perform_one_sided_attack_and_check_for_death(
                self.hero2, self.hero1
            ):
                break

            fighting_round += 1
            print()  # empty row after each fight

        print(f"Fight ended in {fighting_round} rounds!")
