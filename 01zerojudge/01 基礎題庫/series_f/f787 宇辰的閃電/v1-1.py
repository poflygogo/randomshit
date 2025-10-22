class Player:
    def __init__(self, **kwargs):
        self.id: int = kwargs["id"]
        self.name: str = kwargs["name"]
        self.health: int = kwargs["health"]
        self.damage: int = kwargs["damage"]
        self.items: list[str] = kwargs["items"]
        self.next: int = int(self.items.pop()) - 1


total_players, target = map(int, input().split())
players = []
for id in range(total_players):
    name, health, damage, *items = input().split()
    players.append(Player(id=id, name=name, health=int(health), damage=int(damage), items=items))

visited = [False] * total_players
target -= 1
while not visited[target]:
    visited[target] = True
    p = players[target]

    p.health = max(0, p.health - p.damage)
    if p.health > 0:
        print(p.name, p.health, *p.items[:-p.damage])
    else:
        print(p.name, "dead.")

    target = p.next
