# Accept the ages of 4 people
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))

# Find the oldest age using the max() function
oldest_age = max(age1, age2, age3, age4)

# Display the oldest age
print("The oldest age is:", oldest_age)
