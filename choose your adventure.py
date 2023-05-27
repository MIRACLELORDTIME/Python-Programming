print("Notice: Type the keyword correctly which present in the quotes.\n")
while(1):
    start=input("Press 'Enter' to continue:")
    if start == "Enter":
        name=input("Enter your name:")
        print("Welcome",name,"to this adventure spot!\n")
        print("You are at the centre of the jungle.\n ")
        print("Now in which direction you want to move?\n")

    answer=input("Left or Right:")

    if answer == "Left":
        print("You turned Left now , before you there is a path and then there is a river.\n")

        left_1=input("What you want to do , Have a walk in the path type 'Walk' or Swim in the river type 'Swim' :")

        if left_1 == "Walk":
            print("You have walked a long way without food and water.\n")

            decide=input("What you want to do Search for food and water type 'Search' or continue walking to get out of the jungle type 'Continue':")
            if decide == "Search":
                print("You found a nice fruit.What you want to do now...?\n")

                decide_1=input("Are you going to eat that fruit type 'Eat' or throw it away and look for another type 'Another':")
                if decide_1 == "Eat":
                    print("You ate some poisonous food. So, You are died.")

                elif decide_1 == "Another":
                    print("You died out of hunger. You lose.")

                else:
                    print("Please enter a valid input.\n")

            elif decide == "Continue":
                print("Tou enountered an bear infront of you.\n")

                decide_2=input("What you want to do. Are you going to face it and try to scare it away type 'Face' or Are you going to give up and run away type 'Run'...?:")
                if Face == "Face":
                    print("You managed to confront and win against the bear, but you weakened yourself by not eating properly.So you died.")

                elif Run == "Run":
                    print("You made a mistake by trying to run away from the bear instead of confronting it. So, you died. You lose.")

                else:
                    print("Please enter the valid input.")

            else:
                print("Please enter the valid input.\n")

                    
                    
        elif left_1 == "Swim":
            print("You swimming sweetly suddenly you noticed an alligator is coming near to you. What do you want to do now.\n")

            left_2=input("swim fastly and get to sealand quickly type 'Get to sealand' or turn into food of alligator type 'Turn into food': ")

            if left_2 == "Get to sealand":
                print("You drained out of energy and drank lot of water so, after 3 hours you died !!. You Lose\n ")

            elif left_2 == "Turn into food":
                print("You died. So, You Lose\n ")

            else:
                print("Please enter a valid input. So, You lose.\n")

        else:
            print("Please enter a valid input. So, You lose.\n")

    elif answer == "Right":
        print("You turned Right now , Before you a there is a dirty field and then there is a place where some screaming sound of animals are coming !!!.\n")

        jungle_1=input("What you want to do, Move towards the dirty field type 'Move to field' or Move towards the place where some screaming sound of animals are coming type 'Move towards the place' :")

        if jungle_1 == "Move to field":
            print("You got stuck in a sinkhole.Try to get back by from it \n")

            right_1=input("What do you want to do? , get back by pulling any object type 'Get back'or sink in the sinkhole type 'Sink':")

            if right_1 == "Get back":
                print("Mistakenly you pulled the tail of the snake. It bitten you. So, you died. You lose.\n ")

            elif right_1 == "Sink":
                print("You are died by sinking in the sinkhole. You lose.\n")

            else:
                print("Please enter a valid input. So, You lose\n")

        elif jungle_1 == "Move towards the place":
            print("You are witnessing a Hyena which is on hunger for 3 days. It sees and coming towards you.\n")

            right_2=input("What you want to do , Search for a weapon and attack it type 'Attack' or Try to escape by running away from it type 'Escape':")

            if right_2 == "Attack":
                print("By using a sharp wooden branch as a weapon , You killed the hyena.\n")
                print("Since you killed the animal you are literally on tired.\n")

                branch_1=input("What you want to do. Search for some food type 'Search' or find the way to get out from the jungle type 'Find': ")

                if branch_1 == "Search":
                    print("When you are looking for food , you get caught by an unknown animal and you died. so, You lose.\n")

                elif branch_1 == "Find":
                    print("When you are finding the way , You found some stranger roming around!!!\n")

                    branch_2=input("What you want to do , Get his help to get out from this jungle type 'Help' or Move away as you didn't see him type 'Move Away' ")

                    if branch_2 == "Help":
                        print("YOU WON , With his help you have come through the forest!!!.\n")
                        break;

                    elif branch_2 == "Move Away":
                        print("When you move away from him , he looked you by chance. He thought an animal is moving around. You was killed by the him by his gun , as he is a hunter. So, You lose.\n")

                    else:
                        print("Please Enter a valid input. So, You Lose.\n")

            elif right_2 == "Escape":
                print("You can't run faster than a Hyena to escape , so you get caught by the Hyena and you died. So, You lose.\n ")

            else:
                print("Please Enter a valid input. So, You Lose.\n")

    else:
        print("Please Enter a valid input. So, You Lose.\n")

else:
    ("Please enter a valid input. So, You lose.\n")

    
    
