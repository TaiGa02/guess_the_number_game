import random

def isValid(num):
    return num in [1, 3, 5, 10]


print("Welcome to the Guess the number game!!!")
flag = True

minValue = int(input("Please assign the minimum value here\n"))
maxValue = int(input("Next, please input the maximum value for the game\n"))

while flag:
    if minValue < maxValue:
        flag = False
        numberOfTry = int(input("Please select the number of trial, 1, 3, 5, or 10 ?\n"))
        while not isValid(numberOfTry):
            print("The input number is not valid. Please select again")
            numberOfTry = int(input("Please select the number of trial, 1, 3, 5, or 10 ?\n"))

    elif minValue >= maxValue:
        print("The input number is not valid. Please select again")
        minValue = int(input("Please assign the minimum value here\n"))
        maxValue = int(input("Next, please input the maximum value for the game\n"))


ranInt = random.randint(minValue,maxValue)
isCorrect = False
for _ in range(numberOfTry):
    guessNum = int(input(f"Let's guess the random value between {minValue} and {maxValue}\n"))
    if guessNum == ranInt:
        print("Congratulation!! Your guess is correct!! What a suplendid detective")
        isCorrect = True
        break
    else:
        print("Your guess is wrong. Please try again if you don't reach the limit.")

if not isCorrect:
    print("This time, you couldn't figure the random number out, but maybe next time.")
    print("The answer was " + ranInt)
    print("If you want, please try again.")
