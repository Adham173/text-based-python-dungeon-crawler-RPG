# this is the hero file
import random
class Hero:
    def __init__(self, name, hero_health, att_power):
        self.name = name
        self.hero_health = hero_health
        self.att_power = att_power

    def attack(self, target_enemy):
     damage = random.randint(30, self.att_power)
     target_enemy.enm_health -= damage
     print(f'YOU DEALT {damage}! BOSS HEALTH: {target_enemy.enm_health}')
    def is_alive(self):
        return self.hero_health > 0





