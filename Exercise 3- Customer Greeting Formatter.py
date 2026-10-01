# Exercise 3: Customer Greeting Formatter
# Builds a personalized email greeting from a customer's name.
 
 
def format_greeting(name, title="Customer"):
    """Return a greeting using the customer's first name and a title."""
    # strip() removes leading and trailing spaces
    cleaned_name = name.strip()
 
    # If nothing is left after stripping, use a generic greeting
    if cleaned_name == "":
        return "Hello, Valued Customer!"
 
    # title() capitalizes each word ("john doe" -> "John Doe")
    # split() breaks the name at spaces; [0] takes the first word
    first_name = cleaned_name.title().split()[0]
    return f"Hello, {first_name} ({title})!"
 
 
# Main code
full_name = input("What's your full name? ")
 
# Optional extension: let the user enter a custom title.
# If they just press Enter, the function's default "Customer" is used.
custom_title = input("Title (press Enter for default)? ").strip()
 
if custom_title == "":
    print(format_greeting(full_name))
else:
    print(format_greeting(full_name, custom_title))