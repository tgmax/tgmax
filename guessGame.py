secretNumber = int(input("Type here your secret number and don't tell anyone! "))
print("Now give your friend chance to guess it :)")


for gameGuessNumber in range(1,100):
    guessNumber = int(input(" Guess a number from 1 to 100 that your friend guessed now "))

    if (guessNumber > secretNumber) and (secretNumber > guessNumber + 10):
        print("It is hot! You are getting close! But it is less than that!")
    elif guessNumber > secretNumber:
        print("Cold! It is less than that!")
    elif (guessNumber < secretNumber) and (secretNumber < (guessNumber - 10)):
        print("Look at you! Hot Hot Hot! But unfortunately it is more than that!")
    elif guessNumber < secretNumber:
        print("Freezing! Secret number is more than that!")
    else:
        break

if guessNumber == secretNumber:
    print("You are amazing! You need to try your luck with lottery! You won and now you are a Millioner!")
else:
    print("Not the number I was thinking!")
