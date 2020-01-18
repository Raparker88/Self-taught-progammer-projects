


def rock_paper_scissors():
    print("Welcome to rock, paper, scissors! Best 2 out of 3!")
    comp_score=0
    player_score=0
    

    while comp_score<2 and player_score<2:
        try:
            import random
            num=random.randint(0,2)
            options=["rock","paper","scissors"]
            computer=options[num]
            attempt=input("rock,paper,or scissors?: ")
            attempt=attempt.lower()

            if computer==attempt:
                print(computer)
                print("tie")
            if computer=="rock" and attempt=="paper":
                print(computer)
                print("you win")
                player_score += 1
            if computer=="rock" and attempt=="scissors":
                print(computer)
                print("you lose")
                comp_score += 1
            if computer=="paper" and attempt=="rock":
                print(computer)
                print("you lose")
                comp_score += 1
            if computer=="paper" and attempt=="scissors":
                print(computer)
                print("You win")
                player_score =+1
            if computer=="scissors" and attempt=="rock":
                print(computer)
                print("you win")
                player_score += 1
            if computer=="scissors" and attempt=="paper":
                print(computer)
                print("you lose")
                comp_score += 1
        except(ValueError):
            print("invalid input")
    if comp_score==2:
         print("computer wins best 2 of 3")
            
    if player_score==2:
         print("you win best 2 of 3")
            
rock_paper_scissors()
        
