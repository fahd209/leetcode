from collections import deque
def topological_order(graph):

  """
    understanding:
      given a DAG return array of the graph in topological_order

    approach:
      1. find the graph with no parents and start from there
      2. as we iterate we append every node we visited to the array 
  """
  # counting parents of each child
  parent_count = count_parents(graph)
  result = []
  ready = deque([])

  # dfs on the node with no parents
  for parent in parent_count:
    if parent_count[parent] == 0:
      ready.append(parent)

  # going through the graph in topological_order
  while ready:
    cur = ready.popleft()
    result.append(cur)
    for neighbor in graph[cur]:
      parent_count[neighbor] -= 1
      if parent_count[neighbor] == 0:
        ready.append(neighbor)

  return result


def count_parents(graph):
  parents_count = {}
  for node in graph:
    parents_count[node] = 0
    
  for key in graph:
    for neighbor in graph[key]:
      parents_count[neighbor] += 1
      
  return parents_count

  