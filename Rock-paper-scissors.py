import random
victories = 0
defeats = 0
ties = 0
while True:
    user_action = input("rock, paper or scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print(f"\nYou selected {user_action}, the computer selected {computer_action}.\n")
    if user_action == computer_action:
        print(f"Both players selected {user_action}. Is a tie!")
        ties=ties+1
    elif user_action == "rock":
        if computer_action == "scissors":
            print("rock smash scissors! You win!")
            victories=victories+1
        else:
            print("paper covers rock! You lose.")
            defeats=defeats+1
    elif user_action == "paper":
        if computer_action == "rock":
            print("paper covers rock! You win!")
            victories=victories+1
        else:
            print("scissors cut paper! You lose.")
            defeats=defeats+1
    elif user_action == "scissors":
        if computer_action == "paper":
            print("scissors cut paper! You win!")
            victories=victories+1
        else:
            print("rock smash scissors! You lose.")
            defeats=defeats+1
    print(f"victories: {victories}")
    print(f"defeats : {defeats}")
    print(f"ties: {ties}")
    play_again = input("Play again? (y/n): ")
    if play_again.lower() != "y":
        break