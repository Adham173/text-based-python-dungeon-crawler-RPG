#  Python OOP Dungeon Crawler: Version 1.0

## Project Overview
This is a multi-file, text-based RPG engine developed from scratch. The project focuses on **Object-Oriented Programming (OOP)** principles to create a scalable and modular game environment. 

Unlike standard tutorials, this engine utilizes dynamic memory management to handle game states, character inheritance, and unique boss mechanics.

---

##  Key Engineering Features

# 1. State Persistence & Factory Reset
The game features a **Universal Reset System** using Python’s `__dict__` attribute. 
* **The Problem:** Global objects in Python retain their modified states (health/attack) across loop iterations.
* **The Solution:** A `registry` system that "snapshots" the birth-stats of every entity and force-restores them using `.update()` at the start of each run. This ensures a "Clean Boot" every time.

# 2. Class Inheritance & Polymorphism
* **Hero Base Class:** Manages gold, healing logic, and basic combat.
* **Specialized Subclasses:** The `Mage` class overrides the standard attack pattern to implement a `magic` resource management system.
* **Enemy AI:** Includes specialized classes like the `Vampire` (Health Steal logic) and `Wizard` (Turn-based debuffing).

# 3. Dynamic Entity Scaling (The Mimic)
The `Mimic` class is an exercise in **Dynamic Initialization**. It does not have fixed stats; instead, it clones the `max_health` and `att_power` of the specific `Hero` instance at the moment of encounter.

---

##  File Structure
* `main.py`: The central execution hub and game loop logic.
* `classes.py`: The "Circuit Board" where all Hero and Enemy instances are wired together.
* `hero.py`: The Blueprint for player characters.
* `enemy.py`: The Blueprint for monster entities and AI behaviors.

---

##  How to Run
1. Clone this repository or download all 4 `.py` files into a single directory.
2. Run the command: `python main.py`
3. Choose your Hero and try to survive the Wizard's basement!
