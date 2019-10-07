##  Quiz build from Pottermore.com . I got it to work in Windows, but when I rewrote it on 
##  a Linux computer the house point calculation wouldn't work within the dictionary. Also, 
##  calling the dictionary in the 2nd to last line doesn't work anymore, not a string

import random, SortingQuestions

print("Welcome to the Hogwarts Sorting ceremony! Today you will be sorted into your house!")
print("Press Enter when you are ready to begin.")
input()
questions = [SortingQuestions.Q1, SortingQuestions.Q2, SortingQuestions.Q3, SortingQuestions.Q4, SortingQuestions.Q5,
             SortingQuestions.Q6, SortingQuestions.Q7, SortingQuestions.Q8, SortingQuestions.Q9, SortingQuestions.Q10,
             SortingQuestions.Q11, SortingQuestions.Q12, SortingQuestions.Q13, SortingQuestions.Q14, SortingQuestions.Q15,
             SortingQuestions.Q16, SortingQuestions.Q17, SortingQuestions.Q18]
chosen = []

for i in range(10):
    currentQ = random.choice(questions)()
    if currentQ not in chosen:
        chosen.append(currentQ)
        i = i+1
    else:
        continue   

print("Congratulations! you've completed the sorting ceremony!")
placed = max(SortingQuestions.house, key=lambda key: SortingQuestions.house[key])
print("Your house scores are: \n ", SortingQuestions.house)
print("You have been sorted into ", placed)
