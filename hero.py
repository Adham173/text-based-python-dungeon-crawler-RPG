# this is the hero file
import time
import random
class Hero:
    gold = 0
    def __init__(self, name, base_health, att_power, max_health, special):
        self.name = name
        self.base_health = base_health
        self.att_power = att_power
        self.max_health = max_health
        self.special = special
    def heal(self):
       """heal logic"""
       if self.base_health < self.max_health:
           self.base_health += self.max_health - self.base_health
           print(f"HEALED TO MAX HEALTH! CURRENT HEALTH: {self.base_health}")
       else:
           print('MAX HEALTH REACHED')
    def attack(self, target_enemy):
        """base player attack logic"""
        damage = random.randint(30, self.att_power)
        target_enemy.enm_health -= damage
        if target_enemy.enm_health > 0:            #so the user doesn't see negative health numbers
            print(f'YOU DEALT {damage} DAMAGE! ENEMY HEALTH: {target_enemy.enm_health}')
            time.sleep(1.5)
        else:
            print(f'YOU DEALT {damage} DAMAGE! ENEMY DEFEATED! REMAINING HEALTH = {self.base_health}')
            time.sleep(1.5)
    def is_alive(self):
        """helps in handling death"""
        return self.base_health > 0



