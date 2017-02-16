# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Calcul des sorties
# Date : 28/11/2016
# Version : 1

def reel(l1,x,epsilon):
	for e in l1:
		if -epsilon<(e-x)<epsilon:
			return True
	return Fasle

l1=[0,1,2,3,4,5,6,7,8,9,10]
x=4
epsilon=2
print reel(l1,x,epsilon)
