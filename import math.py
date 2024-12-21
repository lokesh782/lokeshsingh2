import math

# Accept the radius of the circle from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle using the formula: Area = π * r^2
area = math.pi * (radius ** 2)

# Display the area of the circle
print(f"The area of the circle with radius {radius} is: {area:.2f}")
