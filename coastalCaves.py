"""
         package: coastalCaves.py
          author: Charles J McDonald «https://github.com/cjmcdonald42»
    last updated: 2026.03.18
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

# Choose an Ancestry
print("""
    In this world, you can be a (h)uman, an (e)lf, or a (d)warf.
    """)
choice = input("Which ancestry will you choose? (h/e/d) ")
if choice == "h":
    print("The humans of Rhode are very versatile.")
    race = "human"
elif choice == "e":
    boost = print("Rhodish Elves are smart and nimble.")
    race = "elf"
else:
    print("You have chosen a Dwarf. Rhodish dwarves are hardy and strong.")
    race = "dwarf"


# Choose a Background
# Choose a Class

# Enter the Dungeon

# Boss mob of some sort

# Fight the Boss
# Sneak past the Boss
# Run away from the Boss in terror
