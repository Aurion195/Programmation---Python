# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : Calcul du pgcd de deux nombres
# Date : 29/11/2016
# Version : 3

def pgcd(p,q):
	if p>q and p%q==0:						#si le modulo des deux nombres et 0 alors il est égal à p si p est supérieur à q
		return q
	elif q>p and q%p==0:					#dans le cas ou q est supérieur à p
		return p
	else:
		return pgcd(q,p%q)
 
 
p=input("Nombre a : ")
q=input("Nombre b : ")
print "Le pgcd de ",p,"et",q," est ",pgcd(p,q)
