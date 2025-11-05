class Stats:
    def __init__(self, str, dex, end, int, cha):
        self.str = str
        self.dex = dex
        self.end = end
        self.int = int
        self.cha = cha

    def print_values(self):
        print(f"Strength: {self.str}")
        print(f"Dexterity: {self.dex}")
        print(f"Endurance: {self.end}")
        print(f"Intelligence: {self.int}")
        print(f"Charisma: {self.cha}")
