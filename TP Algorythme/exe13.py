# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Calcul des sorties
# Date : 28/11/2016
# Version : 1

def intersection(l1,l2):
	l3=[]
	i=0
	j=0
	n=len(l1)
	while i<n:
		if l1[i]==l2[j]:
			l3.append(l1[i])
			i+=1
			j+=1
		else:
			i+=1
			j+=1		
	return l3

l1=[0,2,4,6,8,9,12]
l2=[0,1,3,6,7,9,12]
print intersection(l1,l2)
