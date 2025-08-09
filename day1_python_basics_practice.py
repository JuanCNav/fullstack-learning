"""
Day 1: Python Basics — Guided Practice
--------------------------------------
Run this file with:  python3 day1_python_basics_practice.py

What you'll learn today:
1) Printing to the screen
2) Variables & data types
3) Basic math & operators
4) Getting user input
5) Mini-exercises (with optional solutions at the bottom)
"""

import sys
from textwrap import dedent

def pause():
    input("\nPress Enter to continue...")

def header(title: str):
    print("\n" + "=" * 70)
    print(title)
    print("=" * 70 + "\n")

def section_printing():
    header("1) Printing to the screen")
    print("In Python, print() writes text or values to the screen.")
    print(dedent("""
        Examples:
        ---------
        print("Hello, World!")
        print(42)
        print(True)
    """))
    print("Let's run them now:")
    print("Hello, World!")
    print(42)
    print(True)
    pause()

def section_variables():
    header("2) Variables & data types")
    print("Variables store data. Think of a labeled box that holds a value.")
    name = "Juan"
    age = 24
    height = 6.3
    is_student = True
    print(dedent(f"""
        Examples (pre-filled):
        ----------------------
        name = "{name}"       -> type: {type(name).__name__}
        age = {age}           -> type: {type(age).__name__}
        height = {height}     -> type: {type(height).__name__}
        is_student = {is_student} -> type: {type(is_student).__name__}
    """))
    print("You can check a variable's type with type(value).")
    pause()

def section_math():
    header("3) Basic math & operators")
    x, y = 10, 3
    print(dedent(f"""
        With x = {x} and y = {y}:
        --------------------------
        x + y  -> {x + y}   (addition)
        x - y  -> {x - y}   (subtraction)
        x * y  -> {x * y}   (multiplication)
        x / y  -> {x / y}   (division, float)
        x // y -> {x // y}  (floor division, integer)
        x % y  -> {x % y}   (modulus, remainder)
        x ** y -> {x ** y}  (exponentiation)
    """))
    pause()

def section_input():
    header("4) Getting user input")
    print("input(prompt) pauses the program and returns what the user typed as TEXT (str).")
    print("We often convert input to numbers using int() or float().\n")
    name = input("→ What is your name? ")
    print(f"Hello, {name}! Nice to meet you.")
    while True:
        raw_age = input("→ How old are you? (number) ")
        try:
            age = int(raw_age)
            break
        except ValueError:
            print("Please enter a whole number (e.g., 24).")
    print(f"You are {age} years old.")
    pause()

def exercises():
    header("5) Mini-exercises")
    print(dedent("""
        You'll practice the following tasks:

        A) Simple Greeting
           Ask for the user's name and favorite food.
           Print: "Hello NAME, I like FOOD too!"

        B) Math with Input
           Ask for two numbers.
           Print their sum, difference, product, and quotient.

        C) Age Calculator
           Ask for a birth year.
           Calculate and print how old they are in the year 2025.

        D) Area of a Rectangle
           Ask for length and width (numbers).
           Calculate and print the area (length * width).
    """))

    # A) Simple Greeting
    print("--- A) Simple Greeting ---")
    u_name = input("Enter your name: ")
    fav_food = input("Enter your favorite food: ")
    print(f"Hello {u_name}, I like {fav_food} too!")

    # B) Math with Input
    print("\n--- B) Math with Input ---")
    def read_float(prompt):
        while True:
            s = input(prompt)
            try:
                return float(s)
            except ValueError:
                print("Please enter a valid number (e.g., 3 or 3.5).")

    a = read_float("Enter first number: ")
    b = read_float("Enter second number: ")
    print(f"Sum:        {a + b}")
    print(f"Difference: {a - b}")
    print(f"Product:    {a * b}")
    if b != 0:
        print(f"Quotient:   {a / b}")
    else:
        print("Quotient:   undefined (cannot divide by zero)")

    # C) Age Calculator
    print("\n--- C) Age Calculator ---")
    while True:
        year_raw = input("Enter your birth year (e.g., 2001): ")
        try:
            birth_year = int(year_raw)
            break
        except ValueError:
            print("Please enter a whole number like 2001.")
    current_year = 2025
    age = current_year - birth_year
    print(f"In {current_year}, you are {age} years old.")

    # D) Area of a Rectangle
    print("\n--- D) Area of a Rectangle ---")
    length = read_float("Enter length: ")
    width = read_float("Enter width: ")
    area = length * width
    print(f"Area = {length} * {width} = {area}")

    pause()

def solutions():
    header("Reference Solutions")
    print(dedent("""
    A) Simple Greeting
    ------------------
    name = input("What is your name? ")
    food = input("What is your favorite food? ")
    print(f"Hello {name}, I like {food} too!")

    B) Math with Input
    ------------------
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum:", a + b)
    print("Difference:", a - b)
    print("Product:", a * b)
    print("Quotient:", a / b if b != 0 else "undefined")

    C) Age Calculator
    -----------------
    birth_year = int(input("Enter your birth year: "))
    current_year = 2025
    age = current_year - birth_year
    print(f"In {current_year}, you are {age} years old.")

    D) Area of a Rectangle
    ----------------------
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    print("Area:", length * width)
    """))
    pause()

def main_menu():
    while True:
        header("Day 1: Python Basics — Guided Practice")
        print(dedent("""
            Choose an option:
            1) Printing to the screen
            2) Variables & data types
            3) Basic math & operators
            4) Getting user input (interactive)
            5) Mini-exercises (interactive)
            6) View reference solutions
            0) Exit
        """))
        choice = input("Enter choice: ").strip()
        if choice == "1":
            section_printing()
        elif choice == "2":
            section_variables()
        elif choice == "3":
            section_math()
        elif choice == "4":
            section_input()
        elif choice == "5":
            exercises()
        elif choice == "6":
            solutions()
        elif choice == "0":
            print("Good work today. See you tomorrow!")
            break
        else:
            print("Invalid choice. Please enter a number from the menu.")

if __name__ == "__main__":
    try:
        main_menu()
    except KeyboardInterrupt:
        print("\n\nExiting. Nice job today!")
        sys.exit(0)
