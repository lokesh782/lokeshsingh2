# Accept the salary and years of service from the user
salary = float(input("Enter your salary: Rs "))
years_of_service = int(input("Enter your years of service: "))

# Check if the years of service is more than 5 years
if years_of_service > 5:
    bonus = salary * 0.05  # 5% bonus
    print(f"Your bonus is: Rs {bonus:.2f}")
else:
    print("You are not eligible for a bonus.")
