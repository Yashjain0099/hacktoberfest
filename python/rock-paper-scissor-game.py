import random

print("Hello, welcome to Rock, Paper, Scissors!")
print("Just so you know, I will win!")
print("Enter rock, paper, or scissors")

# Game loop
while True:
    user = input("Choose rock, paper, or scissors: ").lower()
    
    # Validate user input
    if user not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose rock, paper, or scissors.")
        continue

    # Computer choice
    computer_choice = random.choice(["rock", "paper", "scissors"])
    print(f"I chose {computer_choice}.")

    # Determine the winner
    if user == computer_choice:
        print("It's a tie! Try again.")
    elif (user == "rock" and computer_choice == "scissors") or \
         (user == "paper" and computer_choice == "rock") or \
         (user == "scissors" and computer_choice == "paper"):
        print("You win!")
        break
    else:
        print("I win! Try again.")
