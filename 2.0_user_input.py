"""Exercise 2.0 — Asking the user

WHAT THE PROGRAM MUST DO
    Ask the user for two pieces of information, then display a sentence that uses both.

ANSWER THESE FIRST, in comments at the top of your file
    1. What goes in? The user's name and age, typed by the userThe program saves the two answers and puts them together in a sentence.
    2. What happens to it? The quantity is converted from text to a number
    3. What comes out?The name, the age, and the sentence "hi, my name is ... and my age is ..."
    4. Which two pieces of information did you choose, and for Name and age, for a registration form (e.g. a store or event sign-up

WHAT THE AI CANNOT KNOW
    Your two fields, and the sentence you want at the end. Decide both before you ask.

    One of your two values will almost certainly need to be a number. Find out what
    happens when you try to add 1 to something the user typed, and deal with it.

CHECK IT YOURSELF
    Run your program and answer with an empty line. Then with a space. Then with text
    where you expected a number. Write in a comment what happened each time.
    You are not asked to fix it yet, only to see it.

DELIVERABLE
    This file, with your comments and your code.
"""

# 1. In:The user's name and age, typed by the user.
# 2. Process:The program saves the two answers and puts them together in a sentence
# 3. Out:The name, the age, and the sentence "hi, my name is ... and my age is ..."
# 4. My two fields, and what I would do with them:Name and age, for a registration form


# Your code beloww

name = input ("enter your name:")
age = input ("enter your age:")
print(name)
print(age)

print(name,age)
print("hi,my names is "+ name + " and my age is " + age)
