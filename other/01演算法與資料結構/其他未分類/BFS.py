graph = {
    "A":['B','C'],
    "B":['A','C','D'],
    "C":['A','B','D','E'],
    "D":['B','C','E','F'],
    "E":['C','D'],
    "F":['D']
}
def BFS(graph, s):
    queue = [] #創建一個空的集合
    queue.append(s) #將第一個自放進去
    seen = [] #在創建一個檢視這個字是否填到queue過的集合
    seen.append(s)
    while (len(queue) > 0): #所有的字都會進去queue一次然後再被pop出來
        vertex = queue.pop(0) #把pop出來的甜到vertex
        nodes = graph[vertex] #nodes會記錄 剛剛pop出來的節點後面有誰
        for w in nodes:
            if w not in seen: #如果這個字沒有被看過才要進入這個迴圈
                queue.append(w) #把nodes的字記錄到queue裡面，這樣會讓while迴圈一直執行到全部的字都走過一次
                seen.append(w)  #新增看過的字
        print(vertex,end = " ")

BFS(graph,"E")