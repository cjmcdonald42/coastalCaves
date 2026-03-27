import random

# ask what to do?
choice = input("What action will you take? (a=Fight, b=Sneak, c=Run away: ")
# Fight
if choice == "a":
    print("You drw your sword and swing wildly!")
    attackRoll = random.randint(1,20)
    if attackRoll >= 12:
        print(f"You roll a {attackRoll} and hit the beastie!")
    else:
        print("Your swing misses!")
# Sneak
else if choice == "b":
    pass
# Run Away
else:
    pass
