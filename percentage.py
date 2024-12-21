# Input: Percentage
percentage = float(input("Enter the percentage: "))

# Determine the category based on the percentage
if percentage < 40:
    category = "Failed"
elif 40 <= percentage < 55:
    category = "Fair"
elif 55 <= percentage < 65:
    category = "Good"
else:
    category = "Excellent"

# Display the category
print(f"Category: {category}")
