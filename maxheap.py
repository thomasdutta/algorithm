from random import randint

class MaxHeap:

	#length - number of elements in array
	#heap_size - number of elements of the heap stored in the array
	# 1 < A.heap_size < A.length
	def __init__(self):
		self.heap_list = [0,-1,-1,-1,-1,-1,-1,-1,-1,-1,-1]
		self.heap_size = 0
		self.length = 0 

	def parent(self, i):	
		return i // 2

	def left(self, i):
		return (2 * i)

	def right(self, i):
		return (2 * i + 1)


	def maxHeapify(self, i):
		l = self.left(i)
		r = self.right(i)
		if l <= self.heap_size and self.heap_list[l] > self.heap_list[i] :
			largest = l
		else :
			largest = i		
		if r <= self.heap_size and self.heap_list[r] > self.heap_list[largest] :
			largest = r
		if largest != i :
			tmp = self.heap_list[largest]
			self.heap_list[largest] = self.heap_list[i]
			self.heap_list[i] = tmp
			self.maxHeapify(largest)

	def buildHeap(self):
		index1 = self.heap_size // 2
		while index1 > 0 :
			print 'Inside BuildHeap: Called for index1: ' + str(index1) + ' value: ' + str(self.heap_list[index1])
			self.maxHeapify(index1)
			self.printHeap()
			index1 = index1 - 1

	def heapSort(self):
		index2 = self.length
		while index2 > 1 :
			tmp1 = self.heap_list[1]
			self.heap_list[1] = self.heap_list[index2]
			self.heap_list[index2] = tmp1
			self.heap_size = self.heap_size - 1
			self.maxHeapify(1)
			index2 = index2 - 1

	def printHeap(self):
		print self.heap_list
#		for i in self.heap_list:
#			print i

	def populateHeap(self):
		#for i in range(10):
		#	self.heap_list[i + 1] = randint(1,100)
		self.heap_list = [0, 63, 98, 90, 38, 25, 76, 74, 44, 75, 51]
		self.length = len(self.heap_list) - 1
		self.heap_size = len(self.heap_list) - 1
		print "Random heap created"
		self.printHeap()
		print "-------------------------------"
		self.buildHeap()
		self.printHeap()
