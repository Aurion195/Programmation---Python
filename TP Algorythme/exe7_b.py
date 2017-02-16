# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Trier une liste ordonnées
# Date : 18/11/2016
# Version : 1

def Max(l):
	m=0
	for i in xrange(0,len(l)):
		if l[i]>l[m]:
			m=i
	return m
	
def trier(l):
	tri=[]
	while len(l)>0:
		ind = Max(l)
		tri.append(l[ind])
		l.remove(l[ind])

	return tri
		
l=[1,50,26,10,98,100,100,60,50,150,-1]
print "Voici la liste trier par ordre croissant",trier(l)
