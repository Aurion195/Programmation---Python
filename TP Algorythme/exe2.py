# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Renvoie le nombre d'occurence
# Date : 18/11/2016
# Version : 1

def occurence(l,x):
	cpt=0
	for i in l:
		if i==x:
			cpt+=1
	return cpt
		
l=[1,5,6,1,8,5,6,37,5]
x=1
n=occurence(l,x)
print 'le nombre de fois que le chiffre',x,'apparait est',n,'fois'
