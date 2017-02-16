# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Renvoie un élément d'un indice
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

def renvoie(l,x):
	trier(l)
	l_indices=[]
	for i in xrange(0,len(l)):
		if l[i]==x:
			l_indices.append(i)
	return l_indices

l=[1,5,9,10,45,8,5,10]
print trier(l)
x=5
print "A l'indice",renvoie(l,x),"se sont les mêmes valeurs"
