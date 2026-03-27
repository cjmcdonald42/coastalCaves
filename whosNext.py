"""
         package: whosNext.py
          author: Charles J McDonald «https://github.com/cjmcdonald42»
    last updated: 2026.03.27
     description: Pick the next student who will present their work.
"""
import random

# Create a list of students
studentList = ['Joshua', 'Jariel', 'Jacque', 'Gatlin', 'Lief', 'Tristan', 'Easton', 'Wells']

choosingWhosNext = True
while choosingWhosNext:
    # Ask the teacher to spin the wheel
    print("The following students could be next:")
    print(studentList)
    choice = int(input("Would you like to 1) Choose the next volunteer, or 2) End the presentations? (1 | 2): "))

    if choice == 1:
        # Randomly choose the next student
        numberOfStudentsRemaining = len(studentList)
        student = random.randint(0, numberOfStudentsRemaining-1)
        # print(student, len(studentList))
        nextPresenter = studentList[student]
        print(f"Next up on our stage: {nextPresenter} \n")

        # Remove that student from the list
        studentList.remove(nextPresenter)
        if not studentList:
            print("That is the last student \n")
            choosingWhosNext = False

    elif choice == 2:
        # End the Presentation
        print("End of Presentations")
        choosingWhosNext = False

    else:
        print("That's not a valid option, please try again. \n")
