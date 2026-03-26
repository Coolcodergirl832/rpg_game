import random
from CAC import cheatcode

def the_second_game():

    def Choose_species():
        player_health = 100
        player_species = input("What is your species type? (a) troll, (b) orc, (c) vampire, (d) human: ")
        if player_species.lower() == 'a':
            print("You have chosen to be a troll, you are strong but slow.")
            attacks = ["club smash", "ground pound", "troll roar"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "troll"
        elif player_species.lower() == 'b':
            print("You have chosen to be an orc, you are fierce and powerful but not very smart.")
            attacks = ["smash", "roar", "charge"]
            dmg1, dmg2, dmg3 = 5, 10, 15
            species = "orc"
        elif player_species.lower() == 'c':
            print("You have chosen to be a vampire, you are fast and durable but are vulnerable to sunlight.")
            attacks = ["shriek", "bite", "blood drain"]
            dmg1, dmg2, dmg3 = 15, 5, 10
            species = "vampire"
        elif player_species.lower() == 'd':
            print("You have chosen to be a human, you are balanced and versatile but not durable.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "human"
        else:
            print("Invalid choice! species has been set to human by default.")
            attacks = ["slash", "stab", "punch"]
            dmg1, dmg2, dmg3 = 10, 15, 5
            species = "human"

        return (species, attacks, dmg1, dmg2, dmg3)

    def new_monster_generator():
        dice = random.randint(1,18)

        # DEFAULTS so the return never crashes
        monster_type = "unknown"
        monster_health = random.randint(10,50)
        monster_attack = "hit"
        monster_attack_dmg = 5

        if dice == 1:
            monster_type = "skellaten"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "arrow_shot"
                monster_attack_dmg = 5
            else:
                monster_attack = "call for backup"
                monster_attack_dmg = 0

        elif dice == 2:
            monster_type = "mummy"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "drain life"
                monster_attack_dmg = 10

        elif dice == 3:
            monster_type = "werewolf"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "claw swipe"
                monster_attack_dmg = 5
            else:
                monster_attack = "howl"
                monster_attack_dmg = 0

        elif dice == 4:
            monster_type = "gargoyal"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "stone throw"
                monster_attack_dmg = 5
            else:
                monster_attack = "petrify"
                monster_attack_dmg = 10

        elif dice == 5:
            monster_type = "Huldra"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "charm"
                monster_attack_dmg = 0
            else:
                monster_attack = "claw swipe"
                monster_attack_dmg = 5

        elif dice == 6:
            monster_type = "Liche"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "dark magic"
                monster_attack_dmg = 10
            else:
                monster_attack = "drain life"
                monster_attack_dmg = 5

        elif dice == 7:
            monster_type = "Gremlins"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "sabotage"
                monster_attack_dmg = 0
            else:
                monster_attack = "bite"
                monster_attack_dmg = 5

        elif dice == 8:
            monster_type = "Wraiths"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "drain life"
                monster_attack_dmg = 10
            else:
                monster_attack = "hit"
                monster_attack_dmg = 5

        elif dice == 9:
            monster_type = "Ghoul"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 10:
            monster_type = "Revenants"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 11:
            monster_type = "Cyclops"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 12:
            monster_type = "Yeti"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        elif dice == 13:
            monster_type = "witch"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "potion"
                monster_attack_dmg = 15
            else:
                monster_attack = "heal"
                monster_attack_dmg = 0

        elif dice == 14:
            monster_type = "goblin"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "kick"
                monster_attack_dmg = 5
            else:
                monster_attack = "stab"
                monster_attack_dmg = 10

        elif dice == 15:
            monster_type = "medusa"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "paralyze"
                monster_attack_dmg = 10

        elif dice == 16:
            monster_type = "minotaur"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "horse kick"
                monster_attack_dmg = 5
            else:
                monster_attack = "charge"
                monster_attack_dmg = 10

        elif dice == 17:
            monster_type = "cerberus"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "triple bite"
                monster_attack_dmg = random.randint(1,15)
            else:
                monster_attack = "bite"
                monster_attack_dmg = 10

        elif dice == 18:
            monster_type = "zombie"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            else:
                monster_attack = "hit"
                monster_attack_dmg = 10

        return monster_type, monster_health, monster_attack, monster_attack_dmg

    choice = input("welcom back travler our world is in distress agein and you will be the one to save it do you accept this quest (y/n)")

    if choice.lower() == "y":
        player_health = 100
        fight_count = 0

        species, attacks, dmg1, dmg2, dmg3 = Choose_species()

        while player_health > 0:

            fight_count += 1

            # --- YOUR SPECIAL FIGHT COUNT CHECKS ---
            if fight_count % 5 == 0:
                print("A boss approaches! (placeholder)")
            elif fight_count % 10 == 0:
                print("A stronger boss appears! (placeholder)")
            elif fight_count % 15 == 0:
                print("A mega boss appears! (placeholder)")
            elif fight_count % 20 == 0:
                print("A legendary boss appears! (placeholder)")
            elif fight_count % 25 == 0:
                print("A mythical boss appears! (placeholder)")
            elif fight_count % 30 == 0:
                print("THE FINAL BOSS APPEARS! (placeholder)")
            else:
                # Normal monster encounter
                monster_type, monster_health, monster_attack, monster_attack_dmg = new_monster_generator()
                input(f"You have encountered a {monster_type} with {monster_health} HP!")
                attack_choice = input(f"what do you do coose a attack from the following list {attacks}")
                if attack_choice.lower() == "shriek":
                    pass
                elif attack_choice.lower() == "bite":
                    pass
                elif attack_choice.lower() == "blood drain":
                    pass
                elif attack_choice.lower() == cheatcode:#no peaking for the cheat code in this code
                    monster_health =0
                    fight_count = 30
                    print(fight_count)
                    break




    elif choice.lower() == "n":
        print("you are a coward!")

the_second_game()