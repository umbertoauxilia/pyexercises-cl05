"""Exercise 4.2 — Working with a dictionary

WHAT THE PROGRAM MUST DO
    Describe one real object from your field using a dictionary of at least five fields,
    then read it, change it, remove one field, and display every field with its value.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What object did you describe, which five fields did you choose, and why those?
       A field you would never actually use does not count.

WHAT THE AI CANNOT KNOW
    Your object and your fields. A campaign, a customer, a product, a store, a supplier.
    Choose something you would genuinely have to describe in your job.

CHECK IT YOURSELF
    Ask your program for a field that does not exist. Note what happens in a comment,
    then make it survive that case.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A dictionary that describes one product, with 6 fields.
# 2. Process:The program reads one field, changes one, removes one,then shows all the fields with their values.
# 3. Out:The fields and values of the product, after the changes.
# 4. My object, my five fields, and why those:A menswear product I would buy for a store.name, brand, wholesale price, retail price, quantity:they are the information I need on every purchase order.



# Your code below
product = {"name": "Wool blazer", "brand": "Loewe", "price": 2200, "quantity": 6, "season": "FW26"}

print(product["brand"])        # read
product["quantity"] = 10       # change
del product["season"]          # remove

for key in product:            # display every field
    print(key, ":", product[key])

print(product.get("color", "not found"))   # field that does not exist