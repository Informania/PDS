"""*************************
* HashTable Dictionary
* Author: Joakim Lundkvist
* Date: Autum 2012
*************************"""

class Dictionary:
    # Initialize dictionary
    def __init__(self, size):
	self.__table = ["NaN"] * size
    
    # Insert value having key (returns None)
    def insert(self, key, value):
	index = hash(key) % len(self.__table)
	data = [key, value]
	self.__table[index] = data
	print "Adding %s to position %i" % (key, index)
    
    # Delete value having key (returns None)
    def delete(self, key):
	item = self.find(key)
        if item:
            self.__table.pop(item)
            print "Deleting %s" % key
        else:
            print "Can't delete item, it doesn't exist"

    # Return value having key, returns None if
    def find(self, key):
    	index = hash(key) % len(self.__table)
    	item = self.__table[index]
    	if item != "NaN":
    	    return index
    	else:
	    print "Cant find item"

    def hash(self, key):
        h = 5381
        for char in str(key):
	    h = (h<<5) + h + ord(char)
	return h

    # for every value v apply f(v) exactly once
    # (returns None)
    def traverse(self, f):
        pass   # Abstract method, add your own code

    # Returns string representation of dictionary
    def __str__(self):
        return str(self)  # Abstract method, add your own code


dic = Dictionary(500)
dic.insert("Anders Sipinen", "0702563111")

dic.delete("Anders Sipinen")
dic.delete("a")
