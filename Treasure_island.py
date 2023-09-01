print("Welcome to treasure island! Your mission is to find the treasure.")


print("You start your journey in a forest on the cusp of dusk.")
direction = input("You come to a fork in the path, do you go left or right?\n")

if direction == "left":
    print("You go down the left path, wondering what might have happened if you had chosen the right.")
    
    print("You come to a lake, and a rather large on at that, but there is a small dock on it.")
    print("Across the lake you see the shadowy outlines of a house")
    swim_or_wait = input("You could either wait out your time and see if someone comes for you, or you can swim. What do you choose?\n")

    if swim_or_wait == "wait":
        print("Patience is a virtue, and it certainly paid off this time, a strange man appears from the darkness in a boat, and he takes you across to the house.")

        print("The strange man takes you across the lake, but just as you're reaching the other side, he knocks you out with his ore")
        print("When you wake up, it is night, but you can see the house infront of you has three distinct doors, all of different colours, red, blue and yellow")
        door = input("You can't go back across the lake, unless you want to risk swimming, so you decide to choose a door, which do you choose?\n")

        if door == "Yellow":
            print("You open the door and step inside, the door immedietely shuts behind you and you think this is the end")
            print("But just as you have given up, the treasure reveals itself, a large chest full of gold. You have completed your mission")
            print("GAME OVER. YOU WIN")
        elif door == "red":
            print("You open the door and step inside, the door immedietely shuts behind you and you think this is the end")
            print("Turns out, you were right, the place lights up and it turns out the red door was a door to hell!")
            print("GAME OVER")
        elif door == "blue":
            print("You open the door and step inside, the door immedietely shuts behind you and you think this is the end")
            print("You feel cold almost instantly, a light suddenly illuminates the area, and it turns out you chose a walk in freezer.")
            print("You are destined to become a human ice pop forever. GAME OVER")
        else:
            print("You couldn't decide to you opened all three at once, nothing happens for a moment so you wait...")
            print("EVERYTHING HAS GONE BLACK. GAME OVER")

    elif swim_or_wait == "swim":
        print("You try to put your swimming prowess to the test, but try as you might, something grabs your leg and drags you to the bottom of the lake, like so many before.")
        print("GAME OVER")
    else:
        print("You couldn't decide between the two, and since the path you came is now lost to the darkness, you die due to indecision.")
        print("GAME OVER")

elif direction == "right":
    print("You go down the right path, you think you see a light, but the light is a trick, and you are quickly mauled by a wolf")
    print("GAME OVER")
else:
    print("You couldn't decide between going left or right and decided to give up on your adventure.")
    print("GAME OVER")





