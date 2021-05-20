# Search methods

import search

ab = search.GPSProblem('A', 'B'
                       , search.romania)

#print(search.breadth_first_graph_search(ab).path())
#print(search.depth_first_graph_search(ab).path())

busqueda = search.best_value_first_graph_search(ab)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())
busqueda = search.best_value_first_heuristics_graph_search(ab)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())

print("----------------------------------------------------------")

zh = search.GPSProblem('Z', 'H'
                       , search.romania)

busqueda = search.best_value_first_graph_search(zh)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())
busqueda = search.best_value_first_heuristics_graph_search(ab)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())

print("----------------------------------------------------------")

di = search.GPSProblem('D', 'I'
                       , search.romania)

busqueda = search.best_value_first_graph_search(di)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())
busqueda = search.best_value_first_heuristics_graph_search(ab)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())

print("----------------------------------------------------------")

oc = search.GPSProblem('F', 'D'
                       , search.romania)

busqueda = search.best_value_first_graph_search(oc)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())
busqueda = search.best_value_first_heuristics_graph_search(ab)
print("Expanded nodes: ", busqueda[1]," Path: ", busqueda[0].path())

# Result:
# [<Node B>, <Node P>, <Node R>, <Node S>, <Node A>] : 101 + 97 + 80 + 140 = 418
# [<Node B>, <Node F>, <Node S>, <Node A>] : 211 + 99 + 140 = 450
