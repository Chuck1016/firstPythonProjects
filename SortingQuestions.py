# Gryffindor=0
# Ravenclaw=0
# Hufflepuff=0
# Slytherin=0

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
def Q2():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('After you have died, what would you most like people to do when they hear your name?')
    print('a. Miss you, but smile')
    print('b. Ask for more stories about your adventures')
    print('c. Think with admiration of you achievements')
    print('d. I don\'t care what people think of me after I\'m dead; it\'s what they think of me while I\'m alive that counts')
    choice = input()
    if choice == 'b':
        Gryffindor = Gryffindor +1
    elif choice == 'c':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'd':
        Slytherin= Slytherin +1    
def Q3():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Given the choice, would you rather invent a potion that would guarantee you:')
    print('a. Glory')
    print('b. Wisdom')
    print('c. Love')
    print('d. Power')
    choice = input()
    if choice == 'a':
        Gryffindor = Gryffindor +1
    elif choice == 'b':
        Ravenclaw= Ravenclaw +1
    elif choice == 'c':
        Hufflepuff= Hufflepuff +1
    elif choice == 'd':
        Slytherin= Slytherin +1   
def Q4():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('How would you like to be known to history?')
    print('a. The Wise')
    print('b. The Good')
    print('c. The Bold')
    print('d. The Great')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'a':
        Ravenclaw= Ravenclaw +1
    elif choice == 'b':
        Hufflepuff= Hufflepuff +1
    elif choice == 'd':
        Slytherin= Slytherin +1  
def Q5():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('You enter an enchanted garden. What would you be most curious to examine first?')
    print('a. The silver leafed tree bearing golden apples')
    print('b. The fat red toadstools that appear to be talking to each other')
    print('c. The bubbling pool, in the depths of which something luminous is swirling')
    print('d. The statue of an old wizard with a strangely twinkling eye')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'b':
        Hufflepuff= Hufflepuff +1
    elif choice == 'a':
        Slytherin= Slytherin +1   
def Q6():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('What kind of instrument most pleases your ear?')
    print('a. Violin')
    print('b. Drums')
    print('c. Piano')
    print('d. Trumpet')
    choice = input()
    if choice == 'd':
        Gryffindor = Gryffindor +1
    elif choice == 'c':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'b':
        Slytherin= Slytherin +1    
def Q7():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Four boxes are placed before you. Which would you try to open?')
    print('a. The small tortoiseshell box, embellished with gold, inside which some small creature seems to be squeaking.')
    print('b. The gleaming jet black box with a silver lock and key, marked with a mysterious rune that you know to be the mark of Merlin.')
    print('c. The ornate golden casket, standing on clawed feet, whose inscription warns that both secret knowledge and unbearable temptation lie within.')
    print('d. The small pewter box, unassuming and plain, with a scratched message upon it that reads "I open only for the worthy."')
    choice = input()
    if choice == 'd':
        Gryffindor = Gryffindor +1
    elif choice == 'b':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'c':
        Slytherin= Slytherin +1   
def Q8():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Four goblets are placed before you. Which would you choose to drink?')
    print('a. The foaming, frothing, liquid that sparkles as though containing ground diamonds.')
    print('b. The smooth, thick, drink that gives off a delicious smell of chocolate and plums.')
    print('c. The liquid so bright that it hurts the eye, and which makes sunspots dance all around the room.')
    print('d. The mysterious liquid that gleams like ink, and gives off fumes that make you see strange visions.')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'b':
        Hufflepuff= Hufflepuff +1
    elif choice == 'a':
        Slytherin= Slytherin +1  
def Q9():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Once every century, the Flutterby bush produces flowers that adapt their scent to attract the unwary. If it lured you, it would smell of:')
    print('a. A crackling log fire')
    print('b. Fresh parchment')
    print('c. Home')
    print('d. The sea')
    choice = input()
    if choice == 'a':
        Gryffindor = Gryffindor +1
    elif choice == 'b':
        Ravenclaw= Ravenclaw +1
    elif choice == 'c':
        Hufflepuff= Hufflepuff +1
    elif choice == 'd':
        Slytherin= Slytherin +1    
def Q10():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Which would you rather be?')
    print('a. Trusted')
    print('b. Liked')
    print('c. Imitated')
    print('d. Praised')
    choice = input()
    if choice == 'a':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'b':
        Hufflepuff= Hufflepuff +1
    elif choice == 'c':
        Slytherin= Slytherin +1  
