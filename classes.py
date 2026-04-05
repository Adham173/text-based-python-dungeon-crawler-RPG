
# this is the classes file. hero and enemy logic compiled here
import random
import time
from hero import Hero
from enemy import Enemy
#hero classes:
berserker = Hero(name = 'Berserker', base_health = 80 , max_health = 80,att_power = 100,special = None)
tank = Hero(name = 'Tank', base_health = 200, max_health = 200, att_power = 55,special = None)
knight = Hero(name = 'Knight', base_health = 120, max_health = 120 ,att_power = 65, special = None)
class Mage(Hero):
    def __init__(self, name):
        super().__init__(name, base_health = 90, max_health = 90 ,att_power = 60,special = 'MAGIC BOOSTER')
        self.magic = 100
    def special_att (self, target_enemy):
        """for mages special ability. player only allowed to use it 3 times every round"""
        if self.magic > 33:
            self.att_power = 100
            magic_damage = random.randint(50, self.att_power)
            target_enemy.enm_health -= magic_damage
            self.magic -= 33
            if target_enemy.enm_health > 0:         #so the user doesn't see negative health numbers
                print(f'YOU DEALT {magic_damage} DAMAGE! ENEMY HEALTH = {target_enemy.enm_health}')
            else:
                print(f'YOU DEALT {magic_damage} DAMAGE! ENEMY DEFEATED! REMAINING HEALTH: {self.magic}')
        else:
            print('Not enough magic! Using default attack...')
            time.sleep(1.5)
            self.attack(target_enemy)
heroes = {'Knight': knight, 'Berserker': berserker, 'Tank': tank, 'Mage': Mage('Mage')}    #helps extract users hero choice
#enemy classes:
class Vampire(Enemy):
    """Vampire logic here"""
    def __init__(self, enm_name):
        super().__init__(enm_name, enm_health = 105, enm_att_power = 50)
    def health_steal(self, target_player):
        vamp_damage = random.randint(30, self.enm_att_power)
        target_player.base_health -= vamp_damage
        self.enm_health += vamp_damage * 0.5
        if target_player.base_health > 0:          #so the user doesn't see negative health numbers
            print(f'YOU HAVE BEEN DEALT {vamp_damage} DAMAGE! VAMPIRE HAS STOLEN {vamp_damage * 0.5} HEALTH FROM YOU! '
                  f'VAMPIRE HEALTH: {self.enm_health}')
        else:
            print(f'YOU HAVE BEEN DEALT {vamp_damage} DAMAGE! VAMPIRE HAS STOLEN {vamp_damage * 0.5} HEALTH FROM YOU! '
                  'YOU HAVE BEEN DEFEATED')
        time.sleep(1.5)
class Mimic(Enemy):
    def __init__(self, enm_name, target_player):
        super().__init__(enm_name, enm_health = target_player.max_health, enm_att_power = target_player.att_power)
class Wizard(Enemy):
    def __init__(self, enm_name):
        super().__init__(enm_name, enm_health = 150, enm_att_power = 40)
    def spell_cast(self, target_player):
        """wizard spell lowers players strength on the third turn"""
        if self.turn_count == 2:
            target_player.att_power -= 35
            print('THE WIZARD HAS CAST A SPELL ON YOU. PERMANENTLY DECREASED STRENGTH')
        self.enm_att(target_player)

goblin = Enemy(enm_name = 'Goblin', enm_health = 105, enm_att_power = 75)
statue = Enemy(enm_name = 'Golem', enm_health = 200, enm_att_power = 25)
spider = Enemy(enm_name = 'Spider', enm_health = 60, enm_att_power = 40)
skeleton = Enemy(enm_name = 'Skeleton', enm_health = 65, enm_att_power = 75)
treasure_keeper = Enemy(enm_name = 'Treasure Keeper', enm_health = 150, enm_att_power = 95)
vampire = Vampire('Vampire')
wizard = Wizard('Wizard')
#mimic object must be made in main file as it depends on the player object
org_stats = {
    'goblin': goblin.__dict__.copy(),
    'spider': spider.__dict__.copy(),
    'statue': statue.__dict__.copy(),
    'skeleton': skeleton.__dict__.copy(),
    'treasure_keeper': treasure_keeper.__dict__.copy(),         #this dict is used in reseting object stats
    'vampire': vampire.__dict__.copy(),
    'wizard': wizard.__dict__.copy(),
    'knight': knight.__dict__.copy(),
    'berserker': berserker.__dict__.copy(),
    'tank': tank.__dict__.copy(),
    'mage': Mage.__dict__.copy(),
}
