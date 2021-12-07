

import itertools

def performIterator(tuplevalues):
fl=[]
il=[]
x=0
for i in range(4):
il.append(tuplevalues[0][i])
fl.append(tuple(il))
fl.append(tuple(itertools.repeat(tuplevalues[1][0], len(tuplevalues[1]))))
fl.append(tuple(itertools.accumulate(tuplevalues[2])))
fl.append(tuple(itertools.chain(tuplevalues[0],tuplevalues[1],tuplevalues[2],tuplevalues[3])))
fl.append(tuple(itertools.filterfalse(lambda x:x%2==0,ct)))
return tuple(fl)
