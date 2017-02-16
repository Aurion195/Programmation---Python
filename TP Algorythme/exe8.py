# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Renvoie la médiane d'une série de valeur contenues dans un liste
# Date : 18/11/2016
# Version : 1

def Max(l,n):
	if (n>len(l)):
		n=len(l)
	m=0
	for i in range(0,n):
		if l[i]>l[m]:
			m=i
	return m
	
def trier(l):
	n=len(l)
	for j in range(0,n-1):
		ind=Max(l,n-j)
		l[ind],l[n-j-1]=l[n-j-1], l[ind]
	return l

def mediane(l):
	a=0
	b=0
	c=0
	d=0
	trier (l)
	for i in range(0,len(l)):
		if len(l)%2!=0:
			c=(len(l))/2
			d=True
		else:
			a=len(l)/2
			b=len(l)/2-1
	if d==True:
		return c
	return a+b/2
				
l=[1,5,9,10,45,9,5,12,15]
print trier(l)
print "La médianne de la liste est la valeur",mediane(l)
