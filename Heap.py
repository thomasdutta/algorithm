class MaxHeap:

	#length - number of elements in array
	#heap_size - number of elements of the heap stored in the array
	# 1 < A.heap_size < A.length
	def __init__(self):
		self.heap_list = [0]
		self.heap_size = 0
		self.length = 0 

	def parent(i):	
		return i // 2

	def left(i):
		return 2 * i

	def right(i):
		return 2 * i + 1


	def maxHeapify(self, i):
		l = left(i)
		r = right(i)

		if l <= self.heap_size and self.heap_list[l] > self.heap_list[i]:
			largest = l
		else largest = i
		if r <= self.heap_size and self.heap_list[r] > self.heap_list[i]:
			largest = r


	def insert(self, k):
		self.heap_list.append(k)
		self.current_size = self.current_size + 1
		self.maxHeapify(self.current_size)


#implment the priority queue using heap