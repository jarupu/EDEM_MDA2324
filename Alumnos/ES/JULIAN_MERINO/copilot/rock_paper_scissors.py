import random

def game():
    # game choices
    choices = ['rock', 'paper', 'scissors', 'lizard', 'spock']

    # game rules
    rules = {
        'rock': ['scissors', 'lizard'],
        'paper': ['rock', 'spock'],
        'scissors': ['paper', 'lizard'],
        'lizard': ['spock', 'paper'],
        'spock': ['scissors', 'rock']
    }

    # outcome count
    outcomes = {
        'rock': 0,
        'paper': 0,
        'scissors': 0,
        'lizard': 0,
        'spock': 0
    }

    for _ in range(1000):
        # player's choice
        player = random.choice(choices)

        # computer's choice
        computer = random.choice(choices)

        # determine the winner
        if player == computer:
            outcomes[player] += 1
        elif computer in rules[player]:
            outcomes[player] += 1
        else:
            outcomes[computer] += 1

    # print the number of outcomes for each option
    for choice, count in outcomes.items():
        print(f"{choice}: {count}")

game()