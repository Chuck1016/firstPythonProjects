 
def Banana():
    answer1 = ''
    while answer1 != "who's there":
        print('Knock knock')
        answer1 = input()
    answer2 = ''
    while answer2 != "Banana who":
        print('Banana')
        answer2 = input()
def Orange():
    answer3 = ''
    while answer3 != "who's there":
        print ("knock knock")
        answer3 = input()
        answer4 = ''    
    while answer4 != "Orange who":
        print('Orange')
        answer4 = input()

    
joke = 0
while joke <2:
    Banana()
    joke = joke+1
Orange()
print("Orange you glad I didn't say Banana????")
input()

       
