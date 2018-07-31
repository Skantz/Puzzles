import collections

#https://codereview.stackexchange.com/a/135160	
def breadth_first_search(graph, root): 
    visited, queue = set(), collections.deque([root])
    while queue: 
        vertex = queue.popleft()
        for neighbour in graph[vertex]: 
            if neighbour not in visited: 
                visited.add(neighbour) 
                queue.append(neighbour) 

"""
if __name__ == '__main__':
    graph = {0: [1, 2], 1: [2], 2: []} 
    breadth_first_search(graph, 0)
"""

#from stackoverflow. Forgot the link.

def bfs(graph_to_search, start, end):
    queue = [[start]]
    visited = set()

    while queue:
        # Gets the first path in the queue
        path = queue.pop(0)

        # Gets the last node in the path
        vertex = path[-1]

        # Checks if we got to the end
        if vertex == end:
            return path
        # We check if the current node is already in the visited nodes set in order not to recheck it
        elif vertex not in visited:
            # enumerate all adjacent nodes, construct a new path and push it into the queue
            for current_neighbour in graph_to_search.get(vertex, []):
                new_path = list(path)
                new_path.append(current_neighbour)
                queue.append(new_path)

            # Mark the vertex as visited
            visited.add(vertex)
