from abilities.ability import Ability


class StatBoost(Ability):
    """
    Spell to boost stats by one (permanent)
    """

    def __init__(self):
        super().__init__("Stat boost")

        self.cooldown = 5
        self.cooldown_tick = 2
        self.uses = 2
        self.uses_left = self.uses

    def round_tick(self):
        self.cooldown_tick -= 1

    def is_ready(self):
        return self.uses_left > 0 and self.cooldown_tick <= 0

    def use(self, stats):

        self.cooldown_tick = self.cooldown
        self.uses_left -= 1

        print("boosting self stats by +1")

        stats.int += 1
        stats.str += 1
        stats.cha += 1
        stats.dex += 1
        stats.end += 1

        return 0
