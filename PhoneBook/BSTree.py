# Name of class MUST be Dictionary

class Dictionary:

    # Initialize dictionary
	def __init__(self):
		self.root = None
		self.size = 0

    # Insert value having key (returns None)
	def insert(self, key, value):
		if self.root:
			self.root.put(key, value)
		else:
			self.root = TreeNode(key, value)
		self.size += 1

    # Delete value having key (returns None)
	def delete(self, key):
		if self.size > 1:
			self.root.delete(key)
			self.size -= 1

		elif self.size == 1:
			print "last key, deleting root"
			self.root = None
			self.size -= 1

		else:
			print "Error, bad key"

    # Return value having key, returns None if
    # key is not found
	def find(self, key):
		if self.root:
			return self.root.get(key)
		else:
			return None

	# for every value v apply f(v) exactly once
	# (returns None)
	def traverse(self, f):
		if self.root:
			f(self.root)
			if self.root.leftChild:
				self.root.leftChild.traverse(f)
			if self.root.rightChild:
				self.root.rightChild.traverse(f)

	# Returns string representation of dictionary
	def __str__(self):
		self.string = ''
		self.traverse(self.toString)
		return self.string
		
	def toString(self, value):
		self.string += "%s;\n" % str(value)

class TreeNode:

	def __init__(self, key, value, parent=None, left=None, right= None):
		self.key = key
		self.payload = value
		self.leftChild = left
		self.rightChild = right
		self.parent = parent

	def put(self, key, value):
		if key < self.key:
			if self.leftChild:
				self.leftChild.put(key, value)
			else:
				self.leftChild = TreeNode(key, value, self)
		else:
			if self.rightChild:
				self.rightChild.put(key, value)
			else:
				self.rightChild = TreeNode(key, value, self)

	def get(self, key):
		if key == self.key:
			return self.payload

		elif key < self.key:
			if self.leftChild:
				return self.leftChild.get(key)
			else:
				return None

		elif key > self.key:
			if self.rightChild:
				return self.rightChild.get(key)
			else:
				return None

		else:
			print 'Fatal Error'
	
	def delete(self, key):
		if self.key == key:
			if not (self.leftChild or self.rightChild):
				print "Removing node '" + str(self.key) + "' with no children"
				if self == self.parent.leftChild:
					self.parent.leftChild = None
				else:
					self.parent.rightChild = None

			elif (self.leftChild or self.rightChild) and \
					(not (self.leftChild and self.rightChild)):
				print "Removing node '" + str(self.key) + "' with one child"
				if self.leftChild:
					if self == self.parent.leftChild:
						self.parent.leftChild = self.leftChild
					else:
						self.parent.rightChild = self.leftChild

				else:
					if self == self.parent.leftChild:
						self.parent.leftChild = self.rightChild
					else:
						self.parent.rightChild = self.rightChild
			
			else:
				print "deleting node '" + str(self.key) + "' with 2 children"
				successor = self.findSuccessor()
				successor.spliceOut()
				
				if self.parent == None:
					print "Key deleted is root"
					self.key = successor.key
					self.payload = successor.payload

				elif self == self.parent.leftChild:
					self.parent.leftChild = successor
				else:
					self.parentleftChild = successor

				successor.leftChild = self.leftChild
				successor.rightChild = self.rightChild

		else:
			if key < self.key:
				if self.leftChild:
					self.leftChild.delete(key)
				else:
					print 'Trying to remove non-existing node'

			else:
				if self.rightChild:
					self.rightChild.delete(key)
				else:
					print 'Trying to remove non-existing node'

	
	def findSuccessor(self):
		successor = None
		if self.rightChild:
			successor = self.rightChild.findMin()
		else:
			if self.parent.leftchild == self:
				successor = self.parent
			else:
				self.parent.rightChild = None
				successor = self.parent.findSuccessor()
				self.parent.rightchild = self
		return successor

	def findMin(self):
		n = self
		while n.leftChild:
			n = n.leftChild
		print 'found min, key = ', n.key
		return n

	def spliceOut(self):
		if (not self.leftChild and not self.rightChild):
			print "Splicing out node with no children"
			if self == self.parent.leftChild:
				self.parent.leftChild = None
			else:
				self.parent.rightChild = None
		elif (self.leftChild or self.rightChild):
			print "Splicing out node with one child"
			if self.leftChild:
				if self == self.parent.leftChild:
					self.parent.leftChild = self.leftChild
				else:
					self.parent.rightChild = self.leftChild

			else:
				if self == self.parent.leftChild:
					self.parent.leftChild = self.rightChild
				else:
					self.parent.rightChild = self.rightChild

	def traverse(self, f):
		if self:
			f(self)
			if self.leftChild:
				self.leftChild.traverse(f)
			if self.rightChild:
				self.rightChild.traverse(f)

	def __str__(self):
		return "key: %s - value: %s" % (self.key, self.payload)

d = Dictionary()
d.insert('g', 1)
print 'insert'
print str(d.root) + " root"
d.insert('h', 2)
print 'insert'
d.insert('f', 3)
print 'insert'
d.insert('i', 5)
print 'insert'
print str(d.size) + "size"
d.insert('e', 19)
print 'insert'
a = d.root.leftChild
print str(a.parent) + " <--- is parent to leftchild"

d.delete('g')
print str(d.root.rightChild) + "<- rightchild of root"

print d
