import random
import time

character_health = 100
fish = 0
# possible dungeon loot
bronze_sword = 0
iron_sword = 0
gold = 0
broad_sword = 0
stick = 0
food = 0

name = input("Enter your name: ")
print("Hello " + name + "\n")

while character_health > 0:
    if character_health != 100:
        print("You have taken some damage, choose 4 to gain some health back")

    # chose a journey
    chosen_journey = (input(
        "Choose 1 if you want to cross the river\n"
        "Choose 2 if you want to jump on the ravine\n"
        "Choose 3 if you want to fight monster in the dungeon\n"
        "Choose 4 if you want to consume fish and gain some health back\n"
        "Choose 5 if you want to check your item loot from the dungeon\n"
        "Input: "))
    # cross river
    if chosen_journey == '1':
        # ask the user for fishing
        choice = input("If you want to go fishing select [1 for yes/ 0 for no]")
        # fishing
        if choice == "1":
            print("You have chosen Fishing!")
            # chance to catch a fish
            chance = random.randint(0, 9)
            if chance > 4:
                print("You have catch a Fish!")
                fish += 1
                print("Your fish in your inventory is " + str(fish))
            else:
                print("There is no fish to catch")
                print("The fish in your inventory is " + str(fish))
        else:
            print("You have crossed the river")
    # suicide game ewan ko ba sa trip ng prof mo xD
    elif chosen_journey == '2':
        # damages the player
        print("You have jumped into the ravine")
        character_health -= 10
        print("Your character has taken damage, your current health is " + str(character_health))
    # journey inside the dungeon
    elif chosen_journey == '3':
        print("You have enter the dungeon")
        # randomly select a monster
        monster = ['zombie', 'skeleton', 'goblin', 'witch', 'ogre']
        chosen_monster = random.choice(monster)
        print('You have encountered a monster, ' + chosen_monster)

        # stats of the monster
        print(chosen_monster)
        if chosen_monster == 'ogre':
            monster_health = 60
            monster_attack = 6
        elif chosen_monster == 'zombie':
            monster_health = 55
            monster_attack = 7
        elif chosen_monster == 'skeleton':
            monster_health = 50
            monster_attack = 8
        elif chosen_monster == 'goblin':
            monster_health = 45
            monster_attack = 9
        elif chosen_monster == 'witch':
            monster_health = 40
            monster_attack = 10

        # battle system
        while monster_health > 0:
            character_attack = random.randint(5, 15)
            print('You have dealt ' + str(character_attack) + 'pts of damage')
            monster_health = monster_health - character_attack
            character_health = character_health - monster_attack
            time.sleep(1.5)
            print('You have received damage your current health is ' + str(character_health))
            time.sleep(1.5)
            if monster_health <= 0:
                print('You defeated the monster')
                dungeon_loot = ['bronze sword', 'iron sword', 'gold', 'broad sword', 'stick', 'food']
                drop_loot = random.choice(dungeon_loot)
                print('You received an item, ' + drop_loot)
                if drop_loot == 'bronze sword':
                    bronze_sword += 1
                elif drop_loot == 'iron sword':
                    iron_sword += 1
                elif drop_loot == 'gold':
                    gold += 1
                elif drop_loot == 'broad sword':
                    broad_sword += 1
                elif drop_loot == 'stick':
                    stick += 1
                elif drop_loot == 'food':
                    food += 1
                break
    elif chosen_journey == '4':
        # heal and consume fish
        if fish != 0:
            character_health +=10
            print("You gain some health, your current health is " + str(character_health))
            fish -= 1
            print("Your remaining fish is " + str(fish))
        else:
            print("You don't have fish in your inventory, go catch some")
    elif chosen_journey == '5':
        # damages the player
        print('This is the item in your inventory')
        print('Broad Sword: ' + str(broad_sword))
        print('Bronze Sword: ' + str(bronze_sword))
        print('Iron Sword: ' + str(iron_sword))
        print('Food: ' + str(food))
        print('Stick: ' + str(stick))
        print('Gold: ' + str(gold))
    else:
        print("Invalid input")

print("Your Character is dead!")