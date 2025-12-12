class Character:
    def __init__(self, health, damage, speed):
        self.health = health
        self.damage = damage
        self.speed = speed
    def take_damage(self, amount):
        self.health -= amount

         



warrior = Character(health=150, damage=25, speed=10)        
        