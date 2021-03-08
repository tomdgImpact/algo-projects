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
    color[s] = col[0]
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
            __bipartite_col_BFS(G, i, c, color, M) # call for function that will color the graph
    return (2, color)

def __chose_color(G, x, c, nbcolor) :
    col = 1
    i = 0
    l = len(G.adjlists[x])
    while i < l :
        if c[G.adjlists[x][i]] == col :
            col += 1
            i = 0
        else :
            i += 1
    if col > nbcolor : # if col is greater, it has to be greater of 1
        nbcolor += 1
    c[x] = col
    return nbcolor

def __max_vertex(G) :
    sort = []
    for i in range(G.order):
        sort.append(len(G.adjlists[i]))
    sort.sort(reverse=True)
    return sort

def __greedy_BFS(G, c, nbcolor, M, x) :
    q = queue.Queue()
    q.enqueue(x)
    M[x] = True
    c[x] = True
    while not q.isempty() :
        s = q.dequeue()
        for adj in G.adjlists[s] :
            if not M[adj] :
                M[adj] = True
                nbcolor = __chose_color(G, adj, c, nbcolor)
                q.enqueue(adj)
    return (nbcolor, c)

def bipartite (G):
    if __bipartiteBFS(G) :
        return __bipartite_col(G)

def color_greedy(G):
    #if __bipartiteBFS(G) :
     #   return __bipartite_col(G)
    c = [0] * G.order
    M = [False] * G.order
    nbcolor = 1
    for i in range(G.order) :
        if not M[i] :
            nbcolor , c = __greedy_BFS(G, c, nbcolor, M, i)
    return (nbcolor, c)
