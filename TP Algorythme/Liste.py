def cherche(l,x):
	for i in xrange(0,l):
		if l[i]==x: return True
		else: return False

def doublon(l):
	n=len(l)
	for i in xrange(0,n):
		if cherche(l,x)==True:
			l.remove(l[i])
	return l


l=[1,2,2,3,4]
x=2

print doublon(l)
