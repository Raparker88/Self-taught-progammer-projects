
def guess_num():
    import random
    comp_num=random.randint(1,20)
    
    while True:
        try:
            guess=input("guess a number from 1 to 20: ")
            guess=int(guess)
            if guess < comp_num:
                print("guess is too low")
            if guess > comp_num:
                print("guess is too high")
            if guess==comp_num:
                print("You guessed it!")
                break
        except(ValueError):
            print("invalid input")

guess_num()
    
