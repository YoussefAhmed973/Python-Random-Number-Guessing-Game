#table
children = range(0, 15)
youth = range(15, 25)
adults = range(25, 65)
seniors = range(65, 10000000000000)

ageInput = int(input("Enter your age! "))



def determiner():
    if ageInput in children:
        print("You have entered", ageInput, "and you are in Children")
    elif ageInput in youth:
        print("You have entered", ageInput, "and you are in Youth")
    elif ageInput in adults:
        print("You have entered", ageInput,  "and you are in Adult")
    else:
        print("You have entered", ageInput, "and you are in Senior")


determiner()