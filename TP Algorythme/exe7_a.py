# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : retourne l'indice du plus grand éléments
# Date : 18/11/2016
# Version : 1

def Max(l,n):
	if (n>len(l)):
		n=len(l)
	m=0
	for i in xrange(0,n):
		if l[i]>l[m]:
			m=i
	return m

l=[1,50,26,10,98,100,200,60,50,150]
n=input("Entrer le nombre de terme :")
print "L'indice le plus grand parmis les",n,"premier terme est le ",Max(l,n)
