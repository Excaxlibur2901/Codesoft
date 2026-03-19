import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

def get_winner(user, computer):
    if user == computer:
        return "tie"
    elif (user == "rock" and computer == "scissors") or \
         (user == "scissors" and computer == "paper") or \
         (user == "paper" and computer == "rock"):
        return "user"
    else:
        return "computer"

while True:
    print("\n--- Rock Paper Scissors ---")
    print("Choices: rock, paper, scissors")
    print("Type 'exit' to quit")

    user_choice = input("Enter your choice: ").lower()

    if user_choice == "exit":
        print("Game exited.")
        break

    if user_choice not in choices:
        print("Invalid choice. Try again.")
        continue

    computer_choice = random.choice(choices)

    print(f"You chose: {user_choice}")
    print(f"Computer chose: {computer_choice}")

    result = get_winner(user_choice, computer_choice)

    if result == "tie":
        print("It's a tie!")
    elif result == "user":
        print("You win!")
        user_score += 1
    else:
        print("Computer wins!")
        computer_score += 1

    print(f"Score -> You: {user_score} | Computer: {computer_score}")

    