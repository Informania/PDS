#!/usr/bin/python
# -*- coding: utf-8 -*-
"""*************************
* HashTable Dictionary
* Author: Joakim Lundkvist
* Date: Autum 2012
*************************"""

class Dictionary:
    # Initialize dictionary
    def __init__(self):
        self.__size = 4
        self.__numberOfItems = 0
	self.__table = ["Empty"] * self.__size
    
    # Insert value having key (returns None)
    def insert(self, key, value):
	index = hash(key) % len(self.__table)
	data = [key, value]
        if self.__table[index] == "Empty":
            self.__table[index] = data
        else:
            data = self.__table[index] + data
            self.__table[index] = data
	print "Adding %s to position %i" % (key, index)
	self.__numberOfItems += 1
        if self.__numberOfItems >= self.__size:
            self.reHash()
    
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
    	if len(item) >= 1:
            for each in item:
                if key == each[0]:
                    return index
            print "Can't find item"
        elif item == "Empty":
            print "Can't find item"
        else:
            print "Found!"
            return index

    def hash(self, key):
        h = 5381
        for char in str(key):
	    h = (h<<5) + h + ord(char)
	return h

    def reHash(self): 
        oldTable = self.__table
        self.__size = self.__size * 2
        print "doubling size"
        self.__table = ["Empty"] * self.__size
        self.__numberOfItems = 0
        for each in oldTable:
            print each
            key = str(each[0])
            value = str(each[1])
            self.insert(key, value)


    # for every value v apply f(v) exactly once
    # (returns None)
    def traverse(self, f):
        length = len(self.__table) -1
        for each in range(0, length):
            f(self.__table[each])

    # Returns string representation of dictionary
    def __str__(self):
        self.string = ''
        self.traverse(self.toString)
        return self.string

    def toString(self, value):
    ## TODO Buggar om det är mer än 2 värden på samma index i hashtabellen.    
        if value == "Empty":
            pass 
        else:
            for each in value:
                if len(each) == 2:
                    for i in each:
                        self.string += "%s " % i
                    self.string += "\t"
                else:        
                    self.string += "%s " % each


dic = Dictionary()
dic.insert("Anders", "0702563111")
dic.insert("Anders", "0702563111")
dic.insert("Joakim", "0770273821")
dic.insert("Joak", "0770273821")
dic.find("Anders")

print dic
