#!/usr/bin/python
#
# genBook.py generates phone book files for the phoneBook application.
#

size     = 150
filename = "gen150.phn"

# You can set size of book and name of file above, then run 'genBook.py'
#

def mkzeros( val, max ):
    if val == 0:
        val = 1
    if len(str(val)) >= len(str(max)):
        return ''
    else:
        return '0' + mkzeros( 10*val, max )


file = open( filename, 'w' )
for i in xrange( size ):
    file.write( 'name' + mkzeros(i,size-1) + str(i) + '\n' )
    file.write( str(i) + '\n' )
file.close()
