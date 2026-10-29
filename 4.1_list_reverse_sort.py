"""Exercise 4.1 — Reordering without losing the original (homework)

WHAT THE PROGRAM MUST DO
    Starting from the list you built in exercise 4.0, display it in four different
    orders, and prove at the end that the original list has not been damaged.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. Which four orders did you choose, and in which of them is your original list
       modified rather than copied?

WHAT THE AI CANNOT KNOW
    That your original must survive. Some ways of reordering a list change it in place,
    others return a new one. Find out which is which, and say so in your comments.
    That distinction is the entire exercise.

CHECK IT YOURSELF
    The last line of your program must display the original list. Compare it, item by
    item, with what you wrote in 4.0. If it has moved, your program is wrong even
    though it ran.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The list of 8 prices from exercise 4.0
# 2. Process:The program creates four new lists in different orders,without changing the original list.
# 3. Out:The four lists, and at the end the original list, unchanged.
# 4. My four orders, and which ones modify the original:cheapest first, most expensive first, backwards, as text.None of them modifies the original: they all create a NEW list.sort() and reverse() would modify it, so I did not use them.


# Your code below
prices = [450, 1200, 320, 890, 650, 280, 1500, 720]

print("Cheapest first:", sorted(prices))
print("Most expensive first:", sorted(prices, reverse=True))
print("Backwards:", prices[::-1])
print("As text:", sorted(prices, key=str))

print("Original:", prices)