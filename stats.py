import color_helper


class Stats:
    def __init__(self, str, dex, end, int, cha):
        self.str = str
        self.dex = dex
        self.end = end
        self.int = int
        self.cha = cha

    def print_values(self):
        print(f"Strength: {color_helper.red(self.str)}")
        print(f"Dexterity: {color_helper.green(self.dex)}")
        print(f"Endurance: {color_helper.yellow(self.end)}")
        print(f"Intelligence: {color_helper.blue(self.int)}")
        print(f"Charisma: {color_helper.pink(self.cha)}")
