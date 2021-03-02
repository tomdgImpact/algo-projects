from algopy import graph
from algopy import queue

def __bipartite_rec(G, s, M) :
    #Returns True if the connected component which s is a part of is bipartite, False otherwise
    q = queue.Queue()
    q.enqueue(s)
    M[s] = 1#vertex s is arbitrarily put in group 1
    while not q.isempty():
        s = q.dequeue()
        for i in G.adjlists[s]:
            if not M[i]:
                q.enqueue(i)
                M[i] = -M[s]#the group of vertex i is not the group of vertex s
                            #i -- s is an edge of G
            else:#problem detection
                if M[i]==M[s]:#i and s are in the same groupe
                              #i -- s is an edge of G
                    return False
    return True#since no return False in the loop above has been triggered

def __bipartiteBFS(G) :
    M = [None]*G.order #marker vector
                        #M[i] = None if i is not visited
                        #M[i] = 1 if i is part of the first group
                        #M[i] = -1 if i is part of the second group
    for i in range(G.order):
        if not M[i]:
            if not __bipartite_rec(G,i,M):#a problem has been detected
                return False
    return True#since no return False in the loop above has been triggered

def __bipartite_col_BFS(G, s, col, color, M) :
    q = queue.Queue()
    q.enqueue(s)
    M[s] = 1
    while not q.isempty() :
        s = q.dequeue()
        for i in G.adjlists[s] :
            if not M[i] :
                q.enqueue(i)
                M[i] = -M[s] # i is not in the same group as s
                if M[i] == -1:
                    color[i] = col[1]
                else:
                    color[i] = col[0]

def __bipartite_col(G) :
    color = [0] * G.order
    c = [1, 2]
    M = [None] * G.order
    for i in range(G.order) :
        if not M[i]:
            __bipartite_col_BFS(G) # call for function that will color the graph
    return (2, color)

def greedy_color(G):
    if __bipartiteBFS(G) :
        return __bipartite_col(G)
    c = [0] * G.order
    color = 1
    c[0] = color
    for i in range(1, G.order):
        for adj in G.adjlists[i]:
            t = 0


    return (color, c)
