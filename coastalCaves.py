"""
         package: coastalCaves.py
          author: Charles J McDonald «https://github.com/cjmcdonald42»
    date written: 2026.03.18
     description: A sample adventure game for learning python coding.

"""
# Introduction
print("""
    Welcome to the Coastal Caves of the Island of Rhode!
    Long have you known of the splendor and the dangers of the coastal caves,
    But today, you have mustered the courage to go and explore.
    """)

# Create a new character
playerName = input("What is your name: ")

# Start with a blank character sheet
playerSTR = 0
playerDEX = 0
playerCON = 0
playerWIS = 0
playerINT = 0
playerCHA = 0

# Choose an Ancestry
print("""
    In this world, you can be a (h)uman, an (e)lf, or a (d)warf.
    """)
choice = input("Which ancestry will you choose? (h/e/d) ")
if choice == "h":
    print("The humans of Rhode are very versatile. You my boost any two scores.")
    print("(S)TR, (C)ON, (D)EX, (W)IS, (I)NT, (CH)A")
    firstBoost = input("Choose the first skill you'd like to boost: (s/c/d/w/i/ch) ")
    secondBoost = input("Choose the first skill you'd like to boost: (s/c/d/w/i/ch) ")
    if firstBoost == "s":       # First Boost
        playerSTR += 1
    elif firstBoost == "c":
        playerCON += 1
    elif firstBoost == "d":
        playerDEX += 1
    elif firstBoost == "w":
        playerWIS += 1
    elif firstBoost == "i":
        playerINT += 1
    elif firstBoost == "ch":
        playerCHA += 1

    if secondBoost == "s":       # Second Boost
        playerSTR += 1
    elif secondBoost == "c":
        playerCON += 1
    elif secondBoost == "d":
        playerDEX += 1
    elif secondBoost == "w":
        playerWIS += 1
    elif secondBoost == "i":
        playerINT += 1
    elif secondBoost == "ch":
        playerCHA += 1

elif choice == "e":
    boost = print("Rhodish Elves are smart and nimble. Will you boost your INT or your DEX? (i/d)")
    if boost == "i":
        playerINT += 1
    else:
        playerDEX += 1
#TODO add ability choice
else:
    print("You have chosen a Dwarf. Rhodish dwarves are hardy and strong.")
    boost = print("Will you boost your STR or your CON? (s/c)")
    if boost == "s":
        playerSTR += 1
    else:
        playerCON += 1
#TODO add ability choice


# Choose a Background
# Choose a Class

# Enter the Dungeon

# Boss mob of some sort

# Fight the Boss
# Sneak past the Boss
# Run away from the Boss in terror
