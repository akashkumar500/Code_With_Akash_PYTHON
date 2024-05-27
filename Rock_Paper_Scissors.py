import random

while True:
    print("Let's play Rock, Paper, Scissors!")
    user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    while user_choice not in ['rock', 'paper', 'scissors']:
        print("Invalid choice. Please enter rock, paper, or scissors.")
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()

    computer_choice = random.choice(['rock', 'paper', 'scissors'])

    print(f"You chose {user_choice}.")
    print(f"The computer chose {computer_choice}.")

    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer wins!")

    while True:
        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again in ['yes', 'no']:
            break
        else:
            print("Invalid input. Please enter 'yes' or 'no'.")

    if play_again != 'yes':
        break
       
print("Thank you for playing.")
