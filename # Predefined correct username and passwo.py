# Predefined correct username and password
correct_username = "user123"
correct_password = "password456"

# Ask the user for the username and password
username = input("Enter username: ")
password = input("Enter password: ")

# Check if the username is correct
if username == correct_username:
    # If username is correct, check if the password is correct
    if password == correct_password:
        print("Login successful! Welcome.")
    else:
        print("Incorrect password. Please try again.")
else:
    print("Incorrect username. Please try again.")
