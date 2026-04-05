# this is the main file
from classes import *
def slow_print(text, delay= 0.5):
    """helps create atmosphere"""
    print(text)
    time.sleep(delay)
def reset():
    """resets all objects stats"""
    registry = {
        knight: org_stats['knight'],
        berserker: org_stats['berserker'],
        tank: org_stats['tank'],
        Mage: org_stats['Mage'],
        spider: org_stats['spider'],
        statue: org_stats['statue'],
        goblin: org_stats['goblin'],
        vampire: org_stats['vampire'],
        treasure_keeper: org_stats['treasure_keeper'],
        skeleton: org_stats['skeleton'],
        wizard: org_stats['wizard'],
    }
    for obj, original_data in registry.items():
        obj.__dict__.update(original_data)
    Hero.gold = 0
    Enemy.turn_count = 0
    Mage.magic = 100
def battle(target_player, target_enemy):
    """all combat mechanics are compiled and used here"""
    while True:
        att_choice = input('PRESS ENTER FOR NORMAL ATTACK. PRESS E FOR SPECIAL ATTACK ').upper()
        if att_choice == 'E':
            target_player.special_att(target_enemy)
        else:
            target_player.attack(target_enemy)
        if target_enemy.enm_health > 0:
            if hasattr(target_enemy, 'health_steal'):
                target_enemy.health_steal(target_player)
            elif hasattr(target_enemy, 'spell_cast'):
                target_enemy.spell_cast(target_player)
            else:
                target_enemy.enm_att(target_player)
        else:
            break
        if target_player.is_alive(): #this statement handles death
            continue
        else:
            slow_print("You died...Going to main menu...", 4)
            main()
            
