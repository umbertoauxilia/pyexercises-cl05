"""Exercise 5.2 — Repeating until something changes

WHAT THE PROGRAM MUST DO
    Keep asking the user something until a condition you define is met, then display a
    summary of what happened during the loop.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in?
    2. What happens to it?
    3. What comes out?
    4. What is your stop condition, what is your maximum number of attempts, and what
       does your summary contain?

WHAT THE AI CANNOT KNOW
    Your stop condition and your safety limit. An assistant asked for a while loop will
    write one that can run for ever if the user never gives the expected answer. Decide
    how many attempts you allow, and what your program does when that limit is reached.

    Accepting "Yes", "yes" and " yes " as the same answer is your decision too. Make it
    and write it down.

CHECK IT YOURSELF
    Run it and never give the expected answer. If your program is still running after
    your stated maximum, it is wrong. Then run it and answer with capitals and extra
    spaces.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In: The user's answers to the question "Do you approve the order?"
# 2. Process: The program keeps asking until the answer is "yes",or until 3 attempts are used.
# 3. Out: A summary with the number of attempts and if the order was approved.
# 4. My stop condition, my attempt limit, my summary:
#    Stop when the answer is "yes". "Yes", "yes" and " yes " count as the same,
#    because I use strip() and lower(). Maximum 3 attempts.
#    The summary shows how many attempts were used and if the order was approved.
# Your code beloww
attempts = 0
approved = False

while attempts < 3 and approved == False:
    answer = input("Do you approve the order? (yes/no): ")
    attempts = attempts + 1
    if answer.strip().lower() == "yes":
        approved = True

print("Attempts used:", attempts)
if approved:
    print("Order approved")
else:
    print("Order not approved: maximum attempts reached")