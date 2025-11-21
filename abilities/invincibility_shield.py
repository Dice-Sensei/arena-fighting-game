from abilities.ability import Ability


class InvincibilityShield(Ability):
    """
    Invincibility Shield
    Prevents one attack (just holds tons of damage)
    """

    def __init__(self):
        super().__init__("Invincibility Shield")

        self.uses = 2
        self.uses_left = self.uses

    def is_ready(self):
        return self.uses_left > 0

    def use(self, stats):
        print(f"using {self.name}")

        self.uses_left -= 1

        defense = 99

        print(f"calculating {self.name} defense: {defense}")

        return defense
