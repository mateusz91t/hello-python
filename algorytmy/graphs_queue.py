from collections import deque

graph = {
    "I": ["Ald", "Mum", "Seb"],
    "Ald": ['Jus', 'Kam', 'Pau']
}

graph
graph['I']

search_queue = deque()
for k in graph.keys():
    search_queue += graph[k]
search_queue
