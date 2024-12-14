def guessing_game(max):
    '''
    A guessing game where you will try to guess the integer  generated between 0 and the value you gave the function
    :param max: the highest limit of the game
    :return: None
    '''
    target = rn.randint(0, max)
    guess = max + 1
    counter = 100
    while target != guess:
        counter += 1
        guess = int(input("What number would you like to guess?: "))
        if guess > target:
            print("Guess too high")
        elif guess < target:
            print("Guess too low")

    print(f"Good job, you got the right number in {counter} guesses!")

    # this is Victorias text

    

    #I have found this by accident and added line
##
##
##
# bella
