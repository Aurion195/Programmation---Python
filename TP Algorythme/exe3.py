# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Supprimer les doublons
# Date : 18/11/2016
# Version : 1


def cherche_pnp(l,x,n):
	if(len(l)<n): 
		n=len(l)
	for i in xrange(0,n):
		if (x==l[i]):
			return True
	return False

def doublon(l):
	n=0
	m=len(l)
	for i in xrange(0,m):
		if (cherche_pnp(l,l[n],n)==True):
			l.remove(l[n])
		else: n+=1

l=[2,2,4,5,6,7,9,5,10,5,6,7,2,10,25,10]
doublon(l)
print "Voici la liste l sans les doublons",l
