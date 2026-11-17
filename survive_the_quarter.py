# Umberto Auxilia, group A

#
# Feature chosen: (a) streak bonus.
# Why: it only needs one counter, and it rewards the player for playing well three days in a row.
# Rule: 3 moves in a row with impact above 0 give +5 reputation (max 100), then the streak restarts.
#
# 1. What goes in?
#    scenarios_A.csv (comma separator, 14 columns, one scenario per line, 33 scenarios with my 3 new ones),
#    the player's name and one letter A, B or C each day.
# 2. What happens?
#    The file is read with the csv module, the options become tuples (text, budget, reputation, feedback).
#    The scenarios are shuffled and the game runs for 10 days. Each choice changes budget and reputation.
#    The game stops at once if budget or reputation is 0 or less. A history of tuples keeps every move.
# 3. What comes out?
#    A screen for each day, the feedback of each choice, the final score (reputation + budget // 200),
#    the title, the best and the worst move, and one new line in results.csv.
# 4. What could go wrong, and what I decided?
#    - The player types something else than A, B or C: the game asks again (strip and upper too).
#    - Budget or reputation reaches 0: "You are fired!" and the game stops at once; title "Fired".
#    - The reputation goes above 100: I cap it at 100.
#    - The scenarios file is missing: a clear message, no crash.
#    - The player leaves the name empty: the game asks again.
#    - results.csv: I add a line at each game (append), the header is written only the first time.
#
# What is missing: nothing known.

import csv
import os
import random
from datetime import date


# Reads the scenarios file and returns a list: one (situation, options) pair per scenario
def load_scenarios(path):
    # Empty list that will hold all the scenarios
    scenarios = []
    # Open the file; utf-8-sig handles special characters
    with open(path, newline="", encoding="utf-8-sig") as f:
        # DictReader gives every row as a dictionary, using the column names as keys
        reader = csv.DictReader(f)
        # Go through every row of the file
        for row in reader:
            # Option A: a tuple with text, budget change, reputation change, feedback
            option_a = (row["OptionA"], int(row["BudgetA"]), int(row["ReputationA"]), row["FeedbackA"])
            # Option B, same structure
            option_b = (row["OptionB"], int(row["BudgetB"]), int(row["ReputationB"]), row["FeedbackB"])
            # Option C, same structure
            option_c = (row["OptionC"], int(row["BudgetC"]), int(row["ReputationC"]), row["FeedbackC"])
            # One scenario = the situation and the list of its three options
            scenario = (row["Scenario"], [option_a, option_b, option_c])
            scenarios.append(scenario)
    return scenarios


# Asks the player for A, B or C and keeps asking until the answer is valid
def ask_choice():
    # Start with an empty choice, so the loop runs at least once
    choice = ""
    # Repeat while the choice is not one of the valid letters
    while choice not in ["A", "B", "C"]:
        # Ask, remove the spaces around and use capitals, so "b" is accepted
        choice = input("Your choice (A, B or C): ").strip().upper()
        # If it is still not valid, tell the player
        if choice not in ["A", "B", "C"]:
            print("Please type A, B or C:")
    # Send the valid letter back
    return choice


# Applies the chosen option to the two gauges and returns the new values as a tuple
def apply_choice(budget, reputation, option):
    # In the option tuple, position 1 is the budget change and position 2 the reputation change
    budget_change = option[1]
    reputation_change = option[2]
    # Add both changes to the current values
    budget += budget_change
    reputation += reputation_change
    # The reputation can never go above 100
    if reputation > 100:
        reputation = 100
    # Return two values: Python packs them in a tuple
    return budget, reputation


# Prints the screen of one day: title, the two gauges, the situation and the three options
def show_day(day, budget, reputation, situation, options):
    # Empty line to separate the days
    print()
    # Day title
    print(f"--- Day {day} ---")
    # The two gauges
    print(f"[Budget: {budget} EUR | Reputation: {reputation}/100]")
    # The situation of the day
    print(situation)
    # The letters used to label the options
    letters = ["A", "B", "C"]
    # Go through the options with their position (0, 1, 2)
    for i, option in enumerate(options):
        # Position 0 of the tuple is the text of the option
        print(f"{letters[i]}: {option[0]}")


