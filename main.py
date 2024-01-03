graph={
    'a':{'b':3,'c':4,'d':7},
    'b':{'c':1,'f':5},
    'c':{'f':6,'d':2},
    'd':{'e':3,'g':6},
    'e':{'g':3,'h':4},
    'f':{'e':1,'h':8},
    'g':{'h':2},
    'h':{'g':2}
}
def dijkstra(graph,start,goal):
    shortest_distance={}
    track_predecessor={}
    unseenNodes=graph 
    infinity=99999999999
    track_path=[]

    for node in unseenNodes:
        shortest_distance[node]=infinity
    shortest_distance[start]=0

    while unseenNodes:
        min_ditance_node=None
        for node in unseenNodes:
            if min_ditance_node is None:
                min_ditance_node=node
            elif shortest_distance[node]<shortest_distance[min_ditance_node]:
                min_ditance_node=node
        
        path_options=graph[min_ditance_node].items()

        for child_node,weight in path_options:
            if weight+shortest_distance[min_ditance_node]< shortest_distance[child_node]:
                shortest_distance[child_node]=weight+shortest_distance[min_ditance_node]
                track_predecessor[child_node]=min_ditance_node
        
        unseenNodes.pop(min_ditance_node)
    
    currentNode=goal

    while currentNode!=start:
        try:
            track_path.insert(0,currentNode)
            currentNode=track_predecessor[currentNode]


        except KeyError:
            print("Path is not reachable!")
            break
    
    track_path.insert(0,start)

    if shortest_distance[goal]!=infinity:
        print(f"Shortes distance is {shortest_distance[goal]} ")
        print(f"Optimal Path is:{track_path}")



start=input("Enter the starting point")
end=input("Enter the ending point")
dijkstra(graph,start,end)
