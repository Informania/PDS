## Dictionary ADT ##
## Implemented with unordered list

class Dictionary:
    def __init__(this):
        this.D=[]

    def insert(this, key, value):
        this.D.append((key, value))

    def delete(this, key):
        index = this.__find(key)
        if index < len(this.D):
            del this.D[index:index+1]

    def __find(this, key):
        i = 0
        for clef, value in this.D:
            if clef == key:
                return i
            i=i+1
        return i

    def find(this, key):
        index = this.__find(key)
        if index == len(this.D):
            return None
        else:
            return this.D[index][1]
    
    def traverse(this, f):
        for key, value in this.D:
            f(value)

    def __strValue(this, value):
        this.S = this.S + " " + str(value) + ";\n"

    def __str__(this):
        this.S = '[\n'
        this.traverse( this.__strValue )
        return this.S + ']'
