# Accept the ages of 4 people
age1 = int(input("Enter the age of person 1: "))
age2 = int(input("Enter the age of person 2: "))
age3 = int(input("Enter the age of person 3: "))
age4 = int(input("Enter the age of person 4: "))

# Find the youngest age using the min() function
youngest_age = min(age1, age2, age3, age4)

# Display the youngest age
print("The youngest age is:", youngest_age)
