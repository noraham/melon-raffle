"""Randomly pick customer and print customer info"""

# Add code starting here

# Hint: remember to import any functions you need from
# other files or libraries

import random
import customers

def pick_winner(customer_file_path):
    """Choose a random winner from list of customers."""
    customers_obj = customers.get_customers_from_file(customer_file_path)

    chosen_customer = random.choice(customers_obj)

    print "Tell {name} at {email} that they've won".format(
        name=chosen_customer.name,
        email=chosen_customer.email
        )

pick_winner("customers.txt")
