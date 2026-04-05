# This is the enemy file
import time
import random
class Enemy:
    turn_count = 0
    def __init__(self,enm_name, enm_health, enm_att_power):
        self.enm_name = enm_name
        self.enm_health = enm_health
        self.enm_att_power = enm_att_power
    def enm_att(self, target_player):
        """base enemy attack logic here"""
        enm_damage = random.randint(20, self.enm_att_power)
        target_player.base_health -= enm_damage
        if target_player.base_health > 0:     #so the user doesn't see negative health numbers
            print(f'YOU HAVE BEEN DEALT {enm_damage} DAMAGE. REMAINING HEALTH: {target_player.base_health}')
            self.turn_count += 1
        else:
            print(f'YOU HAVE BEEN DEALT {enm_damage} DAMAGE. YOU HAVE BEEN DEFEATED')
        time.sleep(1.5)
