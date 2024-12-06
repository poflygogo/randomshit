# -*- encoding: utf-8 -*-
# python 3.12
# UVa 12503 Robot Instructions
# zerojudge e567


for _ in range(int(input())):
    location = 0
    history_commands = []
    for _ in range(int(input())):
        command = input()

        def action(comm: str):
            global location
            if comm == 'LEFT':
                location -= 1
            elif comm == 'RIGHT':
                location += 1
            else:
                action(history_commands[int(comm.rsplit(maxsplit=1)[-1]) - 1])
        
        action(command)
        history_commands.append(command)
    
    print(location)
