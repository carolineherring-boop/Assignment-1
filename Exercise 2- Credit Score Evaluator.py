# Exercise 2: Credit Score Evaluator
# Categorizes a credit score and decides loan eligibility.

score = int(input("What's your credit score? "))

# Check the valid range first so we don't categorize impossible scores
if score < 300 or score > 850:
    print("Invalid score.")
else:
    # Because each elif is only reached if the previous test failed,
    # we only need to check the lower bound of each range
    if score >= 750:
        category = "Excellent - Loan Approved"
    elif score >= 700:
        category = "Good - Loan Approved with Review"
    elif score >= 600:
        category = "Fair - Loan Conditional"
    else:
        category = "Poor - Loan Denied"

    # Only Excellent and Good are fully approved (score of 700 or more)
    approved = score >= 700
    advice = "Interest rate: Low" if approved else "Seek credit improvement."

    print(f"{category}. {advice}")