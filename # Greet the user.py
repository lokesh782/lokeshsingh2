# Greet the user
print("Welcome to Treasure Land!")

# Prompt the user to choose a direction
direction = input("Do you want to go 'left' or 'right'? ").lower()

if direction == "right":
    print("Game Over")
else:
    # If the user chooses 'left', ask if they want to 'swim' or 'wait'
    action = input("Do you want to 'swim' or 'wait'? ").lower()
    
    if action == "swim":
        print("Game Over")
    else:
        # If the user chooses to 'wait', ask for a color choice
        color = input("Choose a color: 'red', 'blue', or 'yellow': ").lower()
        
        if color == "red" or color == "blue":
            print("Game Over")
        elif color == "yellow":
            print("You found the treasure! You Win!")
        else:
            print("Invalid choice. Game Over.")
