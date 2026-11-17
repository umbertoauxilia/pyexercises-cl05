"""Exercise 6.0 — Naming a piece of work

WHAT THE PROGRAM MUST DO
    Write a function that computes something useful about the list you built in exercise
    4.0, then call it three times with different inputs and display the three results.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?  (what your function receives)
    2. What happens to it?
    3. What comes out?  (what your function returns)
    4. What is your function called, and does its name say what it does without reading
       the code?

WHAT THE AI CANNOT KNOW
    What is worth computing about your data, and what to call it. A function named
    "process" or "do_stuff" fails this exercise even if it works.

    Your function must RETURN its result, not print it. Find out why that difference
    matters and write the reason in a comment. It is the whole point of the exercise.

CHECK IT YOURSELF
    Call your function with an empty list. Note what happens. Then decide whether that
    behaviour is acceptable, and say so in a comment.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:
# 2. Process:
# 3. Out:
# 4. My function name, and why return rather than print:


# Your code below
# My list from exercise 4.0: prices in euros of 8 menswear items
prices = [450, 1200, 320, 890, 650, 280, 1500, 720]


# Counts how many prices are above the limit and RETURNS the number
def count_above_limit(prices, limit):
    # The counter starts at 0
    count = 0
    # Look at every price in the list
    for price in prices:
        # Only if this price is above the limit, add 1 to the counter
        if price > limit:
            count = count + 1
    # Send the result back to whoever called the function
    return count
# I call the function three times with three different limits
result_500 = count_above_limit(prices, 500)
result_1000 = count_above_limit(prices, 1000)
result_1400 = count_above_limit(prices, 1400)

# I print each result with a label, so the reader knows what the number means
print("Above 500:", result_500)      # expected: 5
print("Above 1000:", result_1000)    # expected: 2
print("Above 1400:", result_1400)    # expected: 1