# Python OOP Dungeon Crawler 1.0

### Project Overview
This is a multi-file, text-based RPG engine developed from scratch. This project focuses on **OOP principles** and utilizes dynamic memory management to handle game states, character inheritance, and unique boss/player mechanics.

### Key Features
1. **State Persistence & Factory Reset:**
This game features a universal reset system using Python's `__dict__` attribute in order to reset global objects to their original states at the start of every game loop. 

2. **Class Inheritance & Polymorphism:**
* **Hero Base Class:** Manages gold, healing logic, and basic combat.
* **Specialized Subclasses:** The `Mage` class overrides the standard attack pattern to implement a magic resource management system.
* **Enemy AI:** Includes specialized classes like the `Vampire` (Health Steal) and `Wizard` (Turn-based debuffing).

3. **Dynamic Entity Scaling (The Mimic):**
The `Mimic` class is an exercise in **Dynamic Initialization**. It does not have fixed stats; instead, it clones the `max_health` and `att_power` of the specific `Hero` instance at the moment of creation.

### File Structure
* `main.py`: The central execution hub and game loop logic.
* `classes.py`: The "Circuit Board" where all Hero and Enemy instances are wired together.
* `hero.py`: The Blueprint for player characters.
* `enemy.py`: The Blueprint for monster entities and AI behaviors.

### How to Run
1. Clone this repository or download all 4 `.py` files into a single directory.
2. Run the command: `python main.py`
3. Choose your Hero and try to survive the dungeon!
