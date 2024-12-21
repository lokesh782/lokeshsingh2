# Accept the number of days from the user
days = int(input("Enter the number of days: "))

# Calculate the charge based on the number of days
if days <= 5:
    charge = days * 2  # Rs 2/day for up to 5 days
elif 6 <= days <= 10:
    charge = days * 3  # Rs 3/day for 6 to 10 days
elif 11 <= days <= 15:
    charge = days * 4  # Rs 4/day for 11 to 15 days
else:
    charge = days * 5  # Rs 5/day for after 15 days

# Display the total charge
print(f"The total charge for {days} days is: Rs {charge}")
