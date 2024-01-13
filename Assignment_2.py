import random

"""
Author:                 Sujan Rokad
Authorship statement:   I, Sujan Rokad, 000882948, certify that this material is my original work. No other person's work has been used without due acknowledgement.
Purpose:                Calculate change for a purchase and provide the breakdown of dollars, quarters, dimes, and nickels.
"""

# Generate a random amount for testing purposes
amount = random.uniform(0, 50000) + round(random.uniform(0, 50000), 2)
print('Your amount is:', amount)

# Get the purchase total from the user
payment = float(input("Enter your purchase total: "))

# Assume payment >= amount
change = payment - amount

if change > 0:
    dollars = int(change)
    quarters = int((change - dollars) / 0.25)
    dimes = int((change - dollars - quarters * 0.25) / 0.10)
    nickels = int((change - dollars - quarters * 0.25 - dimes * 0.10) / 0.05)

    print("You will receive:")
    print("- {} dollars".format(dollars))
    print("- {} quarters".format(quarters))
    print("- {} dimes".format(dimes))
    print("- {} nickels".format(nickels))
else:
    print("No change owed")
