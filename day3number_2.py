import random

def get_int(prompt):
    """Ask until user types whole number."""
    while True:
        raw = input(prompt).strip()
        try:
            return int(raw)
        except ValueError:
            print("please enter a whole numer eg, 6, 7...")
            continue
def play_one_round(max_tries=7, low=1, high=20, show_secret=False):
    secret= random.randint(low, high)
    if show_secret:
            print(f"[dev] secret={secret}")
    tries=0

    print(f"\nI am of a number from {low} to {high}. you have {max_tries} tries")

    while tries<max_tries:
        guess=get_int (f"Guess #{tries+1}: ")

        if guess<low or guess>high:
            print(f"stay between {low} and {high}. That guess does not count.")
            continue
        tries+=1
        if guess==secret:
             print(f"Correct🎉! The number was {secret}. You won in {tries} tries")
             return True, tries
        diff = abs(guess - secret)
        if diff <=2:
             hint= "very close"
        elif diff<=5:
             hint= "close"
        else:
             hint= "far"
        if guess< secret:
             print(f"too low. {hint}")
        else:
             print(f"too high. {hint}")
             
    print(f"Out of tries! The number was {secret}")
    return False, tries
if __name__ == "__main__":
    play_one_round()
    