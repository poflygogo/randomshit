import random

def print_action(player:str, action:int):
    """輸出玩家行動結果"""
    choice = ""
    if action == 1: choice = "剪刀"
    elif action == 2: choice = "石頭"
    else: choice = "布"
    print(f"{player}\t出拳: {choice}")

print("------歡迎來到剪刀石頭布小遊戲------")
player_name = input("請輸入您的名字: ")  # type:str

while True:

    # 玩家行動
    print("-----玩家行動階段-----")
    while True:
        player_action = input("1 = 剪刀\n2 = 石頭\n3 = 布\n你想出什麼?: ")
        if player_action.isdigit() and 1 <= int(player_action) <= 3:
            player_action = int(player_action)
            print_action(player_name, player_action)
            break
        else:
            print("注意: 無效輸入，請重新輸入")

    # ai行動
    ai_action = random.randint(1, 3)
    print_action("ai", ai_action)

    # 檢查結果並輸出
    print()     # 空一行
    if player_action == ai_action:
        print("平手")
    elif player_action == 1:
        if ai_action == 2:
            print("ai 勝利!!")
        else:
            print(f"{player_name} 勝利!!")
    elif player_action == 2:
        if ai_action == 3:
            print("ai 勝利")
        else:
            print(f"{player_name} 勝利!!")
    else:
        if ai_action == 1:
            print("ai 勝利")
        else:
            print(f"{player_name} 勝利!!")
    
    # 詢問是否繼續遊戲
    print("-----是否繼續?(Y/N)-----")
    if input() in ("Y", "y"):
        continue
    else:
        print("-----遊戲結束-----")
        break
