# Accept the cost price of the bike
cost_price = float(input("Enter the cost price of the bike (in Rs): "))

# Calculate the road tax based on the given criteria
if cost_price > 100000:
    tax = cost_price * 0.15  # 15% tax
elif cost_price > 50000 and cost_price <= 100000:
    tax = cost_price * 0.10  # 10% tax
else:
    tax = cost_price * 0.05  # 5% tax

# Display the calculated road tax
print(f"The road tax to be paid is: Rs {tax:.2f}")
