class Ability:
    def __init__(self, name):
        self.name = name

    def round_tick(self):
        pass

    def is_ready(self):
        raise NotImplementedError

    def use(self, stats):
        raise NotImplementedError
