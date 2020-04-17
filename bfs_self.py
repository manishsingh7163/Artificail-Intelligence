final = ("1", "2", "3",
          "4", "5", "6",
           "7", " ","8")

initial = ("1", "2", "3",
          "4", "5", " ",
           "7", "8","6")



def right(node, i):
    node=list(node)
    node[i], node[i+1] = node[i+1], node[i]
    return node
def left(node, i):
    node=list(node)
    node[i], node[i-1] = node[i-1], node[i]
    return node
def up(node, i):
    node=list(node)
    node[i], node[i-3] = node[i-3], node[i]
    return node
def down(node, i):
    node=list(node)
    node[i], node[i+3] = node[i+3], node[i]
    return node
    
def find_child(node):
    node=list(node)
    i = node.index(" ")
    child_list = []
    for i,j in node:
        print({}, {}, {}, node[i][j], node[i][j+1], node[i][j+2])
    if((i % 3 !=2) and i in range(0,9) ):
        c1 = right(node, i)
        child_list.append(c1)
    if((i % 3 !=0) and i in range(0,9) ):
        c2 = left(node, i)
        child_list.append(c2)
    if((i-3) in range(0,9)):
        c3 = up(node, i)
        child_list.append(c3)
    if((i+3) in range(0,9)):
        c4 = down(node, i)
        child_list.append(c4)
    return child_list

list_explore = []
def bfs(initial, final):
    initial=list(initial)
    final=list(final)
    queue = [initial]
    while queue:
        for nodes in queue:  
        node = queue.pop(0)
        if node not in list_explore:
            list_explore.append(node)
            if(node == final):
                return list_explore
            child = find_child(node)
            for i in child:
                queue.append(i)
            

print(list_explore)
print(bfs(initial, final))
