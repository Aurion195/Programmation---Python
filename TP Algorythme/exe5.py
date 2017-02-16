# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Calcule la moyenne
# Date : 18/11/2016
# Version : 1

def moyenne(l):
	total=0
	for i in range(0,len(l)):
		total+=l[i]
	moy=total/len(l)
	return moy

l=[1.0,2.0,3.0,4.0,5.0,6.0,7.0,8.0,9.0,10.0]
print "La moyenne est de",moyenne(l)
