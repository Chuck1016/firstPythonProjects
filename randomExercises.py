##  Solving problem withe the Sorting Hat. Set a blank list to be appended
##  each time an option is chosen. Check each iteration for the current option
##  If the current option is already in the chosen list, skip it.
##  
##  the else continue counts as an iteration, so the total result count can change.


import random

choices = ['first', 'second', 'third', 'fourth', 'fifth']
chosen = []

for i in range(6):
    toPrint = random.choice(choices)
    if toPrint not in chosen:
        print(toPrint)
        chosen.append(toPrint)
        i = i+1
        print(chosen)
    else:
        continue
