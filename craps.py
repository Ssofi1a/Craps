from random import randrange

diceThrow1 = randrange(1,6)
diceThrow2 = randrange(1,6)
answer = diceThrow1 + diceThrow2
print(f"The sum of dice is {str(diceThrow1)} + {str(diceThrow2)} = {str(answer)}")
if(answer == 7 or answer == 11):
    print("You win!")
elif(answer == 2 or answer == 3 or answer == 12):
    print("You lose")
else:
    print(f"Now your goal number is {str(answer)}")
    i = answer
    answer1 = 0
    while (i != answer1) :
        diceThrow1 = randrange(1,6)
        diceThrow2 = randrange(1,6)
        answer1 = diceThrow1 + diceThrow2
        print(f"The sum of dice is {str(diceThrow1)} + {str(diceThrow2)} = {str(answer1)}")
        if(answer1 == 7):
            print("You lose((")
            break 
    if(answer1 != 7):
        print("You win!")
