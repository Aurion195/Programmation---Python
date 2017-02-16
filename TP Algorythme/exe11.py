# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Renvoie une nouvelle liste
# Date : 22/11/2016
# Version : 1
	
def fusion(l,L):
	l1=[]
	i=0 								#pour la liste l
	j=0									#pour la liste L
	while i<len(l) and j<len(L):
		if l[i]<=L[j]:
			l1.append(l[i])
			i+=1
		else:
			l1.append(L[j])
			j+=1
	if i==len(l):
		for e in range(j,len(L)):
			l1.append(L[e])
	else:
		for x in range(i,len(l)):
			l1.append(l[x])
	return l1

l=[0,2,4,6,8,10,11,12,14,15,16]
L=[1,3,5,7,8,11,12,13,14]
print fusion(l,L)
