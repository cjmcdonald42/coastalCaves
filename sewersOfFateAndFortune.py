#         package: sewersOfFateAndFortune.py
#          author: Charles J McDonald «https://github.com/cjmcdonald42»
#    date written: 2026.03.23
#     description: A sample adventure game for learning to code in python.

import random

# Introduction, describe the scene as our hero delves deep into the city sewers.
print("""
    Our adventure begins with you heading into the city sewers. These old, cobblestone tunnels are rife
    with an aroma so thick you stand a fork in it. From the moment you enter, you are engulfed by the smell
    of a heavy rot that tastes like wet earth and ancient iron. It’s not just a smell; but a presence that
    clings to the back of your throat.

    As you move deeper into the sewers, the city sounds above fade into a dead, crushing silence, replaced by
    the low, guttural groan of shifting stonework.
    """)

# Face a challenge --> Fight, Magic, Escape
print("Suddenly, you are confronted by a fierce sewer monster. \n")
print("You may (F)ight the fearsome beast, Use (S)tealth to sneak behind it, or (R)un away.")
choice = input("What will you do? (F/S/R): ")

if choice == "F":           # Choose to Fight
    print("You draw your sword and swing wildly")
    attackRoll = random.randint(1, 20)
    if attackRoll >= 12: 
        print("Your attack hits and you slay the vile creature")
        print("Collect your treaure!")
    else:
        print("You swing valiently but miss!")
        print("The dragon pins you down and tickles you into a stupor. \n")
elif choice == "S":         # Choose to Stealth
    stealthRoll = random.randint(1, 20)
    if stealthRoll >= 14:
        print("You get all sneaky-like and move behind the monster to steal its treasure")
        print("Collect your treaure!")
    else:
        print("You're not as sneaky as you though and you wake the beast who then gobbles you up in one bite!")
else:                        # choice == "R" -- RUN AWAY!
    print("You retreat quickly and although you get no treasure, you live to fight another day.")

# Resolution?
    print("You return to town wiser and possibly richer. Perhaps another trip will yield more treasure.")