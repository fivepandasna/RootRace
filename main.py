import random
import math
import time

def clear_screen():
    """Clear the terminal screen."""
    print("\n" * 50)

def print_slowly(text, delay=0.024):
    """Print text with a slight delay between characters."""
    for char in text:
        print(char, end='', flush=True)
        time.sleep(delay)
    print()

def main():
    """Main game function."""
    score = 0
    streak = 0
    
    print_slowly("======= ROOT RACE =======")
    print_slowly("Find the square root of random numbers between 1-100.")
    print_slowly("Each correct digit: +500 points with streak multiplier")
    print_slowly("Each wrong guess: -250 points")
    print_slowly("Streak bonus: +10% per consecutive correct digit")
    print_slowly("Press Enter to start...")
    input()
    
    while True:
        # Generate a random number between 1 and 100
        number = random.randint(1, 100)
        square_root = math.sqrt(number)
        
        # Format the square root to a string with at least 6 decimal places
        square_root_str = f"{square_root:.6f}"
        if square_root == int(square_root):
            square_root_str = f"{int(square_root)}.0"
        
        # Remove trailing zeros after decimal point
        if '.' in square_root_str:
            square_root_str = square_root_str.rstrip('0').rstrip('.')
        
        # Initialize variables for this round
        correct_part = ""
        round_score = 0
        wrong_guesses = 0
        
        clear_screen()
        print_slowly(f"Find the square root of {number}:")
        
        # For each digit in the square root
        for i, correct_digit in enumerate(square_root_str):
            if correct_digit == '.':
                correct_part += '.'
                print_slowly(f"Current progress: {correct_part}")
                continue
                
            while True:
                if i == 0:
                    prompt = "Enter the first digit: "
                elif correct_part[-1] == '.':
                    prompt = "Enter the first decimal digit: "
                else:
                    prompt = "Enter the next digit: "
                
                try:
                    guess = input(prompt)
                    
                    # Check if the input is valid (a single digit or period)
                    if not (guess.isdigit() and len(guess) == 1):
                        print_slowly("Please enter a single digit (0-9).")
                        continue
                        
                    if guess == correct_digit:
                        correct_part += guess
                        
                        # Calculate points with streak bonus
                        multiplier = 1 + (streak * 0.1)
                        points_earned = round(500 * multiplier)
                        
                        print_slowly(f"Correct! +{points_earned} points (500 × {multiplier:.1f} streak multiplier)")
                        round_score += points_earned
                        
                        # Increase streak for next digit
                        streak += 1
                        print_slowly(f"Current progress: {correct_part} | Streak: {streak}")
                        break
                    else:
                        wrong_guesses += 1
                        # Reset streak on wrong guess
                        streak = 0
                        print_slowly(f"Wrong! Try again. (-250 points) | Streak reset to 0")
                except ValueError:
                    print_slowly("Invalid input. Please enter a single digit.")
        
        # Calculate final score for this round
        round_penalty = wrong_guesses * 250
        round_final_score = max(0, round_score - round_penalty)
        
        print_slowly(f"\nCorrect! The square root of {number} is {square_root_str}")
        print_slowly(f"Round score: {round_score} points - {round_penalty} penalty = {round_final_score}")
        print_slowly(f"Current streak: {streak}")
        
        score += round_final_score
        print_slowly(f"Total score: {score}")
        
        play_again = input("\nPlay again? (y/n): ").lower()
        if play_again != 'y':
            print_slowly(f"Thanks for playing! Final score: {score}")
            break

if __name__ == "__main__":
    main()