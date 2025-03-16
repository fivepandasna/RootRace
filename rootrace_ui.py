import random
import math
import tkinter as tk
from tkinter import messagebox, font

class SquareRootGame:
    def __init__(self, root):
        self.root = root
        self.root.title("Square Root Guessing Game")
        self.root.geometry("600x500")
        self.root.resizable(False, False)
        self.root.configure(bg="#2c3e50")
        
        # Game variables
        self.score = 0
        self.streak = 0
        self.round_score = 0
        self.wrong_guesses = 0
        self.correct_part = ""
        self.current_index = 0
        self.current_number = None
        self.square_root_str = None
        self.game_active = False
        
        # Fonts
        title_font = font.Font(family="Helvetica", size=18, weight="bold")
        info_font = font.Font(family="Helvetica", size=12)
        button_font = font.Font(family="Helvetica", size=10, weight="bold")
        digit_font = font.Font(family="Courier", size=14, weight="bold")
        
        # Title
        self.title_label = tk.Label(root, text="SQUARE ROOT GUESSING GAME", 
                              font=title_font, bg="#2c3e50", fg="#ecf0f1")
        self.title_label.pack(pady=15)
        
        # Game info frame
        self.info_frame = tk.Frame(root, bg="#34495e", padx=10, pady=10)
        self.info_frame.pack(fill=tk.X, padx=20)
        
        # Number to guess
        self.number_label = tk.Label(self.info_frame, text="Number: --", 
                                font=info_font, bg="#34495e", fg="#ecf0f1")
        self.number_label.grid(row=0, column=0, sticky="w", pady=5)
        
        # Score display
        self.score_label = tk.Label(self.info_frame, text="Score: 0", 
                              font=info_font, bg="#34495e", fg="#ecf0f1")
        self.score_label.grid(row=0, column=1, sticky="e", pady=5, padx=10)
        
        # Streak display
        self.streak_label = tk.Label(self.info_frame, text="Streak: 0", 
                               font=info_font, bg="#34495e", fg="#ecf0f1")
        self.streak_label.grid(row=1, column=0, sticky="w", pady=5)
        
        # Round score display
        self.round_score_label = tk.Label(self.info_frame, text="Round Score: 0", 
                                    font=info_font, bg="#34495e", fg="#ecf0f1")
        self.round_score_label.grid(row=1, column=1, sticky="e", pady=5, padx=10)
        
        # Progress display
        self.progress_frame = tk.Frame(root, bg="#2c3e50", padx=10, pady=10)
        self.progress_frame.pack(fill=tk.X, padx=20, pady=20)
        
        self.progress_label = tk.Label(self.progress_frame, text="Current Progress:", 
                                 font=info_font, bg="#2c3e50", fg="#ecf0f1")
        self.progress_label.pack(anchor="w")
        
        self.progress_display = tk.Label(self.progress_frame, text="", 
                                   font=digit_font, bg="#2c3e50", fg="#2ecc71", 
                                   height=2)
        self.progress_display.pack(fill=tk.X)
        
        # Message display
        self.message_var = tk.StringVar()
        self.message_var.set("Press 'Start Game' to begin!")
        self.message_label = tk.Label(root, textvariable=self.message_var, 
                                font=info_font, bg="#2c3e50", fg="#f39c12", 
                                wraplength=550, height=2)
        self.message_label.pack(pady=10)
        
        # Input frame
        self.input_frame = tk.Frame(root, bg="#2c3e50")
        self.input_frame.pack(pady=10)
        
        self.input_label = tk.Label(self.input_frame, text="Enter digit:", 
                              font=info_font, bg="#2c3e50", fg="#ecf0f1")
        self.input_label.grid(row=0, column=0, padx=5)
        
        self.input_var = tk.StringVar()
        self.input_entry = tk.Entry(self.input_frame, textvariable=self.input_var, 
                              font=digit_font, width=3, justify='center')
        self.input_entry.grid(row=0, column=1, padx=5)
        self.input_entry.bind('<Return>', self.check_guess)
        self.input_entry.config(state='disabled')
        
        self.submit_button = tk.Button(self.input_frame, text="Submit", 
                                 font=button_font, bg="#3498db", fg="#ffffff",
                                 command=self.check_guess, state='disabled')
        self.submit_button.grid(row=0, column=2, padx=5)
        
        # Button frame
        self.button_frame = tk.Frame(root, bg="#2c3e50")
        self.button_frame.pack(pady=15)
        
        self.start_button = tk.Button(self.button_frame, text="Start Game", 
                                font=button_font, bg="#2ecc71", fg="#ffffff",
                                width=15, height=2, command=self.start_game)
        self.start_button.grid(row=0, column=0, padx=10)
        
        self.quit_button = tk.Button(self.button_frame, text="Quit", 
                              font=button_font, bg="#e74c3c", fg="#ffffff",
                              width=15, height=2, command=self.root.quit)
        self.quit_button.grid(row=0, column=1, padx=10)
        
        # Instructions
        self.instructions_label = tk.Label(root, text=
            "• Find the square root of the given number digit by digit\n"
            "• Each correct digit: +500 points with streak bonus\n"
            "• Each wrong guess: -250 points\n"
            "• Streak bonus: +10% per consecutive correct digit",
            font=info_font, bg="#2c3e50", fg="#bdc3c7", justify="left")
        self.instructions_label.pack(pady=10)
    
    def start_game(self):
        """Start a new round of the game."""
        # Reset round variables
        self.round_score = 0
        self.wrong_guesses = 0
        self.correct_part = ""
        self.current_index = 0
        
        # Generate a random number between 1 and 100
        self.current_number = random.randint(1, 100)
        square_root = math.sqrt(self.current_number)
        
        # Format the square root to a string with decimal places
        self.square_root_str = f"{square_root:.6f}"
        if square_root == int(square_root):
            self.square_root_str = f"{int(square_root)}.0"
        
        # Remove trailing zeros after decimal point
        if '.' in self.square_root_str:
            self.square_root_str = self.square_root_str.rstrip('0').rstrip('.')
        
        # Update UI
        self.number_label.config(text=f"Number: {self.current_number}")
        self.progress_display.config(text="")
        self.message_var.set("Game started! Enter the first digit of the square root.")
        
        # Enable input
        self.input_entry.config(state='normal')
        self.submit_button.config(state='normal')
        self.input_var.set("")
        self.input_entry.focus_set()
        
        # Change start button to next round
        self.start_button.config(text="New Number", state='disabled')
        
        self.game_active = True
    
    def check_guess(self, event=None):
        """Check if the entered digit is correct."""
        if not self.game_active:
            return
        
        # Get current digit to guess
        if self.current_index >= len(self.square_root_str):
            self.finish_round()
            return
        
        correct_digit = self.square_root_str[self.current_index]
        
        # If it's a decimal point, add it automatically and move to next digit
        if correct_digit == '.':
            self.correct_part += '.'
            self.current_index += 1
            self.progress_display.config(text=self.correct_part)
            
            if self.current_index < len(self.square_root_str):
                correct_digit = self.square_root_str[self.current_index]
            else:
                self.finish_round()
                return
        
        # Get the user's guess
        guess = self.input_var.get().strip()
        
        # Validate input
        if not (guess.isdigit() and len(guess) == 1):
            self.message_var.set("Please enter a single digit (0-9).")
            self.input_var.set("")
            self.input_entry.focus_set()
            return
        
        # Check if guess is correct
        if guess == correct_digit:
            # Calculate points with streak bonus
            multiplier = 1 + (self.streak * 0.1)
            points_earned = round(500 * multiplier)
            
            # Update UI
            self.round_score += points_earned
            self.correct_part += guess
            self.current_index += 1
            
            # Increase streak
            self.streak += 1
            
            # Update displays
            self.progress_display.config(text=self.correct_part)
            self.streak_label.config(text=f"Streak: {self.streak}")
            self.round_score_label.config(text=f"Round Score: {self.round_score}")
            
            # Next prompt
            if self.current_index < len(self.square_root_str):
                if self.square_root_str[self.current_index] == '.':
                    self.correct_part += '.'
                    self.current_index += 1
                    self.progress_display.config(text=self.correct_part)
                
                if self.current_index == 0:
                    prompt = "Enter the first digit:"
                elif self.correct_part[-1] == '.':
                    prompt = "Enter the first decimal digit:"
                else:
                    prompt = "Enter the next digit:"
                
                self.message_var.set(f"Correct! +{points_earned} points (500 × {multiplier:.1f} streak multiplier)\n{prompt}")
            else:
                self.finish_round()
                return
        else:
            # Wrong guess
            self.wrong_guesses += 1
            self.streak = 0
            self.streak_label.config(text=f"Streak: {self.streak}")
            self.message_var.set(f"Wrong! Try again. (-250 points) | Streak reset to 0")
        
        # Clear input for next digit
        self.input_var.set("")
        self.input_entry.focus_set()
    
    def finish_round(self):
        """End the current round and update the final score."""
        # Calculate final score for this round
        round_penalty = self.wrong_guesses * 250
        round_final_score = max(0, self.round_score - round_penalty)
        
        # Update total score
        self.score += round_final_score
        
        # Update UI
        self.score_label.config(text=f"Score: {self.score}")
        self.round_score_label.config(text=f"Round Score: {round_final_score}")
        
        # Show completion message
        self.message_var.set(
            f"Correct! The square root of {self.current_number} is {self.square_root_str}\n"
            f"Round score: {self.round_score} points - {round_penalty} penalty = {round_final_score}"
        )
        
        # Disable input
        self.input_entry.config(state='disabled')
        self.submit_button.config(state='disabled')
        self.start_button.config(state='normal')
        
        self.game_active = False

# Create and run the application
if __name__ == "__main__":
    root = tk.Tk()
    game = SquareRootGame(root)
    root.mainloop()