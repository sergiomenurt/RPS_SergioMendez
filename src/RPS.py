import random
from enum import IntEnum


class GameAction(IntEnum):
    Rock = 0
    Paper = 1
    Scissors = 2


class GameResult(IntEnum):
    Victory = 0
    Defeat = 1
    Tie = 2


Victories = {
    GameAction.Rock: GameAction.Paper,
    GameAction.Paper: GameAction.Scissors,
    GameAction.Scissors: GameAction.Rock
}

user_history = []


def assess_game(user_action, computer_action):
    if user_action == computer_action:
        print(f"User and computer picked {user_action.name}. Draw game!")
        return GameResult.Tie
    elif Victories[user_action] == computer_action:
        print(f"{user_action.name} beats {computer_action.name}. You won!")
        return GameResult.Victory
    else:
        print(f"{computer_action.name} beats {user_action.name}. You lost!")
        return GameResult.Defeat


def get_computer_action():
    if len(user_history) < 3:
        computer_selection = random.randint(0, len(GameAction) - 1)
    else:
        user_last_move = user_history[-1]
        computer_selection = Victories[user_last_move].value
    computer_action = GameAction(computer_selection)
    print(f"Computer picked {computer_action.name}.")
    return computer_action


def get_user_action():
    game_choices = [f"{game_action.name}[{game_action.value}]" for game_action in GameAction]
    game_choices_str = ", ".join(game_choices)
    user_selection = int(input(f"\nPick a choice ({game_choices_str}): "))
    return GameAction(user_selection)


def play_another_round():
    another_round = input("\nAnother round? (y/n): ")
    return another_round.lower() == 'y'


def main():
    while True:
        try:
            user_action = get_user_action()
        except ValueError:
            range_str = f"[0, {len(GameAction) - 1}]"
            print(f"Invalid selection. Pick a choice in range {range_str}!")
            continue

        user_history.append(user_action)

        computer_action = get_computer_action()
        assess_game(user_action, computer_action)

        if not play_another_round():
            break


if __name__ == "__main__":
    main()
