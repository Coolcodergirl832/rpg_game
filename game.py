import random

while True:
    player_name = input("What is your name, traveler? ")
    player_health = 100
    fight_count = 0
    player_skill_points = 0
    def monster_dice_roll():
        monster_dice = random.randint(1, 6)
        if monster_dice == 1:
            monster_type = "witch"
            monster_health = 30
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "potion"
                monster_attack_dmg = 15
            elif attack_dice == 2:
                monster_attack = "heal" 
                monster_attack_dmg = 0
        elif monster_dice == 2:
            monster_type = "gobilin"
            monster_health = 20
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "kick"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "stab" 
                monster_attack_dmg = 10
        elif monster_dice == 3:
            monster_type = "midusa"
            monster_health = 80
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "parilize" 
                monster_attack_dmg = 10
        elif monster_dice == 4:
            monster_type = "minitar"
            monster_health = 30
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "horse kick"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "charge" 
                monster_attack_dmg = 10
        elif monster_dice == 5:
            monster_type = "cyeribis"
            monster_health = 40
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "triple bite"
                monster_attack_dmg = random.randint(1,15)
            elif attack_dice == 2:
                monster_attack = "bite" 
                monster_attack_dmg = 10
        elif monster_dice == 6:
            monster_type = "zombie"
            monster_health = 10
            attack_dice = random.randint(1,2)
            if attack_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attack_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        
        return (monster_type,monster_health,monster_attack,monster_attack_dmg)
    
    def Chosse_spices():
        player_spices = input("What is your species type? (a) troll, (b) org, (c) vampire, (d) human: ")
        if player_spices.lower() == 'a':
            print("You have chosen to be a troll, you are strong but slow.")
            attacks = ["club smash", "ground pound", "troll roar"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "troll"
        elif player_spices.lower() == 'b':
            print("You have chosen to be an org, you are fierce and powerful but not very smart.")
            attacks = ["smash", "roar", "charge"]
            dmg1, dmg2, dmg3 = 5, 10, 15
            spices = "org"
        elif player_spices.lower() == 'c':
            print("You have chosen to be a vampire, you are fast and durable but are vulnerable to sunlight.")
            attacks = ["shriek", "bite", "blood drain"]
            dmg1, dmg2, dmg3 = 15, 5, 10
            spices = "vampire"
        elif player_spices.lower() == 'd':
            print("You have chosen to be a human, you are balanced and versatile but not durable.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "human"
        else:
            print("Invalid choice! spices has been set to human by default.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            spices = "human"
        
        # Return all 5 values as a tuple
        return (spices, attacks, dmg1, dmg2, dmg3)

    choice = input(f"Welcome {player_name}, you have been chosen to be the hero of this world. Do you accept? (y/n) ")
    
    if choice.lower() == 'y':
        # FIX: We must "unpack" the 5 things the function returns into 5 variables
        player_spices, current_attacks, attack1_dmg, attack2_dmg, attack3_dmg = Chosse_spices()

        print(f"Great! {player_name} the {player_spices}, your adventure begins now.")
        
        input("""How this game will work: when you defeat a monster you gain skill points...
              (Press Enter to continue)""")
        
        choice = input("Are you ready to start your adventure? (y/n) ")
        if choice.lower() == 'y':
            print("Let's begin!")
            
            # Start the game loop here
            while player_health > 0:
                fight_count += 1
                if fight_count % 3 == 0:
                    # Boss battle
                    monster_type = "BOSS"
                    monster_health = 100
                    monster_attack = "power strike"
                    monster_attack_dmg = 30

                else:
                    monster_type, monster_health, monster_attack, monster_attack_dmg = monster_dice_roll()
                
                input(f"""You encounter a {monster_type}! It has {monster_health} health and uses {monster_attack} that 
                      does {monster_attack_dmg} damage. (Press Enter to continue)""")
                cooldowns = [0, 0, 0]
                while monster_health > 0 and player_health > 0:
                    for i in range(3):
                        if cooldowns[i] > 0:
                            cooldowns[i] -= 1
                    choice = input(f"What attack will you use? (1) {current_attacks[0]}{' (cooldown: ' + str(cooldowns[0]) + ')' if cooldowns[0] > 0 else ''} (2) {current_attacks[1]}{' (cooldown: ' + str(cooldowns[1]) + ')' if cooldowns[1] > 0 else ''} (3) {current_attacks[2]}{' (cooldown: ' + str(cooldowns[2]) + ')' if cooldowns[2] > 0 else ''} ")
                    if choice == '1' and cooldowns[0] == 0:
                        monster_health -= attack1_dmg
                        print(f"You used {current_attacks[0]} and did {attack1_dmg} damage! The {monster_type} now has {monster_health} health.")
                        cooldowns[0] = 2
                    elif choice == '2' and cooldowns[1] == 0:
                        monster_health -= attack2_dmg
                        print(f"You used {current_attacks[1]} and did {attack2_dmg} damage! The {monster_type} now has {monster_health} health.")
                        cooldowns[1] = 2
                    elif choice == '3' and cooldowns[2] == 0:
                        monster_health -= attack3_dmg
                        print(f"You used {current_attacks[2]} and did {attack3_dmg} damage! The {monster_type} now has {monster_health} health.")
                        cooldowns[2] = 2
                    else:
                        print("Invalid choice or attack on cooldown!")
                    if monster_health <= 0:
                        print(f"You defeated the {monster_type}! You gain skill points.")
                        player_skill_points += 1
                        print(f"Skill points: {player_skill_points}")
                        choice = input("Would you like to go to the shop to buy upgrades? (Press Enter to continue (y/n)) ")
                        if choice.lower() == 'y':
                            print("You head to the shop...")
                            upgrade_choice = input("""What would you like to upgrade? (1) 10 hp cost: 5 skill points 
                                                   (2) Attack strength upgrade, cost: 10 skill points
                                                    (3) New attack cost:20 skill points """)
                        break
                    player_health -= monster_attack_dmg
                    print(f"The {monster_type} used {monster_attack} and did {monster_attack_dmg} damage! You now have {player_health} health.")
                    if player_health <= 0:
                        print("You have been defeated! Game over.")
                        break
                

    elif choice.lower() == 'n':
        print("Perhaps another time.")
        break
    else:
        print("Please enter 'y' or 'n'.")