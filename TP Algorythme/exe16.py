# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Rôle : 
# Date : 29/11/2016
# Version : 3

def annee(an):
	p=an/100						#Permet d'afficher les 1er chiffres de l'année
	q=an%100						#Permet d'afficher les derniers chiffres de l'année avec le modulo
	return p,q

def date(jour,mois,an):
	x=0
	y=an-1
	if mois<3:
		y=an-1
		x=(((23*mois)/9)+jour+4+an+(y/4)-(y/100)+(y/400))%7
	elif mois>3:
		y=an
		x=(((23*mois)/9)+jour+4+an+(y/4)-(y/100)+(y/400)-2)%7
	return l[x]
	
def m(mois,l1):
	mois-=1
	return l1[mois]

l=["Dimanche","Lundi","Mardi","Mercredi","Jeudi","Vendredi","Samedi"]
l1=["Janvier","Février","Mars","Avril","Mai","Juin","Juiellet","Aout","Septembre","Octobre","Novembre","Décembre"]
jour=18
mois=3
an=1953

print "En année",an,"nous étions le",date(jour,mois,an),"du",jour,m(mois,l1)
