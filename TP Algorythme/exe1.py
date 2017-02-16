# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Cherche un élément x dans une liste
# Date : 18/11/2016
# Version : 1

def chercher(l,x):
	for i in range(0,len(l)):
		if l[i]==x:
			return True
	return False

l=[1,2,3,4,5,6]
x=6
if (chercher(l,x)==True):
	print True
else:
	print False
