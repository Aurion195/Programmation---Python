class date:
	def __init__(self, jour=1,mois=1,annee=0000):
		self.j=jour
		self.m=mois
		self.a=annee
	
	def saisir(self):
		s=raw_input("Entrer une date :")
		r=s.rsplit("/")
		
		self.j=int(r[0])
		self.m=int(r[1])
		self.a=int(r[2])
	
	def affichage(self):
		print "{}/{}/{}".format(self.j,self.m,self.a)
