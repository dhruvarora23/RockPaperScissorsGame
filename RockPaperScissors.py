def One_Player():
    print("One Player")
    from random import randint
    t = ["R", "P", "S"]
    computer = t[randint(0,2)]
    player = False
    while player == False:
        player = input("Rock, Paper, Scissors? (R/P/S) \n")
        if player == computer:
            print("Tie!")
        elif player == "R":
            if computer == "P":
                print("You lose!", computer, "covers", player)
            else:
                print("You win!", player, "smashes", computer)
        elif player == "P":
            if computer == "S":
                print("You lose!", computer, "cut", player)
            else:
                print("You win!", player, "covers", computer)
        elif player == "S":
            if computer == "R":
                print("You lose...", computer, "smashes", player)
            else:
                print("You win!", player, "cut", computer)
        else:
            print("That's not a valid play. Check your spelling!")
        
        player = False
        computer = t[randint(0,2)]

def Two_Player():
    print("Two Player")

    score = [0,0]
    while 1:
        c1 = input("Player 1 choose Rock/Paper/Scissors (R/P/S) : ")
        c2 = input("Player 2 choose Rock/Paper/Scissors (R/P/S) : ")
        if c1 == c2:
            print('Tie')
            score[0] += 1
            score[1] += 1
        elif c1 == "R" and c2 == "S":
            print('Player 1 won')
            score[0] += 1
        elif c1 == "R" and c2 == "P":
            print('Player 2 won')
            score[1] += 1
        elif c1 == "P" and c2 == "R":
            print('Player 1 won')
            score[0] += 1
        elif c1 == "P" and c2 == "S":
            print('Player 2 won')
            score[1] += 1
        elif c1 == "S" and c2 == "R":
            print('Player 2 won')
            score[1] += 1
        elif c1 == "S" and c2 == "P":
            print('Player 1 won')
            score[0] += 1
        else :
            print('Invalid Option, Check your spelling!')
           
        print(" score: Player 1 =",score[0]," Player 2 =",score[1])
        answer = input("Play another Round (y / n) : ")
        if answer.lower() != "y":
            break
            
       

Input_GameMode = input("What Game Mode would you like to choose? \n A - 1 player \n B - 2 Player \n")
if Input_GameMode == 'A':
    
    One_Player()
elif Input_GameMode == 'B':
    
    Two_Player()
else:
    print("Error, Incorrect Option. Try Again")
    


                
