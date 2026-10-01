# Exercise 5: Product Category Matcher
# Uses match-case to assign a pricing category to a product.
 
# strip() removes extra spaces; lower() makes matching case-insensitive
product = input("What's the product name? ").strip().lower()
 
if product in {"electronics", "gadget"}:
    category = "High Margin"
# A guard (the "if" part) lets us match any name starting with "tech".
elif product.startswith("tech"):
    category = "High Margin"
elif product in {"clothing", "apparel"}:
    category = "Medium Margin"
elif product in {"food", "grocery"}:
    category = "Low Margin"
else:
    category = "Uncategorized - Review Needed"
 
print(f"Product: {product} | Category: {category}")