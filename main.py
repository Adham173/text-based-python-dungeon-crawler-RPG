# this is the main file
from hero import Hero
from enemy import Enemy
from classes import *
def main():
    choice1 = input('Would you like to start the game? (y/n)').capitalize()
    if choice1 == 'y':
       player = input('Welcome to the cave! Please pick a hero:')
       print('Heroes: Soldier---Berserker---Tank---Mage')

if __name__ == '__main__':
    main()