# -*- coding: utf-8 -*-
# Auteur : MATHIEU Thomas
# Date : 13/01/2017
# Version : 1

class Date:												#1 a/b/c
	def __init__(self, jour=0, mois=0, an=0):
		self.j=jour
		self.m=mois
		self.a=an
	
	def saisie_date(self):
		s=raw_input("Entrer une date : ")
		r=s.rsplit("/")
		
		self.j=int(r[0])
		self.m=int(r[1])
		self.a=int(r[2])
	
	def affichage_date(self):
		print "{}/{}/{}".format(self.j, self.m, self.a)

d=Date()
d.saisie_date()
d.affichage_date()
print "\n","--------------------","\n"

#---------------------------------------------------------------------------------

class Etudiant:																#2 a/b/c/d/e/f/g
	def __init__(self, nom=" ", prenom=" ", jour=0,  mois=0, an=0,):
		self.n=nom
		self.p=prenom
		self.j=jour
		self.m=mois
		self.a=an
		self.l=[]
	
	def note(self):
		n=input("Combien voulez-vous entrer de notes : ")
		x=0
		for i in xrange(0,n):
			x=input("Entrer une note : ")
			self.l.append(x)
		
		return self.l
		
	
	def saisie_etudiant(self):
		self.n=raw_input("Entrer le nom : ")
		self.p=raw_input("Entrer le prénom :")
		self.j=input("Entrer le jour :")
		self.m=input("Entrer le mois :")
		if self.m>12:
			self.m=input("Entrer un nombre de mois inferieur à 12 : ")
		self.a=input("Entré une année : ")
		self.l=self.note()
	
		
	def affichage_etudiant(self):
		x=2017
		x-=self.a
		print "{} {} : ".format(self.p, self.n)
		print x," ans"
		print "Voici la liste de notes : ",self.l

			
	def moyenne(self):
		moy=0
		for i in self.l:
			moy+=i
		moy/=len(self.l)
		
		return moy
	
	def module(self):
		moy=self.moyenne()
		if moy>=10 :
			return True
		else : 
			return False
	
	def maxi(self):
		ind=0
		for i in xrange(0,len(self.l)):
			if i>ind:
				ind=i
		return ind
	
	def trier(self):
		tri=list()
		while len(self.l)>0:
			m=self.maxi()
			tri.append(self.l[m])
			self.l.remove(self.l[m])
		return self.l

x=Etudiant()
x.saisie_etudiant()
x.affichage_etudiant()	
print " la moyenne est de : ",x.moyenne()

if x.module()==True:
	print "Bravo, tu as ton dîplome "
else :
	print "Désolé, tu n'as pas recu ton dîplome .."

print x.trier()
print "\n","--------------------","\n"
		
#---------------------------------------------------------------------		

class College:															#3 a/b/c/d
	def __init__(self, nom=" "):
		self.n=nom
		self.liste=[]
	
	def ajouter(self, Etudiant):
		self.liste.append(Etudiant)
	
	def afficher_college(self):
		print "College : ",self.n
		print "\n"
		
		for i in self.liste:
			i.affichage_etudiant()
			print "\n"
	
	def moyenne_general(self):
		moy = 0.0
		x=0.0
		for i in self.liste:
			for j in i.l:
				moy+=j
				x+=1
		moy/=x
		
		return moy
	
	def moyenne_eleve(self):
		maxi=0
		ind_max=0
		for i in self.liste:
			moy=0
			for j in i.l:
				moy+=j
			moy/=len(i.l)
			if moy>maxi:
				maxi=moy
				ind_max=i.n
		return ind_max,maxi
	
	def moyenne_basse(self):
		mini=20
		ind_min=0
		for i in self.liste:
			moy=0
			for j in i.l:
				moy+=j
			moy/=len(i.l)
			if moy<mini:
				mini=moy
				ind_min=i.n
		return ind_min,mini
		
	def naissance(self,x):
		moy=0
		cpt=0
		for i in self.liste:
			if i.a==x:
				for j in i.l:
					moy+=j
					cpt+=1
				moy/=cpt
		
		return moy
	
	def reussi(self):
		x=10
		R=list()
		moy=0
		for i in self.liste:
			for j in i.l:
				moy=j.moyenne_general()
			if moy>=10:
				R.append(i)
		return R
				
e1=Etudiant()
e2=Etudiant()
e3=Etudiant()

e1.n="Stark"
e1.p="Tony"
e1.j=20
e1.m=10
e1.a=1987
e1.l.append(10.0)
e1.l.append(15.0)
e1.l.append(5.0)

e2.n="Rogers"
e2.p="Steve"
e2.j=25
e2.m=8
e2.a=1927
e2.l.append(15.0)
e2.l.append(12.0)
e2.l.append(18.0)

e3.n='Parker'
e3.p='Peeter'
e3.j=25
e3.m=8
e3.a=1997
e3.l.append(18.0)
e3.l.append(15.0)
e3.l.append(17.0)

c=College("Marvel")
c.ajouter(e1)
c.ajouter(e2)
c.ajouter(e3)
c.afficher_college()

print "La moyenne générale du collège est de :",c.moyenne_general()
print "La moyenne la plus élevé appartient à : ",c.moyenne_eleve()
print "La moyenne la plus basse appartient à : ",c.moyenne_basse()
print "La moyenne pour cette année de naissance est de : ",c.naissance(1997)
