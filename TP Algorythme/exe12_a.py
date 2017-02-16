# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Calcul des sorties
# Date : 22/11/2016
# Version : 1

from math import sqrt

def discriminant(a,b,c):
	disc=0
	disc=b**2-4*a*c
	nb=0											
	if disc==0:
		nb+=1
		return 	nb
	elif disc>0:
		nb+=2
		return nb
	elif a==0 and b==0 and c==0:
		nb+=3
		return nb
	elif a==0 and b==0:
		if c==0:
			nb+=3
			return nb
		else:
			nb=0
			return nb
	elif a==0:
		nb+=1
		return nb
	else:
		nb=0
		return nb
		
def calcul(a,b,c):
	disc=0
	disc=b**2-4*a*c
	if disc==0:
		x1=(-b/2*a)
		return x1
	elif disc>0:
		x1=(-b+sqrt(disc))/(2*a)
		x2=(-b-sqrt(disc))/(2*a)
		return x1,x2
	else:
		x1=-c/b
		return x1
	
def resultat(a,b,c):
	nb=discriminant(a,b,c)
	x1=calcul(a,b,c)
	x2=calcul(a,b,c)
	if nb==1:
		print "Il y a une solution qui est",x1
	elif nb==2:
		print "Il y a deux solutions qui sont",x1
	elif nb==3:
		print "Il y a une infinités de solutions"
	else:
		print "Il n'y a pas de solution"
	

a=input("Entrer une valeur pour a :")
b=input("Entrer une valeur pour b :")
c=input("Entrer une valeur pour c :")
print resultat(a,b,c)

