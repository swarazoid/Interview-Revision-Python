import sys 

class MinHeap: 
	def __init__(self, maxsize): 
		self.maxsize = maxsize 
		self.size = 0
		self.Heap = [0]*(self.maxsize + 1) 
		self.Heap[0] = -1 * sys.maxsize 
		self.FRONT = 1

	def parent(self, pos): 
		return pos//2

	def leftChild(self, pos): 
		return 2 * pos 

	def rightChild(self, pos): 
		return (2 * pos) + 1

	def isLeaf(self, pos): 
		return pos*2 > self.size 

	def swap(self, fpos, spos): 
		self.Heap[fpos], self.Heap[spos] = self.Heap[spos], self.Heap[fpos] 

	# Function to heapify the node at pos 
	def minHeapify(self, pos): 

		# If the node is a non-leaf node and greater 
		# than any of its child 
		if not self.isLeaf(pos): 
			if (self.Heap[pos] > self.Heap[self.leftChild(pos)] or
			self.Heap[pos] > self.Heap[self.rightChild(pos)]): 

				# Swap with the left child and heapify 
				# the left child 
				if self.Heap[self.leftChild(pos)] < self.Heap[self.rightChild(pos)]: 
					self.swap(pos, self.leftChild(pos)) 
					self.minHeapify(self.leftChild(pos)) 

				# Swap with the right child and heapify 
				# the right child 
				else: 
					self.swap(pos, self.rightChild(pos)) 
					self.minHeapify(self.rightChild(pos)) 

	# Function to insert a node into the heap 
	def insert(self, element): 
		if self.size >= self.maxsize : 
			return
		self.size+= 1
		self.Heap[self.size] = element 
		current = self.size 
		while self.Heap[current] < self.Heap[self.parent(current)]: 
			self.swap(current, self.parent(current)) 
			current = self.parent(current) 

	# Function to build the min heap using 
	# the minHeapify function 
	def minHeap(self): 
		for pos in range(self.size//2, 0, -1): 
			self.minHeapify(pos) 

	# Function to remove and return the minimum 
	# element from the heap 
	def remove(self): 
		popped = self.Heap[self.FRONT] 
		self.Heap[self.FRONT] = self.Heap[self.size] 
		self.size-= 1
		self.minHeapify(self.FRONT) 
		return popped 

# Driver Code 
if __name__ == "__main__": 
	
	print('The minHeap is ') 
	minHeap = MinHeap(15) 
	minHeap.insert(5) 
	minHeap.insert(3) 
	minHeap.insert(17) 
	minHeap.insert(10) 
	minHeap.insert(84)
	minHeap.minHeap() 

	print("The Min val is " + str(minHeap.remove())) 
