# Exercise 4: Tax Bracket Determiner
# Determines an income tax bracket and estimates the tax owed.
 
 
def get_tax_bracket(income, check_deduction=False):
    """Return the tax bracket for an income as a string."""
    if income < 0:
        return "Invalid income."
 
    if income < 50_000:
        bracket = "Low (10%)"
    elif income < 100_000:
        bracket = "Medium (20%)"
    else:
        bracket = "High (30%)"
 
    # Bonus: ternary expression. Income is deduction-eligible if it is even.
    if check_deduction:
        return bracket + " (Deduction Eligible)" if income % 2 == 0 else bracket
    return bracket
 
 
def get_tax_rate(income):
    """Return the tax rate as a decimal, matching the brackets above."""
    if income < 50_000:
        return 0.10
    elif income < 100_000:
        return 0.20
    else:
        return 0.30
 
 
# Main code
income = float(input("What's your annual income? "))
 
if income < 0:
    print(get_tax_bracket(income))
else:
    bracket = get_tax_bracket(income)
    estimated_tax = round(income * get_tax_rate(income), 2)
    print(f"Your bracket: {bracket}. Estimated tax: {estimated_tax}")
 
    # Bonus output: show the bracket with the deduction check applied
    print(f"Deduction check: {get_tax_bracket(income, check_deduction=True)}")