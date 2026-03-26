import random
def the_second_game():
    def new_monster_generator():
        dice = random.randint(1,12)
        if dice == 1:
            monster = "skellaten"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "arrow_shot"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "call for backup" 
                monster_attack_dmg = 0

        if dice == 2:
            monster = "mummy"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "drain life" 
                monster_attack_dmg = 10

        if dice == 3:
            monster = "werewolf"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "claw swipe"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "howl" 
                monster_attack_dmg = 0
        if dice == 4:
            monster = "gargoyal"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "stone throw"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "petrify" 
                monster_attack_dmg = 10

        if dice == 5:
            monster = "Huldra"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "charm"
                monster_attack_dmg = 0
            elif attck_dice == 2:
                monster_attack = "claw swipe" 
                monster_attack_dmg = 5
        if dice == 6:
            monster = "Liche"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "dark magic"
                monster_attack_dmg = 10
            elif attck_dice == 2:
                monster_attack = "drain life" 
                monster_attack_dmg = 5
        if dice == 7:
            monster = "Gremlins"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "sabotage"
                monster_attack_dmg = 0
            elif attck_dice == 2:
                monster_attack = "bite" 
                monster_attack_dmg = 5
        if dice == 8:
            monster = "Wraiths"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "drain life"
                monster_attack_dmg = 10
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 5
        if dice == 9:
            monster = "Ghoul"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        if dice == 10:
            monster = "Revenants"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        if dice == 11:
            monster = "Cyclops"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            elif attck_dice == 2:
                monster_attack = "hit" 
                monster_attack_dmg = 10
        if dice == 12:
            monster = "Yeti"
            attck_dice = random.randint(1,2)
            if attck_dice == 1:
                monster_attack = "bite"
                monster_attack_dmg = 5
            monster_dice = random.randint(1, 6)
            if monster_dice == 13:
                monster_type = "witch"
                monster_health = 30
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "potion"
                    monster_attack_dmg = 15
                elif attack_dice == 2:
                    monster_attack = "heal" 
                    monster_attack_dmg = 0
            elif monster_dice == 14:
                monster_type = "goblin"
                monster_health = 20
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "kick"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "stab" 
                    monster_attack_dmg = 10
            elif monster_dice == 15:
                monster_type = "medusa"
                monster_health = 80
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "bite"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "paralyze" 
                    monster_attack_dmg = 10
            elif monster_dice == 16:
                monster_type = "minotaur"
                monster_health = 30
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "horse kick"
                    monster_attack_dmg = 5
                elif attack_dice == 2:
                    monster_attack = "charge" 
                    monster_attack_dmg = 10
            elif monster_dice == 17:
                monster_type = "cerberus"
                monster_health = 40
                attack_dice = random.randint(1,2)
                if attack_dice == 1:
                    monster_attack = "triple bite"
                    monster_attack_dmg = random.randint(1,15)
                elif attack_dice == 2:
                    monster_attack = "bite" 
                    monster_attack_dmg = 10
            elif monster_dice == 18:
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
    choice = input("welcom back travler our world is in distress agein and you will be the one to save it do you accept this quest (y/n)")
    if choice.lower() == "y":
        print("you are a brave hero saving us again")


    elif choice.lower() == "n":
        print("you are a coward!")
