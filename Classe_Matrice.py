class Matrice:
	def __init__(self,ligne,colonne):
		self.nb_l=ligne
		self.nb_c=colonne
		self.l=[]
		
		for i in range(0,self.nb_l):
			self.l.append([])
			for j in range(0,self.nb_c):
				self.l[i].append([0])
	
	def saisie(self):
		for i in xrange(0,self.nb_l):
			for j in xrange(0,self.nb_c):
				x=input("Entrer une valeur :")
				self.l[i][j]=x
	
	def affichage(self):
		for i in xrange(0,self.nb_l):
			for j in xrange(0,self.nb_c):
				print "|",self.l[i][j],"|"
			print " "
	
	def dimension(self):
		return self.nb_l,self.nb_c
	
	def aleatoire(self):
		for i in xrange(0, self.nb_l):
			for j in xrange(0,self.nb_c):
				x=uniform(-1,1)
				self.l[i][j]=x
	
	def addition(self,matrice):
		l1,h1=self.dimension()
		l2,h2=matrice.dimension()
		if l1!=l2 and h1!=h2:
			print "Erreur : Dimension incorect, veuillez reesayer"
		else :
			r=Matrice(l1,h1)
			for i in xrange(0,l1):
				for j in xrange(0,h1):
					r.l[i][j]=self.l[i][j]+matrice.l[i][j]
			r.affichage()
	
	def scalaire(self,k):
		for i in xrange(0,self.nb_l):
			for j in xrange(0,self.nb_c):
				self.l[i][j]*=k
		
		self.affichage()
		
	def produit(self,matrice):
		l1,h1=self.dimension()
		l2,h2=matrice.dimension()
		if l1!=h2 and h1!=l2:
			print "Erreur : Dimension incorect"
		else :
			m=Matrice(l1,h2)
			for i in xrange(0,l1):
				for j in xrange(0,h2):
					n=0
					for u in range(0,l2):
						n=self.l[i][u]*matrice.l[u][j]
					m.l[i][j]=n
			m.affichage()
