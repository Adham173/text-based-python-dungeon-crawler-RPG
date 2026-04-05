# this is the classes file
import random
from hero import Hero
from enemy import Enemy
#hero classes:
berserker = Hero(name = 'Mage', hero_health = 40, att_power = 75)
tank = Hero(name = 'Tank', hero_health = 200, att_power = 50)
soldier = Hero(name = 'Soldier', hero_health = 60, att_power = 60)
class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, att_power = 45, hero_health = 60)
    def special_att (self, target_player, target_enemy):
        magic = 100
        if magic > 25:
            target_player.att_power = 125
            target_enemy.enm_health -= target_player.att_power
            print(f'YOU DEALT {target_player.att_power}! BOSS HEALTH = {target_enemy.enm_health}')
#enemy classes:
goblin = Enemy(enm_name = 'Goblin', enm_health = 50, enm_att_power = 50)
golem = Enemy(enm_name = 'Golem', enm_health = 500, enm_att_power = 75)
class Vampire(Enemy):
    def __init__(self, enm_name):
        super().__init__(enm_name, enm_health = 75, enm_att_power = 50)
    def health_steal(self, target_player):
        vamp_damage = random.randint(50, self.enm_att_power)
        target_player.hero_health -= vamp_damage
        self.enm_health += vamp_damage * 0.5
        print(f'YOU HAVE BEEN DEALT {vamp_damage} DAMAGE! '
              f"VAMPIRE HAS STOLEN {vamp_damage / 0.5} HEALTH FROM YOU! VAMPIRE"
              f'HEALTH {self.enm_health}')