def main():
    while True:
        reset()
        start = input('Would you like to start the game? (y/n): ').lower()
        if start == 'y':
            print('Heroes: Knight---Berserker---Tank---Mage')
            hero_choice = input('Welcome to the dungeon! Please pick a hero: ').capitalize().strip()
            if hero_choice in heroes:
                player = heroes.get(hero_choice)   #extracting players hero choice from dictionary in hero file
            else:
                player = knight
                print('INVALID CHOICE. CHOOSING KNIGHT AS DEFAULT...')
            mimic = Mimic('Mimic', player)
            player.base_health = player.max_health
            slow_print(f'HERO: {player.name}')
            slow_print(f'BASE HEALTH = {player.base_health}')  # presenting players stats
            slow_print(f'ATT_POWER = {player.att_power}')
            slow_print(f'SPECIAL = {player.special}')
            slow_print("You enter a dark, spooky dungeon filled with monsters... and treasure.", 2)
            slow_print('You see three paths ahead of you, a forward wide path, a smaller path to '
                       "the right, and tight path to the left that you'd have to crawl through.", 3)
            while True:
                path_choice = input('\nWhich path do you choose, forward, right, or left? ').lower().strip()
                if path_choice == 'forward':
                    slow_print("You light your torch and go down the forward path...", 1)
                    slow_print("It's a very wide path and you start to feel exposed until...", 3)
                    slow_print('A wild spider appears!')
                    battle(player, spider)
                    slow_print(
                        'You survive your first encounter, and your strength has increased, but many dangers still await you...',
                        2)
                    player.att_power += 15
                    slow_print(
                        'After healing wandering for a few moments, you have another choice to make, which might be your last...',
                        2)
                    player.heal()
                    slow_print(
                        'The left path smells of gold and riches, while the right path smells of monsters and danger...',
                        2)
                    while True:
                        forward_choice = input('Which path do you choose... left or right? ').lower().strip()
                        if forward_choice == 'left':
                            slow_print("After pondering over your decision, you decide to go down the left path...", 5)
                            slow_print('After what feels like hours you finally see it, the treasure room...', 2)
                            slow_print('You enter the room and as you are just about to pick up a gold coin...', 1.5)
                            slow_print('The treasure keeper appears!!')
                            battle(player, treasure_keeper)
                            slow_print(
                                'You have defeated the treasure keeper and get to enjoy the treasure you have earned. Congratulations!', )
                            player.gold += 500
                            print(
                                f'FINAL STATS: HEALTH: {player.base_health}  STRENGTH: {player.att_power}  WEALTH: {player.gold}')
                            slow_print('Returning to main menu...', 2)
                            main()
                        elif forward_choice == 'right':
                            slow_print("After pondering over your decision, you decide to go down the right path...", 3)
                            slow_print(
                                'After wondering for a few minutes, you encounter a strange looking statue guarding a chest...',
                                2)
                            slow_print('You go to open the chest and then suddenly...', 3.5)
                            slow_print('The statue awakens and attacks you!!')
                            battle(player, statue)
                            slow_print('You have defeated the statue. Congratulations!')
                            slow_print('You take a second to heal and then go to open the chest and then suddenly...',
                                       3.5)
                            player.heal()
                            slow_print('A goblin jumps out of the chest and attacks you!')
                            battle(player, goblin)
                            slow_print('You have defeated the goblin and your strength has increased greatly!', 2)
                            player.att_power += 50
                            slow_print(
                                "You check what's in the chest and discover that all that's in are a couple silver coins..",
                                3)
                            player.gold += 50
                            slow_print('You leave the cave disappointed...')
                            print(
                                f'FINAL STATS: HEALTH: {player.base_health}  STRENGTH: {player.att_power}  WEALTH: {player.gold}')
                            slow_print('Returning to main menu...', 2)
                            main()
                        else:
                            print('INVALID CHOICE. TRY AGAIN!')
                elif path_choice == 'left':
                    slow_print('You light your torch and go down the left path...', 4)
                    slow_print(
                        "It's a very tight crawl but after what feels like forever you reach a wide open area...", 2)
                    slow_print(
                        'This room looks safe so you take a minute stretch your legs but then you hear some weird footsteps and...',
                        3)
                    slow_print('A skeleton attacks you!!')
                    battle(player, skeleton)
                    slow_print(
                        'You survive your first encounter, and your strength has increased, but many dangers still await you...',
                        2)
                    player.att_power += 20
                    slow_print(
                        "After wandering around the large room you discover that there's no treasure here, but a choice to make, "
                        "which might be your last...", 3)
                    slow_print('Beyond you are two staircases, one going upstairs, and one going downstairs.', 1)
                    slow_print('The upstairs staircase looks very fancy and it may lead to a bedroom, '
                               'the downstairs staircase looks like it leads to basement.')
                    while True:
                        left_choice = input('Which do you choose? Upwards or downwards? ').lower().strip()
                        if left_choice == 'upwards':
                            slow_print('You decide to go upwards towards the bedroom...', 3)
                            slow_print("The staircase seems like it goes forever until you finally reach the bedroom.",
                                       2)
                            slow_print(
                                "The room looks massive and has multiple chests and you assume it's empty so you decide to "
                                "go open one of the chests when...", 3.5)
                            slow_print('A Vampire emerges out of the bed and attacks you!!')
                            battle(player, vampire)
                            slow_print(
                                'You have defeated the vampire and get to enjoy all the treasures in the bedroom. Congratulations!')
                            player.gold += 100
                            player.att_power += 30
                            print(
                                f'FINAL STATS: HEALTH: {player.base_health}  STRENGTH: {player.att_power}  WEALTH: {player.gold}')
                            slow_print('Returning to main menu...', 2)
                            main()
                        elif left_choice == 'downwards':
                            slow_print('You decide to go downwards towards the basement...', 3)
                            slow_print("The staircase seems like it goes forever until you finally reach the basement.",
                                       2)
                            slow_print('The basement gives you an eerie feeling as there are bones and webs everywhere',
                                       3)
                            slow_print(
                                "You notice a weird robotic skeleton on the ground, it look's dead so you let your "
                                "guard down then suddenly...", 2.5)
                            slow_print('The robot comes to life and becomes a mimic and it attacks you!!', 1)
                            battle(player, mimic)
                            slow_print("After surviving that encounter you search everywhere in the dungeon for wealth "
                                       "and discover very valuable gem!", 3)
                            player.gold += 50
                            slow_print(
                                "It's not much but you are happy with it and leave the dungeon accomplished. Congratulations!")
                            print(
                                f'FINAL STATS: HEALTH: {player.base_health}  STRENGTH: {player.att_power}  WEALTH: {player.gold}')
                            slow_print('Returning to main menu...', 2)
                            main()
                        else:
                            print('INVALID CHOICE. TRY AGAIN!')
                elif path_choice == 'right':
                    slow_print('You light your torch and go down the right path...', 3)
                    slow_print("The path is kind of narrow but still wide enough so you don't get claustrophobic.", 2)
                    slow_print(
                        'After wandering for a few moments you hear faint footsteps behind you so you look back and...',
                        3)
                    slow_print('A goblin attacks you!!')
                    battle(player, goblin)
                    slow_print(
                        "You survive the first encounter, and you pick up a shield from the goblin which benefits"
                        "your defense, but many dangers still await you...", 3)
                    player.heal()
                    player.base_health += 25
                    slow_print('After wondering for few minutes you find a scroll and read it.', 1.5)
                    slow_print(
                        'The scroll talks about a wealthy evil wizard living in the depths of the dungeon in a basement...',
                        1.5)
                    slow_print('As you continue to wander you find a bag of gold coins!', 3.5)
                    player.gold += 75
                    slow_print(
                        "After what felt like hours you finally stumble upon a trapdoor which leads to a basement", 1.5)
                    slow_print(
                        "You know this is probably the basement the scroll was talking about. And you have a big decision to make...",
                        2)
                    slow_print(
                        "You can either leave the dungeon now with the riches you already have, or face the wizard"
                        " with the promise of great wealth if you defeat him.", 3)
                    while True:
                        right_choice = input('What would you like to do? Fight or leave? ').lower().strip()
                        if right_choice == 'leave':
                            slow_print('You leave the dungeon with the riches you already have...', 2)
                            print(
                                f'FINAL STATS: HEALTH: {player.base_health}  STRENGTH: {player.att_power}  WEALTH: {player.gold}')
                            slow_print('Returning to main menu...', 2)
                            main()
                        elif right_choice == 'fight':
                            slow_print('You choose to fight the wizard...', 2)
                            slow_print('You open the trapdoor and enter the basement and you feel like your heart is '
                                       'beating out of your chest, but you continue...', 4)
                            slow_print(
                                'The basement looks empty and you start to think that the scroll was either fake or the '
                                'wizard is dead, then suddenly...', 3)
                            slow_print('The wizard emerges from the dark and attacks you!!')
                            battle(player, wizard)
                            slow_print(
                                "You have defeated the evil wizard and enjoy the great riches that were promised to you. Congratulations!",
                                1.5)
                            player.gold += 200
                            print(
                                f'FINAL STATS: HEALTH: {player.base_health}  STRENGTH: {player.att_power}  WEALTH: {player.gold}')
                            slow_print('Returning to main menu...', 2)
                            main()
                        else:
                            print('INVALID CHOICE TRY AGAIN!')
                else:
                    print('INVALID CHOICE TRY AGAIN!')


    else:
        exit()
if __name__ == '__main__':
    main()
