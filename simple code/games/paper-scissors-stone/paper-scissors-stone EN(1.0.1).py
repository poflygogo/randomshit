import random

def print_action(player:str, action:int):
    """print player's action"""
    choice = ""
    if action == 1: choice = "Scissors"
    elif action == 2: choice = "Rock"
    else: choice = "Paper"
    print(f"{player}\tchose: {choice}")

def judge(player:int, ai:int) -> str:
    """judge and return the result"""
    WIN_TABLE = (None, 2, 0, 1)
    if player == ai:
        return "DRAW!!"
    elif WIN_TABLE[player] == ai:
        return "ai WON!!"
    else:
        return f"{player_name} WON!!"
    
def ask_continue() -> bool:
    """Ask if continue to play"""
    print("-----Continue?(Y/N)-----")
    if input() in ("Y", "y"):
        return True
    else:
        print("-----End-----")
        return False
        
print("------Welcome to Rock Paper Scissors game!------")
player_name = input("Enter your name: ")  # type:str

while True:

    # player action
    print("-----Player Action Stage-----")
    while True:
        try:
            player_action = int(input("1 = Scissors\n2 = Rock\n3 = Paper\nWhat's your choice?: "))
            if 1 <= player_action <= 3:
                print()
                print_action(player_name, player_action)
                break
            else:
                print("\nALERT: Please input 1, 2 or 3\n")
        except ValueError:
            print("\nALERT: Please input integer number\n")

    # ai action
    ai_action = random.randint(1, 3)
    print_action("ai", ai_action)

    # check the result and output
    print("\n",judge(player_action, ai_action))
    
    # Ask if continue to play
    if ask_continue():
        continue
    else:
        break
