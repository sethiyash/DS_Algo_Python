# find lexographically smallest string with multiple allowed swaps on particular indices
# Input - cdafbe
# 3 m no of pairs that allowed to be swapped
# 0 1
# 2 1
# 3 5

from collections import defaultdict

instr = str(raw_input())

m = int(raw_input())


def add_edge(graph, u, v):
    graph[u].append(v)
    graph[v].append(u)


def dfs(indx, graph, vis, instr, indxlist, string):
    vis[indx] = True
    string.append(instr[indx])   
    indxlist.append(int(indx))
    
    for node in graph[indx]:
        if vis[node] == False:
            dfs(node, graph, vis, instr, indxlist, string)


def solution(instr, m):
    graph = defaultdict(list)
    while (m):
        u, v = map(int, raw_input().split())
        add_edge(graph, u, v)
        m -= 1
    vis = [False] * len(instr)

    output = list(instr)
    for i in range(0, len(instr)):
        if vis[i] == False:
            indxlist = []
            chars = []
            dfs(i, graph, vis, instr,indxlist,chars)
            string = ""
            for i in chars:
              string += i;
            string = sorted(string)
            indxlist = sorted(indxlist)
            j = 0
            for i in indxlist:
                if j < len(string):
                    output[i] = string[j] 
                    j += 1
    result= ""
    for i in output:
      result += i     
    print(result)

# instr = "cdafbe"
# m= 3
solution(instr, m)
