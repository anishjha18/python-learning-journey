import random
import os
import time

# ---------- DATASET ----------
# Structure: [Question, Opt1, Opt2, Opt3, Opt4, Correct_Index, Level]
QUESTIONS_POOL = [
    ["Which of these is the national bird of India?", "Parrot", "Peacock", "Eagle", "Sparrow", 1, 1],
    ["How many states are there in India currently?", "25", "29", "28", "30", 2, 1],
    ["Which city is known as the 'Pink City' of India?", "Jodhpur", "Jaipur", "Udaipur", "Bhopal", 1, 2],
    ["Who is the author of 'Wings of Fire'?", "A.P.J. Abdul Kalam", "V.S. Naipaul", "R.K. Narayan", "Amartya Sen", 0, 2],
    ["Which is the highest civilian award in India?", "Padma Vibhushan", "Param Vir Chakra", "Bharat Ratna", "Padma Bhushan", 2, 3],
    ["Which planet is known as the Red Planet?", "Venus", "Mars", "Jupiter", "Saturn", 1, 3],
    ["The 2024 Olympic Games were held in which city?", "Tokyo", "Los Angeles", "Paris", "London", 2, 4],
    ["Who was the first woman Prime Minister of India?", "Pratibha Patil", "Sarojini Naidu", "Indira Gandhi", "Sushma Swaraj", 2, 4],
    ["Which element's chemical symbol is 'Au'?", "Silver", "Aluminum", "Argon", "Gold", 3, 5],
    ["In which year did the Quit India Movement start?", "1930", "1942", "1919", "1945", 1, 5],
]

MONEY_TREE = [0, 1000, 2000, 3000, 5000, 10000, 20000, 40000, 80000, 160000, 320000]
MILESTONES = {5: 10000, 10: 320000} # Safe zones

class KBCGame:
    def __init__(self):
        self.money_idx = 0
        self.lifelines = {"50:50": True, "Flip": True}
        self.current_pool = list(QUESTIONS_POOL)
        random.shuffle(self.current_pool)

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def draw_ui(self, q_text, options, q_num):
        print("═" * 60)
        print(f"║ {'KAUN BANEGA CROREPATI':^56} ║")
        print("═" * 60)
        print(f" QUESTION {q_num}/10 | Current: ₹{MONEY_TREE[self.money_idx]:,} | Next: ₹{MONEY_TREE[self.money_idx+1]:,}")
        print("-" * 60)
        print(f"\n Q: {q_text}\n")
        
        labels = ['A', 'B', 'C', 'D']
        for i in range(4):
            print(f"   {labels[i]}. {options[i]}")
        print("-" * 60)
        
        available = [name for name, status in self.lifelines.items() if status]
        print(f" Lifelines Available: {', '.join(available) if available else 'NONE'}")
        print(" (Enter A/B/C/D or '50' for 50:50, 'F' for Flip, 'Q' to Quit)")

    def play(self):
        q_count = 1
        while q_count <= 10:
            q_data = self.current_pool.pop(0)
            q_text, opts, correct_idx = q_data[0], q_data[1:5], q_data[5]
            
            while True:
                self.clear_screen()
                self.draw_ui(q_text, opts, q_count)
                choice = input("\nYour Answer: ").strip().upper()

                # Lifeline: 50:50
                if choice == "50" and self.lifelines["50:50"]:
                    self.lifelines["50:50"] = False
                    wrong_indices = [i for i in range(4) if i != correct_idx]
                    for idx in random.sample(wrong_indices, 2):
                        opts[idx] = "--------"
                    continue
                
                # Lifeline: Flip
                elif choice == "F" and self.lifelines["Flip"]:
                    self.lifelines["Flip"] = False
                    q_data = self.current_pool.pop() # Take from end of shuffled list
                    q_text, opts, correct_idx = q_data[0], q_data[1:5], q_data[5]
                    continue

                # Quit Game
                elif choice == "Q":
                    print(f"\nYou decided to quit. You take home: ₹{MONEY_TREE[self.money_idx]:,}")
                    return

                # Validate Answer
                labels = ['A', 'B', 'C', 'D']
                if choice in labels:
                    if labels.index(choice) == correct_idx:
                        self.money_idx += 1
                        print(f"\n★★★ SAHI JAWAB! You won ₹{MONEY_TREE[self.money_idx]:,} ★★★")
                        time.sleep(1.5)
                        break
                    else:
                        # Game Over Logic
                        winnings = 0
                        for m in sorted(MILESTONES.keys(), reverse=True):
                            if q_count > m:
                                winnings = MILESTONES[m]
                                break
                        print(f"\nGALAT JAWAB! The correct answer was {labels[correct_idx]}.")
                        print(f"You dropped down to the last milestone. Final Prize: ₹{winnings:,}")
                        return
                else:
                    print("Invalid input! Try again.")
                    time.sleep(1)

            q_count += 1

        print("\n" + "█"*60)
        print(f"CONGRATULATIONS! YOU ARE THE ULTIMATE WINNER!")
        print(f"FINAL PRIZE: ₹{MONEY_TREE[-1]:,}")
        print("█"*60)

if __name__ == "__main__":
    game = KBCGame()
    game.play()