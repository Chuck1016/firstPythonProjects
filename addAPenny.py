print('If you put a penny in your piggy bank on the first day of the year,')
print('two pennies the second day, and so on for an entire year...\n')

day = 0
money = 0.00

for i in range(365):
    day = day +1
    money = money+day
    if day == 30:
        print('After one month you would have: $'+str(money/100))
    elif day == 180:
        print('After six months you would have: $'+str(money/100) )
    elif day == 365:
        print('After one year you would have: $'+str(money/100) )

##    print(day, money/100) to see amount for each day
