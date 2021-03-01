from algopy import graph

def greedy_color(G):
    c = [0] * G.order # color vector
    p  = [] # parent vector if needed
    co = 1 # current color
    for i in range(G.oder):
        for adj in G.adjlists[i] :
            if c[adj] == c[i] :
                co += 1
            c[i] = co