def Q11():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Which of the following do you find most difficult to deal with?')
    print('a. Hunger')
    print('b. Loneliness')
    print('c. Boredom')
    print('d. Being Ignored')
    choice = input()
    if choice == 'b':
        Gryffindor = Gryffindor +1
    elif choice == 'c':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'd':
        Slytherin= Slytherin +1   
def Q12():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('If you could have any power, which would you choose?')
    print('a. The power to read minds')
    print('b. The power of invisibility')
    print('c. The power of superhuman strength')
    print('d. The power to speak to animals')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'b':
        Ravenclaw= Ravenclaw +1
    elif choice == 'd':
        Hufflepuff= Hufflepuff +1
    elif choice == 'a':
        Slytherin= Slytherin +1  
def Q13():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('One of your house mates has cheated in a Hogwarts exam. Now he has taken top of the class in Charms from you. Professor Flitwick is suspicious, so he draws you to one side after his lesson and asks you if you know what happened. What do you do?')
    print('a. Lie and say you don\'t know (then tell your house mate that your silence has a price).')
    print('b. Tell Professor Flitwick that he ought to ask your classmate (and resolve to tell your classmate that if he doesn\'t tell the truth, you will).')
    print('c. Tell Professor Flitwick the truth. If your classmate is prepared to win by cheating, he deserves to be found out.')
    print('d. You would not wait to be asked to tell Professor Flitwick the truth. If you knew that somebody was using a forbidden quill, you would tell the teacher before the exam started.')
    choice = input()
    if choice == 'b':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'c':
        Hufflepuff= Hufflepuff +1
    elif choice == 'a':
        Slytherin= Slytherin +1    
def Q14():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('You and two friends need to cross a bridge guarded by a river troll who insists on fighting one of you before he will let all of you pass. Do you:')
    print('a. Attempt to confuse the troll into letting all three of you pass without fighting?')
    print('b. Suggest drawing lots to decide which of you will fight?')
    print('c. Suggest that all three of you should fight (without telling the troll)?')
    print('d. Volunteer to fight?')
    choice = input()
    if choice == 'd':
        Gryffindor = Gryffindor +1
    elif choice == 'a':
        Ravenclaw= Ravenclaw +1
    elif choice == 'b':
        Hufflepuff= Hufflepuff +1
    elif choice == 'c':
        Slytherin= Slytherin +1  
def Q15():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Which road tempts you most?')
    print('a. The wide, sunny, grassy lane')
    print('b. The narrow, dark, lantern-lit alley')
    print('c. The twisting, leaf-strewn path through woods')
    print('d. The cobbled street lined with ancient buildings')
    choice = input()
    if choice == 'a':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'c':
        Hufflepuff= Hufflepuff +1
    elif choice == 'b':
        Slytherin= Slytherin +1  
def Q16():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Which nightmare would frighten you most?')
    print('a. Standing on top of something very high and realizing suddenly that there is nothing to stop you falling')
    print('b. An eye at the keyhole of the dark, windowless room in which you are locked')
    print('c. Waking up to find that neither your friends nor your family have any idea who you are')
    print('d. Being forced to give a speech where everyone laughs at you')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'b':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'd':
        Slytherin= Slytherin +1  
def Q17():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('Late at night, walking alone down the street, you hear a peculiar cry that you believe to have a magical source. Do you:')
    print('a. Proceed with caution, keeping one hand on your concealed wand and an eye out for any disturbance?')
    print('b. Draw your wand and try to discover the source of the noise?')
    print('c. Draw your wand and stand your ground?')
    print('d. Withdraw into the shadows to await developments, while mentally reviewing the most appropriate defensive and offensive spells, should trouble occur?')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'b':
        Slytherin= Slytherin +1  
def Q18():
    global Gryffindor
    global Ravenclaw
    global Hufflepuff
    global Slytherin
    print('A Muggle confronts you and says that they are sure you are a witch. Do you:')
    print('a. Ask what makes them think so')
    print('b. Agree, and ask whether they\'d like a free sample of a jinx')
    print('c. Agree, and walk away, leaving them to wonder whether you are bluffing')
    print('d. Tell them that you are worried about their mental health, and offer to call a doctor')
    choice = input()
    if choice == 'c':
        Gryffindor = Gryffindor +1
    elif choice == 'd':
        Ravenclaw= Ravenclaw +1
    elif choice == 'a':
        Hufflepuff= Hufflepuff +1
    elif choice == 'b':
        Slytherin= Slytherin +1  
