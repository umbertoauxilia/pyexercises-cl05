"""Exercise 4.0 — Working with a list

WHAT THE PROGRAM MUST DO
    Build a list of at least eight items, then display: the whole list, one item of your
    choice, the list sorted, and something computed from it.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your list about, and what did you compute from it? Why is that number
       interesting?

WHAT THE AI CANNOT KNOW
    The content of your list. It must come from your own field: marketing channels,
    campaign names, product references, cities you operate in, monthly budgets. Not
    fruit, not "item1, item2, item3".

    Keep this file. Exercise 5.1 and exercise 6.0 both reuse the list you build here.

CHECK IT YOURSELF
    If you computed an average, a total or a maximum, work it out by hand on three of
    your items first, then check your program agrees on those three.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:A list of 8 prices (in euros) of menswear items for a store
# 2. Process:he program shows the list, picks one price, sorts the list,and calculates the total and the average price.
# 3. Out:The whole list, one price, the sorted list, the total and the average
# 4. What my list is about, and what I computed from it:The prices of 8 menswear items I would buy for a storeI computed the total and the average price,The total tells me how much of my budget I spend The average tells me the price level of my selection


# Your code below
prices = [450, 1200, 320, 890, 650, 280, 1500, 720]

print("Whole list:", prices)
print("First item:", prices[0])
print("Sorted:", sorted(prices))

total = sum(prices)
average = total / len(prices)

print("Total:", total)
print("Average:", average)