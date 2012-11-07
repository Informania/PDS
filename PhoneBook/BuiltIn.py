## Dictionary ADT ##
## Implemented with built-in dictionary structure

class Dictionary:
    def __init__(this):
        this.D={}

    def insert(this, key, value):
        if this.D.get(key) == None and this.D.get(key, 'N/A') == 'N/A':
            this.D[key]=value

    def delete(this, key):
        if this.D.get(key) != None or this.D.get(key, 'N/A') != 'N/A':
            del this.D[key]

    def find(this, key):
        return this.D.get(key)
    
    def traverse(this, f):
        for key, value in this.D.iteritems():
            f(value)

    def __strValue(this, value):
        this.S = this.S + " " + str(value) + ";\n"

    def __str__(this):
        this.S = '{\n'
        this.traverse( this.__strValue )
        return this.S + '}'
