class Ninja:
    def __init__(self, name, health = 100, strength = 10):
        self.name = name
        self.health = health
        self.strength = strength

    def check_stats(self):
        print(self.name, self.health, self.strength)
        return self
    
    def attack(self, target):
        target.health -= self.strength
        print(f"{self.name} attacks {target.name} and deals {self.strength} damage!")
        print(target.name, "has", target.health, "hp left!")
        print(self.name, "has", self.health, "hp left!")
        return self

# Inheritance
class Tiger_Clan(Ninja):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
        self.is_crouching = True

    def attack(self, target):
        if self.is_crouching:
            self.strength += self.strength
            self.is_crouching = False
            super().attack(target)
        else:
            self.is_crouching = True
            self.strength -= self.strength//2
            super().attack(target)
        return self

class Dragon_Clan(Ninja):
    def __init__(self, name, health, strength):
        super().__init__(name, health, strength)
        self.is_hidden = True

    def attack(self, target):
        if self.is_hidden:
            self.health += self.strength
            self.is_hidden = False
            super().attack(target)
        else:
            self.is_hidden = True
            super().attack(target)
        return self

Leo = Tiger_Clan("Leo", 100, 10)
Raph = Dragon_Clan("Raph", 100, 10)

Leo.attack(Raph)
Raph.attack(Leo)
Leo.attack(Raph)
Raph.attack(Leo)