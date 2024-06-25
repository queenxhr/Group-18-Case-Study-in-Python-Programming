import random

def roll_dice():
    #Roll two six-sided dice
    return random.randint(1, 6) + random.randint(1, 6)

def play_game():
    first_roll = roll_dice()
    print(f"First roll: {first_roll}")
    
    #win if 7 or 11 on first roll
    if first_roll in [7, 11]:
        print("You win!")
        
    #lose if 2, 3 or 12 on first roll
    elif first_roll in [2, 3, 12]:
        print("Craps! You lose.")
        
    #if other than that, loop until same value to win or lose if 7
    else:
        print(f"Your point is {first_roll}.")
        point = first_roll
        while True:
            roll = roll_dice()
            print(f"Next roll: {roll}")
            if roll == point:
                print(f"You win! Your point is {roll} same as your first roll")
                break
            elif roll == 7:
                print("Its a 7, you lose.")
                break

#call the funtion
play_game()
