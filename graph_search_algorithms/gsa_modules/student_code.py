from inspect import stack
from expand import expand
from collections import deque
import math
class hashT:
	def __init__(self) -> None:
		self.hash = {}

	def insert(self, key, val):
		self.hash[key] = val

	def get(self, key):
		try:
			return self.hash[key]
		except KeyError:
			return None

class valuedKey:
	def __init__(self, key):
		self.key = key
		self.h = math.inf
		self.g = math.inf
		self.f = math.inf

# A simple implementation of Priority Queue
# using Queue.
class PriorityQueue(object):
	def __init__(self):
		self.queue = []

	def __str__(self):
		return ' '.join([str(i) for i in self.queue])

	# for checking if the queue is empty
	def isEmpty(self):
		return len(self.queue) == 0

	# for inserting an element in the queue
	def insert(self, data):
		self.queue.append(data)

	# for popping an element based on Priority
	def delete(self):
		try:
			max = 0
			for i in range(len(self.queue)):
				if self.queue[i].f < self.queue[max].f:
					max = i
				elif self.queue[i].f == self.queue[max].f: #tiebreaker
					if self.queue[i].h < self.queue[max].h:
						max = i
						#might need to check key.g as well
			item = self.queue[max].key
			del self.queue[max]
			return item
		except IndexError:
			print()
			exit()

def f(vKey, end, mapT, mapD, vKeyGivenNode, kyNdTbl, parentHshTbl):
	if not parentHshTbl.get(vKeyGivenNode.key) == vKey.key: #prevent child infinite loop
		if kyNdTbl.get(vKey.key).g  > vKeyGivenNode.g + mapT[vKeyGivenNode.key][vKey.key]:
			vKey.h = mapD[vKey.key][end]
			vKey.g = vKeyGivenNode.g + mapT[vKeyGivenNode.key][vKey.key]
			vKey.f = vKey.h + vKey.g
			parentHshTbl.insert(vKey.key, vKeyGivenNode.key)


def a_star_search (dis_map, time_map, start, end):
	'''priorityqueue(stackRefill) # priority based off of smallest f(n) = g(n) + h(n), lets also think about TIEBREAKERS!!!
		for kp in stackRefill:
			nodeStack.append(kp)'''
	seen = hashT() # will be a hash table later
	seen_inc = 1
	parent = hashT()
	keyNodeTable = hashT()
	returnedPath = []
	nodePQueue = PriorityQueue()
	reverseStack = deque()
	initKey = valuedKey(start) # container for all info about nodes key,g,h,f
	initKey.g = 0
	initKey.h = dis_map[start][end]
	initKey.f = dis_map[start][end]
	keyNodeTable.insert(start, initKey) # hashTable of node names "keys" and valuedKeys "values"
	nodePQueue.insert(initKey)
	if (start == end): # should only happen if start = end  
			returnedPath.append(end) 
			return returnedPath
	while (not nodePQueue.isEmpty()): # while the nodeStack isn't empty
		givenNode = nodePQueue.delete() # copy/store first node of the stack
		if (givenNode == end): #check if goal is reached
			child = end
			reverseStack.append(end)
			while child != start:
				reverseStack.append(parent.get(child)) 
				child = parent.get(child)
			for i in range(len(reverseStack)):
				returnedPath.append(reverseStack.pop())
			return returnedPath		
		if not seen.get(givenNode): # don't expand same node twice
			seen.insert(givenNode, seen_inc)
			seen_inc += 1 
			stackRefill = expand(givenNode, time_map) # collect all givenNode's children
			for key in stackRefill:
				if key != start:
					if not keyNodeTable.get(key) : # don't change vKey values of key if they already exist
						vKey = valuedKey(key) # otherwise make a vKey for key 
						keyNodeTable.insert(key, vKey) # and insert into keyNodeTable 
					f(keyNodeTable.get(key), end, time_map, dis_map, keyNodeTable.get(givenNode), keyNodeTable, parent)
					nodePQueue.insert(keyNodeTable.get(key))		
	return [''] #couldn't get to end node 

def depth_first_search(time_map, start, end): # reaching end node is the goal
	parent = {} # ASSUMING DICTIONARIES WORK WELL LIKE THIS
	returnedPath = []
	nodeStack = deque()
	reverseStack = deque()
	nodeStack.append(start)
	if (start == end): # should only happen if star  
			returnedPath.append(end) 
			return returnedPath
	while (nodeStack): # while the nodeStack isn't empty	
		givenNode = nodeStack.pop() # copy/store first node of the stack 
		if (givenNode == end): # check if goal is reached
			child = end
			reverseStack.append(end)
			while child != start:
				reverseStack.append(parent[child]) 
				child = parent[child]
			for i in range(len(reverseStack)):
				returnedPath.append(reverseStack.pop())
			return returnedPath
		stackRefill = expand(givenNode, time_map) # in BFS do not expand the same node twice 
		for key in stackRefill:
			parent[key] = givenNode
			nodeStack.append(key)
	return [''] #couldn't get to end node


def breadth_first_search(time_map, start, end):
	seen = hashT() # will be a hash table later
	seen_inc = 1
	parent = hashT()
	returnedPath = []
	nodeQueue = deque()
	reverseStack = deque()
	nodeQueue.append(start)
	if (start == end): # should only happen if start == end  
			returnedPath.append(end) 
			return returnedPath
	while (nodeQueue): # while the nodeStack isn't empty
		givenNode = nodeQueue.popleft() # copy/store first node of the stack
		if (givenNode == end): #check if goal is reached
			child = end
			reverseStack.append(end)
			while child != start:
				reverseStack.append(parent.get(child)) 
				child = parent.get(child)
			for i in range(len(reverseStack)):
				returnedPath.append(reverseStack.pop())
			return returnedPath			
		if not seen.get(givenNode): 
			seen.insert(givenNode, seen_inc)
			seen_inc += 1 
			stackRefill = expand(givenNode, time_map) # stackRefill, will be sorted by least to greatest traffic time # in BFS do not expand the same node twice 
			#stackRefill.reverse()
			for key in stackRefill:
				if (not parent.get(key)): # may kill parent-child cycle issue
					parent.insert(key, givenNode)
				nodeQueue.append(key)	
	return [''] #couldn't get to end node 

''' if not keyNodeTable.get(givenNode):
					vKeyGivenNode = valuedKey(givenNode)
					vKeyGivenNode.h = dis_map[givenNode][end]
					if time_map[start][givenNode]:
						vKeyGivenNode.g = time_map[start][givenNode]
						vKeyGivenNode.f = vKeyGivenNode.g + vKeyGivenNode.h
					keyNodeTable.insert(givenNode, vKeyGivenNode) '''