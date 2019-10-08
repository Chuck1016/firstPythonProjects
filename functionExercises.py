Gryffindor=0
Ravenclaw=0
Hufflepuff=0
Slytherin=0

house = {'Gryffindor':0, 'Ravenclaw':0, 'Hufflepuff':0, 'Slytherin':0}


def Q1():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Which of the following would you most hate people to call you?')
    print('a. Ordinary')
    print('b. Ignorant')
    print('c. cowardly')
    print('d. Selfish')
    choice = input()

    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'b':
        Ravenclaw= Ravenclaw +1
    elif choice == 'd':
        Hufflepuff= Hufflepuff +1
    elif choice == 'a':
        Slytherin= Slytherin +1
    else:
        print("That is not a valid choice. Please try again")

Q1()
print("Gryffindor:", Gryffindor, "Ravenclaw:", Ravenclaw, "Hufflepuff:", Hufflepuff, "Slytherin:", Slytherin)

