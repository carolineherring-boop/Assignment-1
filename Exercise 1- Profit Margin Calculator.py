# Exercise 1: Profit Margin Calculator
# Calculates profit and profit margin from revenue and cost.
 
# Get revenue and cost from the user, converting the text input to floats
revenue = float(input("What's the revenue? "))
cost = float(input("What's the cost? "))
 
# Margin divides by revenue, so revenue must be positive to avoid dividing by zero
if revenue > 0:
    profit = revenue - cost
    margin = (profit / revenue) * 100
    # :,.2f adds thousands separators and rounds to 2 decimal places
    print(f"Profit: ${profit:,.2f} | Margin: {margin:.2f}%")
else:
    print("Invalid revenue.")