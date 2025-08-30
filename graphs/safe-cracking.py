from collections import deque
def safe_cracking(hints):
  """
  understanding:
  1. given a input of pairs (x, y) which are number combinations
  2. return the number combinations

  approach:
    pattern: topligical order
    iterate through the graph and add the parents that has 0 parents to string
  
  """
  ready = deque([])
  result = ""
  graph = build_graph(hints)
  parents_count = {}
  
  for key in graph:
    for node in graph[key]:
      if node not in parents_count:
        parents_count[node] = 1
      else:
        parents_count[node] += 1

  for node in graph:
    if node not in parents_count:
      ready.append(node)

  while ready:
    cur = ready.popleft()
    result += str(cur)
    for child in graph[cur]:
      parents_count[child] -= 1
      if parents_count[child] == 0:
        ready.append(child)

  return result

def build_graph(hints):
  graph = {}
    
  for pair in hints:
    x, y = pair 
    if not x in graph:
      graph[x] = []

    if not y in graph:
      graph[y] = []
    graph[x].append(y)

  return graph