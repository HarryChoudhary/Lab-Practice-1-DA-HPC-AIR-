
class Node:

	def __init__(self, f=0, h=0, name=0):
		self.f = f
		self.h = h
		self.name = name
	
	def setNeighbours(self, neighbours={}):
		self.neighbours = neighbours


# assume heuristics for each node
heuristics = [0, 3, 6, 5, 9, 8, 12, 14, 7, 5, 6, 1, 10, 2]

s = Node(h=heuristics[0], name='s')
a = Node(h=heuristics[1], name='a')
b = Node(h=heuristics[2], name='b')
c = Node(h=heuristics[3], name='c')
d = Node(h=heuristics[4], name='d')
e = Node(h=heuristics[5], name='e')
f = Node(h=heuristics[6], name='f')
g = Node(h=heuristics[7], name='g')
h = Node(h=heuristics[8], name='h')
i = Node(h=heuristics[9], name='i')
j = Node(h=heuristics[10], name='j')
k = Node(h=heuristics[11], name='k')
l = Node(h=heuristics[12], name='l')
m = Node(h=heuristics[13], name='m')

s.setNeighbours([a,b,c])
a.setNeighbours([s,d,e])
b.setNeighbours([s,f,g])
c.setNeighbours([s,h])
d.setNeighbours([a])
e.setNeighbours([a])
f.setNeighbours([b])
g.setNeighbours([b])
h.setNeighbours([c,i,j])
i.setNeighbours([h,k,l,m])
j.setNeighbours([h])
k.setNeighbours([i])
l.setNeighbours([i])
m.setNeighbours([i])

startNode = s
goalNode = i

def bfs(start,goal):

	closedSet = set([])
	openSet = set([start])

	cameFrom = {}
	print(cameFrom)
	
	start.f = start.h

	while len(openSet)!=0:

		current = findNodeWithLowestFScore(openSet)

		if current==goal:
			return contruct_path(cameFrom, current)

		openSet.remove(current)
		closedSet.add(current)

		#print(current.name, current.f, current.g, current.h)

		for neighbour in current.neighbours:

			#print(neighbour.name, neighbour.f, neighbour.g, neighbour.h)

			if neighbour in closedSet:
				print("already visited")
				continue

			if neighbour not in openSet:
				openSet.add(neighbour)

			cameFrom[neighbour] = current
			neighbour.f = neighbour.h



	return -1

def findNodeWithLowestFScore(openSet):
	fScore = 999999
	node = None
	for eachNode in openSet:
		if eachNode.f < fScore:
			fScore = eachNode.f
			node = eachNode
	return node


def contruct_path(cameFrom, current):

	totalPath = []
	while current in cameFrom.keys():
		current = cameFrom[current]
		totalPath.append(current)

	return totalPath



if __name__=="__main__":
	
	
	path = bfs(startNode, goalNode)

	print("Path is : " )
	for node in path[::-1]:
		print(str(node.name) + "-->")	
	print(goalNode.name)


