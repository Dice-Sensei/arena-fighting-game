from abilities.ability import Ability


class Heal(Ability):
    """
    Heal
    An ability to regenerate some health
    """

    def __init__(self):
        super().__init__("Heal")

        self.uses = 2
        self.uses_left = self.uses

    def is_ready(self):
        return self.uses_left > 0

    @staticmethod
    def calculate_ability_strength(stats):
        return 4 * stats.int

    def use(self, stats):
        print(f"using {self.name}")

        self.uses_left -= 1

        health_to_restore = self.calculate_ability_strength(stats)

        print(f"calculating {self.name} healing: {health_to_restore}")

        return health_to_restore
