# Implements the ADT Stack 
class Stack:
	def __init__(self):
		self.__items = []

	def push(self, item):
		self.__items.append(item)

	def pop(self):
		return self.__items.pop()

	def isEmpty(self):
		if self.__items == []:
			return True
		else:
			return False

	def __len__(self):
		return len(self.__items)

# Implements the ADT Queue
class Queue:
	def __init__(self):
		self.__items = []

	def enqueue(self, item):
		self.__items.insert(0, item)

	def dequeue(self):
		return self.__items.pop()
	
	def size(self):
		return len(self.__items)

	def isEmpty(self):
		if self.__items == []:
			return True
		else:
			return False

def menu():
	choice = 1
	while choice != 0:
		print "\nStart which function?"
		print "1: Uppgift 2 - Stack"
		print "2: Uppgift 3 - Queue"
		print "3: Uppgift 4 - parcheck"
		print "4: Uppgift 5 - parcheck v 2.0"
		print "5: Uppgift 6 - tagcheck"
		print "6: Uppgift 7 - Pictionary"
		choice = input("Ditt val: ")
		if choice == 0:
			break
		elif choice == 1:
			uppg2()
		elif choice == 2:
			uppg3()
		elif choice == 3:
			symbolString = raw_input("Skriv ett antal parenteser: ")
			parChecker(symbolString)
		elif choice == 4:
			symbolString = raw_input("Skriv en string med parenteser: ")
			parChecker2(symbolString)
		elif choice == 5:
			tagString = raw_input("Skriv ett antal startande och avslutande 'p'-taggar: ")
			tagChecker(tagString)
		elif choice == 6:
			mailList()

			

# Functions that do the specified exercises	
def uppg2():
	print "\n"
	stack = Stack()
	print stack.isEmpty()
	elements = [7, 6, 100, "Y"]
	for each in elements:
		stack.push(each)

	print stack.pop()
	print stack.isEmpty()
	stack.push(9)
	
	iterations = 0
	while iterations < 4:
		print stack.pop()
		iterations += 1
	
def uppg3():
	print "\n"
	queue = Queue()
	print queue.isEmpty()
	print queue.size()
	queue.enqueue("first in")
	print queue.size()
	queue.enqueue("second in")
	print queue.dequeue()
	print queue.isEmpty()

def parChecker (symbolString):
	print "\n"
	s = Stack()
	balanced = True
	for symbol in symbolString:
		if symbol == "(":
			s.push(symbol)
		else:
			if s.isEmpty() == True:
				balanced = False
				break
			else:
				s.pop()

	if s.isEmpty() == True and balanced == True:
		print "True"
	else:
		print "False"

def parChecker2(symbolString):
	print "\n"
	s = Stack()
	balanced = True
	for symbol in symbolString:
		if symbol == "(":
			s.push(symbol)
		elif symbol == ")":
			if s.isEmpty() == True:
				balanced = False
				break
			else:
				s.pop()
		else:
			pass

	if s.isEmpty() == True and balanced == True:
		print "True"
	else:
		print "False"
				
def tagChecker(tagString):
	stack_p = Stack()
	stack_slash = Stack()
	for symbol in tagString:
		if symbol == "<" or symbol == ">":
			pass
		elif symbol == "/":
			stack_slash.push(symbol)
		else:
			stack_p.push(symbol)

	outcome = float(len(stack_p)) / float(len(stack_slash))
	if outcome == 1 or outcome == 2:
		print True
	else:
		print False

def mailList():
	
	mail_list = {'Anders': 'nan@nan.com', 'Ola': 'non@bill.com'}
	
	choice = 1
	while choice != 0:
		print "What to do?"
		print "1: Add till person"
		print "2: Visa lista"
		print "0: Backa"
		choice = input("Deine vales: ")
		if choice == 0:
			pass
		elif choice == 1:
			name = raw_input("Namn personen? ")
			mail = raw_input("Mailadresssszs? ")
			mail_list[name]=mail
		elif choice == 2:
			print mail_list

menu()

// Test edit of text from git online