class Player:
    def __init__(self, name: str, health: int, damage: int, items: list, n: int):
        self.name = name
        self.health = health
        self.damage = damage
        self.items = items
        self.next = n


def construct(s: str):
    name, health, damage, *items = s.split()
    n = int(items.pop()) - 1
    return Player(name, int(health), int(damage), items, n)


total_player, target = map(int, input().split())
players = [construct(input()) for _ in range(total_player)]
visited = [False] * total_player
target -= 1
while not visited[target]:
    visited[target] = True
    p = players[target]
    p.health -= p.damage
    if p.health > 0:
        print(p.name, p.health, *p.items[: -p.damage])
    else:
        print(p.name, "dead.")
    target = p.next
