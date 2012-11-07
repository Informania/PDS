## Dictionary ADT ##
## Implemented with sorted list

class Dictionary:
    def __init__(this):
        this.D=[]

    def insert(this, key, value):
        this.D.append((key, value))
        i = len(this.D)-2
        done = False
        while i > -1 and not done:
            if key < this.D[i][0]:
                this.D[i+1] = this.D[i]
                this.D[i]   = (key, value)
            else:
                done = True
            i = i-1

    def delete(this, key):
        index = this.__find(key)
        if index < len(this.D):
            del this.D[index:index+1]

    def __find(this, key):
        i = 0
        j = len(this.D)-1
        while j-1 > i:
            m = (i+j)/2
            if key == this.D[m][0]:
                return m
            elif key < this.D[m][0]:
                j = m-1 
            else:
                i = m+1
        return len(this.D)

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
