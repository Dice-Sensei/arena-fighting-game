from abilities.ability import Ability


class Fireball(Ability):
    """
    Fireball
    High damage ability with long cooldown
    """

    def __init__(self):
        super().__init__("Fireball")

        self.cooldown = 7
        self.cooldown_tick = 0

    def round_tick(self):
        self.cooldown_tick -= 1

    def is_ready(self):
        return self.cooldown_tick <= 0

    def use(self, stats):
        print(f"using {self.name}")
        self.cooldown_tick = self.cooldown

        attack = stats.int * 2.2

        print(f"calculating {self.name} damage...from intelligence: {attack}")

        return attack
