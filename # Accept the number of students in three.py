# Accept the number of students in three classrooms
a = int(input("Enter the number of students in classroom A: "))
b = int(input("Enter the number of students in classroom B: "))
c = int(input("Enter the number of students in classroom C: "))

# Calculate the number of desks needed for each classroom
desks_a = (a + 1) // 2
desks_b = (b + 1) // 2
desks_c = (c + 1) // 2

# Calculate the total number of desks needed
total_desks = desks_a + desks_b + desks_c

# Display the result
print(f"The total number of desks required is: {total_desks}")
