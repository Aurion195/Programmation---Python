# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : insére un élément dans une liste triée
# Date : 22/11/2016
# Version : 1

def Max(l,n):
	if (n>len(l)):
		n=len(l)
	m=0
	for i in xrange(0,n):
		if l[i]>l[m]:
			m=i
	return m

def trier(l):
	n=len(l)
	for j in xrange(0,n-1):
		ind=Max(l,n-j)
		l[ind],l[n-j-1]=l[n-j-1], l[ind]
	return l
	
def insere_trie(l,x):
	trier(l)
	n=len(l)
	if x<=l[0]:
		l.insert(0,x)
		return
	if x>=l[n-1]:
		l.insert(n,x)
		return 
	d=0
	f=n-1
	while (f-d)>1:
		m=(f+d)/2
		if (x<l[m]):
			f=m
		else:
			d=m
	l.insert(d+1,x)

l=[1,2,5,4,8,6,9,7,10]
x=3
insere_trie(l,x)
print l
