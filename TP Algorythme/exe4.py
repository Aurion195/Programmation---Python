# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : retourne l'indice du plus grand élément
# Date : 18/11/2016
# Version : 1

def Max(l):
	m=0
	for i in xrange(0,len(l)):
		if l[i]>l[m]:
			m=i
	return m

l=[1,50,26,10,98,100,50]
print "L'indice le plus grand est le",Max(l)
