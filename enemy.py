# This is the enemy file
import random
class Enemy:
    def __init__(self,enm_name, enm_health, enm_att_power):
        self.enm_name = enm_name
        self.enm_health = enm_health
        self.enm_att_power = enm_att_power

    def enm_att(self, enm_name, target_player):
        enm_damage = random.randint(25, enm_name.enm_att_power)
        target_player.hero_health -= enm_damage
        print(f'YOU HAVE BEEN DEALT {enm_damage} DAMAGE. REMAINING HEALTH: {target_player.hero_health}')
