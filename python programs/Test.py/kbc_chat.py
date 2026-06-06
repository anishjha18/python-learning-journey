import random
import os

# ---------- DATASET (expand this) ----------
questions = [
    {
        "question": "What is the capital of India?",
        "options": ["A. Mumbai", "B. New Delhi", "C. Kolkata", "D. Chennai"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "Who was the first Prime Minister of India?",
        "options": ["A. Mahatma Gandhi", "B. Sardar Patel", "C. Jawaharlal Nehru", "D. Rajendra Prasad"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Which river is known as the lifeline of India?",
        "options": ["A. Yamuna", "B. Ganga", "C. Brahmaputra", "D. Godavari"],
        "answer": "B",
        "difficulty": "easy"
    },
    {
        "question": "In which year did India gain independence?",
        "options": ["A. 1942", "B. 1945", "C. 1947", "D. 1950"],
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "Which Indian state has the largest population?",
        "options": ["A. Maharashtra", "B. Bihar", "C. Uttar Pradesh", "D. West Bengal"],
        "answer": "C",
        "difficulty": "medium"
    },
    {
        "question": "Who is known as the Missile Man of India?",
        "options": ["A. Vikram Sarabhai", "B. A.P.J. Abdul Kalam", "C. Homi Bhabha", "D. C.V. Raman"],
        "answer": "B",
        "difficulty": "medium"
    },
    {
        "question": "Which Indian monument is built by Shah Jahan?",
        "options": ["A. Red Fort", "B. Qutub Minar", "C. Taj Mahal", "D. India Gate"],
        "answer": "C",
        "difficulty": "easy"
    },
    {
        "question": "Which is the national sport of India (traditionally recognized)?",
        "options": ["A. Cricket", "B. Hockey", "C. Kabaddi", "D. Football"],
        "answer": "B",
        "difficulty": "medium"
    }
]

# ---------- UTIL ----------
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

# ---------- INPUT ----------
def get_difficulty():
    print("Select Difficulty:")
    print("1. Easy  2. Medium  3. Hard")
    choice = input("Enter choice: ")

    mapping = {"1": "easy", "2": "medium", "3": "hard"}
    return mapping.get(choice, "medium")

# ---------- FILTER ----------
def get_questions_by_difficulty(diff):
    filtered = [q for q in questions if q["difficulty"] == diff]
    return filtered if filtered else questions

# ---------- DISPLAY ----------
def display_question(q, score):
    print("\n" + "="*50)
    print(f"Score: {score}")
    print("-"*50)
    print(q["question"], "\n")

    for opt in q["options"]:
        print(opt)

# ---------- VALIDATION ----------
def check_answer(q):
    while True:
        ans = input("\nEnter option (A/B/C/D): ").upper()
        if ans in ["A", "B", "C", "D"]:
            break
        print("Invalid input")

    if ans == q["answer"]:
        print("Correct\n")
        return True
    else:
        print("Wrong")
        print("Correct answer:", q["answer"])
        return False

# ---------- MAIN ----------
def main():
    clear()
    print("=== KBC INDIA QUIZ ===\n")

    difficulty = get_difficulty()
    pool = get_questions_by_difficulty(difficulty)

    random.shuffle(pool)

    score = 0

    for q in pool:
        clear()
        display_question(q, score)

        if check_answer(q):
            score += 1000
        else:
            break

    print("\nFinal Score:", score)

# ---------- RUN ----------
if __name__ == "__main__":
    main()