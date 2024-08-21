import random

def print_action(player:str, action:int):
    """輸出玩家行動結果"""
    choice = ""
    if action == 1: choice = "剪刀"
    elif action == 2: choice = "石頭"
    else: choice = "布"
    print(f"{player}\t出拳: {choice}")

def judge(player:int, ai:int) -> str:
    """裁判並返回結果"""
    WIN_TABLE = (None, 2, 0, 1)     # 剪刀贏石頭, 石頭贏布, 布贏剪刀
    if player == ai:
        return "平手!!"
    elif WIN_TABLE[player] == ai:
        return "ai 勝利!!"
    else:
        return f"{player_name} 勝利!!"
    
def ask_continue() -> bool:
    """詢問是否繼續遊戲"""
    print("-----是否繼續?(Y/N)-----")
    if input() in ("Y", "y"):
        return True
    else:
        print("-----遊戲結束-----")
        return False
        
print("------歡迎來到剪刀石頭布小遊戲------")
player_name = input("請輸入您的名字: ")  # type:str

while True:

    # 玩家行動
    print("-----玩家行動階段-----")
    while True:
        try:
            player_action = int(input("1 = 剪刀\n2 = 石頭\n3 = 布\n你想出什麼?: "))
            if 1 <= player_action <= 3:
                print_action(player_name, player_action)
                break
            else:
                print("注意: 請輸入1, 2 或 3")
        except ValueError:
            print("\n注意: 請輸入整數數字\n")

    # ai行動
    ai_action = random.randint(1, 3)
    print_action("ai", ai_action)

    # 檢查結果並輸出
    print()     # 空一行
    print(judge(player_action, ai_action))
    
    # 詢問是否繼續遊戲
    if ask_continue():
        continue
    else:
        break