# Plays one full game of 10 days and returns the final budget, reputation, if the player was fired and the history
def play_game(scenarios):
    # Mix the scenarios in place, so every game is different
    random.shuffle(scenarios)
    # Starting values of the two gauges
    budget = 10000
    reputation = 50
    # The player is not fired at the start
    fired = False
    # Empty list that will hold one tuple per day
    history = []
    # Counter of good moves in a row, for the streak bonus
    streak = 0
    # The letters, to turn "A", "B", "C" into the positions 0, 1, 2
    letters = ["A", "B", "C"]
    # One loop turn per day, from day 1 to day 10
    for day in range(1, 11):
        # Take the scenario of this day: the situation and its 3 options
        situation, options = scenarios[day - 1]
        # Show the screen of the day
        show_day(day, budget, reputation, situation, options)
        # Ask the player for A, B or C
        choice = ask_choice()
        # Find the chosen option in the list (A is position 0, B is 1, C is 2)
        option = options[letters.index(choice)]
        # Update the gauges: the function returns two values, unpacked here
        budget, reputation = apply_choice(budget, reputation, option)
        # Impact of the move, with the same formula as the final score
        impact = option[2] + option[1] // 200
        # Save the day as a tuple; impact is first, so max() and min() compare it first
        history.append((impact, day, option[0]))
        # Show the feedback of the chosen option (position 3 of the tuple)
        print(option[3])
        # If one gauge reaches zero or less, the player is fired and the loop stops at once
        if budget <= 0 or reputation <= 0:
            fired = True
            print("You are fired!")
            break
        # Streak bonus: a good move has an impact above 0
        if impact > 0:
            # One more good move in a row
            streak += 1
        else:
            # A bad move: the streak starts again
            streak = 0
        # Three good moves in a row: bonus
        if streak == 3:
            # +5 reputation, but never above 100
            reputation += 5
            if reputation > 100:
                reputation = 100
            # The streak starts again
            streak = 0
            print("Streak bonus! 3 good moves in a row: +5 reputation.")
    # Send back the final values, if the player was fired, and the history
    return budget, reputation, fired, history


# Returns the best and the worst move of the game as two tuples
def best_and_worst(history):
    # max() compares the tuples element by element: the highest impact wins
    best = max(history)
    # min() does the same and finds the lowest impact
    worst = min(history)
    # Return two values (a tuple)
    return best, worst


# Calculates the final score: reputation plus one point every 200 EUR of budget
def calculate_score(budget, reputation):
    # // is the whole division: 9200 // 200 = 46
    return reputation + budget // 200


# Returns the title that goes with the final score
def get_title(score):
    # Below 95
    if score < 95:
        return "Eternal Intern"
    # From 95 to 119
    elif score < 120:
        return "Growth Hacker"
    # From 120 to 139
    elif score < 140:
        return "CMO Material"
    # 140 or more
    else:
        return "Viral Legend"


# Adds one line to results.csv; the header is written only when the file is new
def save_result(name, budget, reputation, title):
    # True if the file does not exist yet
    is_new = not os.path.exists("results.csv")
    # "a" = append: the old lines stay, a new one is added at the end
    with open("results.csv", "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        # Header only the first time
        if is_new:
            writer.writerow(["name", "budget", "reputation", "title", "date"])
        # One line: name, budget, reputation, title, today's date
        writer.writerow([name, budget, reputation, title, date.today()])


# The whole game, in order: load, play, show the result, save it
def main():
    # Stop with a clear message if the scenarios file is missing
    if not os.path.exists("scenarios_A.csv"):
        print("File not found: scenarios_A.csv - put it in the same folder as this program.")
        return
    # Load the scenarios
    scenarios = load_scenarios("scenarios_A.csv")
    # Ask the name and keep asking if it is empty
    name = input("Your name: ").strip()
    while name == "":
        name = input("The name cannot be empty. Your name: ").strip()
    # Play the 10 days: four values come back, unpacked here
    budget, reputation, fired, history = play_game(scenarios)
    print()
    # If the player was fired, say why; otherwise show score and title
    if fired:
        title = "Fired"
        if budget <= 0:
            print(name + ", you are fired: the budget is finished.")
        else:
            print(name + ", you are fired: nobody trusts you anymore.")
    else:
        score = calculate_score(budget, reputation)
        title = get_title(score)
        print(f"{name}, you survived! Score: {score}, title: {title}")
    # Best and worst move of the game
    best, worst = best_and_worst(history)
    print("Best move: day", best[1], "-", best[2], "(impact", best[0], ")")
    print("Worst move: day", worst[1], "-", worst[2], "(impact", worst[0], ")")
    # Save the result
    save_result(name, budget, reputation, title)
    print("Result saved in results.csv")


# Start the game only when this file is run directly
if __name__ == "__main__":
    main()
