def pause():
    input("\nPress Enter to continue...")

def header(title):
    print("\n" + "="*70)
    print(title)
    print("="*70)

def demo_comparisons():
    header("1) Comparison Operators")
    print("These return True/False:")
    print("5 > 3  ->", 5 > 3)
    print("5 < 3  ->", 5 < 3)
    print("5 == 5 ->", 5 == 5)
    print("5 != 5 ->", 5 != 5)
    print("5 >= 5 ->", 5 >= 5)
    print("4 <= 5 ->", 4 <= 5)
    pause()

def demo_if_elif_else():
    header("2) if / elif / else")
    age = 16
    print(f"Example with age = {age}")
    if age < 13:
        print("-> child")
    elif age < 18:
        print("-> teen")
    else:
        print("-> adult")
    print("\nRule of thumb: test the narrow/smallest ranges first, then broader, use else for the rest.")
    pause()

def demo_logical_ops():
    header("3) Logical Operators (and / or / not)")
    temp = 25
    raining = False
    print(f"temp = {temp}, raining = {raining}")
    print("temp > 20 and not raining ->", temp > 20 and not raining)
    print("temp > 20 or  raining     ->", temp > 20 or  raining)
    print("not (temp > 30)           ->", not (temp > 30))
    pause()

def mini_project_age_access():
    header("4) Mini-Project: Age & Access Checker")
    # robust input
    while True:
        raw = input("How old are you? ")
        try:
            age = int(raw)
            if age < 0:
                print("Age can't be negative. Try again.")
                continue
            break
        except ValueError:
            print("Please enter a whole number (e.g., 18).")

    if age < 13:
        print("Access denied.")
    elif age < 18:
        print("Access granted to teen zone.")
    else:
        print("Access granted to adult zone.")
    pause()

def exercises():
    header("5) Exercises")
    print("A) Even or Odd")
    print("   Ask for a number. If divisible by 2 -> 'even', else 'odd'.")
    print("B) Grade to Letter")
    print("   Ask for a score 0–100. 90+ A, 80–89 B, 70–79 C, 60–69 D, else F.")
    print("C) Discount Eligibility")
    print("   Ask for age. If < 12 or >= 65 -> 'discount applies', else 'no discount'.")
    print("\nLet's do A interactively now:")

    # A) Even or Odd interactive
    while True:
        raw = input("Enter a whole number: ")
        try:
            n = int(raw)
            break
        except ValueError:
            print("Please enter a whole number.")
    if n % 2 == 0:
        print("even")
    else:
        print("odd")

    print("\nNow you try B and C in your editor if you want extra reps.")
    pause()

def quiz():
    header("6) Quiz (5 questions)")
    score = 0

    # Q1
    print("\nQ1) What does this print?\n   x = 10; y = 3; print(x % y)")
    ans = input("a) 0   b) 1   c) 3   d) 10  -> ").strip().lower()
    if ans == "b": score += 1

    # Q2
    print("\nQ2) Fill the teen branch so adults (18+) don't go to teen zone. Which is correct?")
    print("if age < 13: ...")
    print("elif _______: print('teen')")
    print("else: print('adult')")
    ans = input("a) age <= 18   b) age >= 13   c) age < 18   d) age > 18  -> ").strip().lower()
    if ans == "c": score += 1

    # Q3
    print("\nQ3) Which is a logical operator?")
    ans = input("a) add   b) and   c) eq   d) not_equal  -> ").strip().lower()
    if ans == "b": score += 1

    # Q4
    print("\nQ4) What does this print?\n   print( (5 > 3) and (2 > 4) )")
    ans = input("a) True   b) False   c) Error   d) None  -> ").strip().lower()
    if ans == "b": score += 1

    # Q5
    print('\nQ5) For display, which prints 6\'3"?')
    ans = input('a) print(6`3)   b) print("6\'3\\"")   c) print(6,3)   d) print("6,3")  -> ').strip().lower()
    if ans == "b": score += 1

    print(f"\nYour score: {score}/5")
    if score == 5:
        print("🔥 Perfect! You’re ready to move on.")
    elif score >= 3:
        print("Nice! Review any misses, then you’re good.")
    else:
        print("No worries—rewatch sections 1–3 and retake the quiz.")
    pause()

def main():
    while True:
        header("Day 2: Control Flow — Interactive")
        print("Choose an option:")
        print("1) Comparison operators")
        print("2) if / elif / else")
        print("3) Logical operators")
        print("4) Mini-project: Age & Access Checker")
        print("5) Exercises")
        print("6) Quiz")
        print("0) Exit")
        choice = input("Enter choice: ").strip()
        if choice == "1": demo_comparisons()
        elif choice == "2": demo_if_elif_else()
        elif choice == "3": demo_logical_ops()
        elif choice == "4": mini_project_age_access()
        elif choice == "5": exercises()
        elif choice == "6": quiz()
        elif choice == "0":
            print("Great work today. See you on Day 3!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()




