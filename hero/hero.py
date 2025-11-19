class Hero:
    def __init__(self, name, stats, backstory=""):
        self.name = name
        self.stats = stats
        self.backstory = backstory
        self.health = 100

    def introduce_yourself(self):
        print(
            f"I am {self.name} and my backstory is {"ups I dont have any" if self.backstory == "" else self.backstory}"
        )
        self.stats.print_values()

    def calculate_attack_damage(self):
        print("calculating attack damage...from strength")
        return self.stats.str

    def calculate_defense(self):
        print("calculating defense...")
        return self.stats.end

    def is_dead(self):
        return self.health <= 0

    def take_damage(self, damage):
        self.health -= damage
        print(f"health after damage: {self.health}")
