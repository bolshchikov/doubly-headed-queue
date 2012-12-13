class Item():
	def __init__(self, value):
		'''class for an item in linked list'''
		self.value = value
		self.prev = None
		self.next = None


class DBL_Queue():
	def __init__(self):
		'''@constructor'''
		self.head = None
		self.tail = None
		self.length = 0

	def destroy(self):
		'''
		This method is going to play the role of a destructor.
		Due to the properties of Python as a language,
		destructors are not much in use, due to efficient garbage collector.
		It's worth to mention that garbage collector removes the instance,
		if nobody else has reference to it.
		Thus, the way the destructor is build: go over whole queue and 
		remove the references, and item instance. If the DBL_Queue
		won't contains any references, it will be removed by garbage collector.
		'''
		# remove references to head and tail
		del self.tail
		del self.head

		# set first iteration item
		current = self.tail
		next = current.next

		while next != None:
			#remove the references to next and previous
			del current.prev
			del current.next
			# remove the instance itself
			del current
			# create new iteration
			current = next
			next = current.next


			self.length -= 1
		
		# at the end, one instance of left, so it need to be removed
		del current.prev
		del current.next
		del current

		self.length -= 1

	def get_queue_size(self):
		'''
		Return length of a queue
		Complexity O(1)
		'''
		return self.length

	def enqueueBeg(self, value):
		'''
		Adds member at the beginning of a queue
		Complexity O(1)
		'''
		item = Item(value)
		if (self.length == 0):
			self.head = item
			self.tail = item
		else:
			item.prev = self.head
			self.head.next = item
			self.head = item
		self.length += 1

	def dequeueBeg(self):
		'''
		Removes and returns the member
		from the beginning of a queue
		Complexity O(1)
		'''
		if (self.head != None):
			if (self.length == 1):
				item = self.head
				self.head = None
				self.tail = None
				self.length -= 1
				return item
			else:
				item = self.head
				self.head = item.prev
				self.head.next = None
				self.length -= 1
				return item
		else:
			return -1

	def enqueueEnd(self, value):
		'''
		Adds member to the end of a queue
		Complexity O(1)
		'''
		item = Item(value)
		if (self.length == 0):
			self.head = item
			self.tail = item
		else:
			item.next = self.tail
			self.tail.prev = item
			self.tail = item
		self.length += 1


	def dequeueEnd(self):
		'''
		Removes and returns the member
		from the end of a queue
		Complexity O(1)
		'''
		if (self.tail != None):
			if (self.length == 1):
				item = self.tail
				self.head = None
				self.tail = None
				self.length -= 1
				return item
			else:
				item = self.tail
				self.tail = item.next
				self.tail.prev = None
				self.length -= 1
				return item
		else:
			return -1

	def concatQueue(self, q):
		'''
		Append one queue to the tail of another
		Complexity O(1)
		'''
		if (q.get_queue_size() != 0):
			self.tail.prev = q.head
			q.head.next = self.tail
			self.tail = q.tail
			self.length += q.length

	def printQueue(self):
		'''
		Prints the queue
		Complexity O(n)
		'''
		res = ''
		if (self.tail != None):
			item = self.tail
			while (item.next != None):
				res = res + str(item.value) + ' '
				item = item.next
			res = res + str(item.value)  + ' '
			print res
		else: 
			print res + '\n'