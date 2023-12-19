# Do not edit the class below except for the buildHeap,
# siftDown, siftUp, peek, remove, and insert methods.
# Feel free to add new properties and methods to the class.
class MinHeap:
	def __init__(self, nodes, max_heat):
        # Do not edit the line below.
		self.heap, self.idx_map = self.buildHeap(nodes, max_heat)
		
	def buildHeap(self, nodes, max_heat):
        # Write your code here.
    	
		array = []
		idx_map = {}
		for i, row in enumerate(nodes):
			for j, col in enumerate(row):
				for dir, steps in col.items():
					for step in range(len(steps)):
						vertex = ((i,j), dir, step)
                        
						idx_map[vertex] = len(array)
                        
						array.append([vertex, max_heat])
        
		for k in range(12):
            
			array[k][1] = 0
		return array, idx_map

	def swap(self, i, j):
		self.idx_map[self.heap[i][0]] = j
		self.idx_map[self.heap[j][0]] = i
		self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    
	def siftDown(self, parent = 0):
        # Write your code here.
		child1 = 2*parent + 1
		child2 = child1 + 1
		
		while ((child1 < len(self.heap) and self.heap[parent][1] > self.heap[child1][1]) 
		    or (child2 < len(self.heap) and self.heap[parent][1] > self.heap[child2][1])):
			toSwap = child1 if child2 < len(self.heap) and self.heap[child1][1] < self.heap[child2][1] else child2
			# self.heap[parent], self.heap[toSwap] = self.heap[toSwap], self.heap[parent]
			self.swap(parent, toSwap)
			parent = toSwap
			child1 = 2*parent + 1
			child2 = child1 + 1

    
	def siftUp(self):
        # Write your code here.
		child = len(self.heap) - 1
		parent = (child - 1) // 2
		
		while self.heap[parent] > self.heap[child] and child > 0:
			self.swap(parent, child)
			child = parent
			parent = (parent - 1) // 2
		

    
	def peek(self):
        # Write your code here.
        
		return self.heap[0]

    
	def remove(self):
        # Write your code here.
		self.idx_map[self.heap[-1][0]] = 0
		del self.idx_map[self.heap[0][0]]

        
		self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
		to_remove = self.heap.pop()
		self.siftDown()
	
		return to_remove

    
	def insert(self, value):
        # Write your code here.
        
		self.heap.append(value)
		self.siftUp()
