import math
import random

def play():
    user = input("r, p, s\n")
    user = user.lower()

    computer = random.choice(["r", "p", "s"])

    if user == computer:
        return (0, user, computer)

    if is_win(user, computer):
        return (1, user, computer)

    return (-1, user, computer)

def is_win(player, CPU):
    if(player == "r" and CPU == "s") or (player == "p" and CPU == "r") or (player == "s" and CPU == "p"):
        return True
    return False

def play_rounds(n):
    player_wins = 0
    computer_wins = 0
    wins_req = math.ceil(n/2)
    while player_wins < wins_req and computer_wins < wins_req:
        results, user, computer = play()

        if results == 0:
            print("{} Tie!\n".format(user))
        elif results == 1:
            player_wins += 1
            print("player {} computer {}. You won\n". format(user, computer))
        else:
            computer_wins += 1
            print("player {} computer {}. You lost :\n".format(user, computer))
        print("\n")

    if player_wins > computer_wins:
        print("You won {} rounds. congrats you beat a computer".format(n))
    else:
        print("Computer won {} rounds. Beat by a machine smh".format(n))
if __name__ == '__main__' :
    play_rounds(3)
    play_rounds(9)
