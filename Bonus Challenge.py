# Bonus Challenge: Integrated Decision Tool
# Combines profitability checks and product categories into an investment suggestion.
 
 
def is_profitable(revenue, cost):
    """Return True if revenue is greater than cost."""
    return revenue > cost
 
 
def get_category(product):
    """Return the margin category for a product name."""
    if product in ("electronics", "gadget"):
        return "High Margin"
    if product.startswith("tech"):
        return "High Margin"
    if product in ("clothing", "apparel"):
        return "Medium Margin"
    if product in ("food", "grocery"):
        return "Low Margin"
    return "Uncategorized - Review Needed"


def get_suggestion(category):
    """Return an investment suggestion based on the category."""
    if category == "High Margin":
        return "Reinvest"
    if category == "Medium Margin":
        return "Maintain current investment"
    if category == "Low Margin":
        return "Focus on volume and cost control"
    return "Review product before investing"
 
 
def main():
    revenue = float(input("What's the revenue? "))
    cost = float(input("What's the cost? "))
    product = input("What's the product category? ").strip().lower()
 
    category = get_category(product)
 
    if is_profitable(revenue, cost):
        profit = revenue - cost
        print(f"Profitable! Profit: ${profit:,.2f}")
        print(f"Category: {category} | Suggestion: {get_suggestion(category)}")
    else:
        loss = cost - revenue
        print(f"Not profitable. Loss: ${loss:,.2f}")
        print("Suggestion: Reduce costs or review pricing before investing.")
 
 
main()