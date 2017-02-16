from math import *

class Point:
	def __init__(self):
		self.x=0.0
		self.y=0.0
		self.z=0.0

	def saisi(self):
		self.x=input("Entrer une valeur pour x :")
		self.y=input("Entrer une valeur pour y :")
		self.z=input("Entrer une valeur pour z :")
	
	def affichage(self):
		print "({},{},{})".format(self.x,self.y,self.z)
	
	def ing__egal(self,p):
		if self.x<p.x: return True
		elif self.x>p.x: return False
		if self.y<p.y: return True
		elif self.y>p.y: return False
		if self.z<p.z: return True
		elif self.z>p.z: return False
		else: return True
	
	def distance(self,p):
		dist=0.0
		dist=sqrt((self.x-p.x)**2+(self.y-p.y)**2+(self.z-p.z)**2)
		
		return dist
		
	def appartient(self,p):
		app=Point()
		app=self.distance(p)
		if app<0.00001:return True
		else: return False
	
class collection:
	def __init__(self):
		self.li=list()
	
	def ajouter(self,Point):
		self.li.append(Point)
			
	def affichage_c(self):
		for i in self.li:
			i.affichage()
	
	def intersection(self,x):
		p_inter=[]
		for i in self.li:
			for e in x.li:
				if i==e: 
					p_inter.append(l[i])
		
		return p_inter
		
	def gravite(self):
		cpt_x=0
		cpt_y=0
		cpt_z=0
		x=0
		y=0
		z=0
		moy=0
		for i in self.li:
			x=
			
	

#Class collection
p1=Point()
p2=Point()
p3=Point()
p4=Point()
p1.saisi()
p2.saisi()
p3.saisi()

l=collection()
l1=collection()

l.ajouter(p1)
l.ajouter(p2)



