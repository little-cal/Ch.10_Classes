class Character:
    def __init__(self, name, status, strength, mc, planet):
        self.name = name
        self.status = status
        self.strength = strength
        self.midichlorian_count = mc
        self.home = planet


jedi = Character("Luke", "Master", 100, 1000, "Tatooine")


print("This object we just create was " + jedi.name)
