# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : calculer la moyenne et la variance
# Date : 18/11/2016
# Version : 1

def moyenne(l):
	total=0
	moy=0
	for i in range(0,len(l)):
		total+=l[i]
	moy=total/len(l)
	return moy

def variance(l):
	s=0
	for i in range(0,len(l)):
		s+=((l[i]-moyenne(l))**2)/len(l)
	return s
	
l=[7.0,0.0,1.0,2.0,0.0]
print "La moyenne est de",moyenne(l)
print "La variance est de",variance(l)
