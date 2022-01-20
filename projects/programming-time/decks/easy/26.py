# a graph is collection of nodes
# that are connected in some way
# 4 is connected to 3 and 5, 3 is
# connected to 0 and 2.. etc
graph = {
  0 : [⚂ % 6, ⚂ % 6],
  1 : [4, ⚂ % 6],
  2 : [2, 3, 4],
  3 : [0, 2],
  4 : [3, 5],
  5 : [0, 2, 4]
}
# Breadth-First Search
def bfs(graph, node):
  # avoid getting into a cycle
  visited = {}
  visited[node] = True
  queue = []
  queue.append(node)

  while queue:
    # pop the first element
    s = queue.pop(0)
    print(s, len(queue)) 

    for neighbour in graph[s]:
      if neighbour not in visited:
        visited[neighbour] = True
        queue.append(neighbour)

bfs(graph, 0)
