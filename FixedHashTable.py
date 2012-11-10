#!/usr/bin/python
# -*- coding: utf-8 -*-
"""*************************
* HashTable Dictionary
* Author: Joakim Lundkvist
* Date: Autum 2012
*************************"""

class Dictionary:
    # Initialize dictionary
    def __init__(self, size):
	self.__table = ["Empty"] * size
    
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
    	if len(item) >= 3:
            for each in item:
                if key == each:
                    print "Found on index %s" % index
                    return index
            print "Can't find item '%s'" % key
        elif item == "Empty":
            print "Can't find item %s, index is empty" % key
        else:
            print "Found!"
            return index
    
    # Hash function for choosing index
    def hash(self, key):
        h = 5381
        for char in str(key):
	    h = (h<<5) + h + ord(char)
	return h

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
        if value == "Empty":
            pass 
        else:
            count = 0
            for each in value:
                self.string += "%s" % each
                if count == 1:
                    count = 0
                    self.string += ", "
                else:
                    self.string += " - "
                    count += 1


dic = Dictionary(500)
dic.insert("Anders", "0702563111")
dic.insert("Anders", "0702563111")
dic.insert("Joakim", "0770273821")
dic.insert("Joakim", "0770273821")
dic.find("Anders")

print dic

