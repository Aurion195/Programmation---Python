class Date:
    def __init__(self, jour=0, mois=0, annee=0):
        self.j=jour
        self.m=mois
        self.a=annee

    def saisir(self):
		s=raw_input("Entrer une date du jour :")
		r=s.rsplit("/")
		
		self.j=int(r[0])
		self.m=int(r[1])
		self.a=int(r[2])

    def affichage(self):
        print "{}/{}/{}".format(self.j,self.m,self.a)
        
	def __le__(self,d2):
		if self.a>d2.a: return True
		if self.a<d2.a: return False
		if self.m>d2.m: return True
		if self.m<d2.m: return False
		if self.m>d2.m: return True
		else: return False

#-------------------------------------------------------------------------------------------

class Ingredient:
	def __init__(self, nom=" ", qte=0, unite=" "):
		self.n=nom
		self.q=qte
		self.u=unite
	
	def saisi_I(self):
		self.n=raw_input("Entrer un nom d'ingredient : ")
		self.q=input("Entrer une quantite :")
		self.u=raw_input("Entrer une unite :")
	
	def affichage_I(self):
		print "		> {}	{} {}".format(self.n,self.q,self.u)
		
#-------------------------------------------------------------------------------------------

class PA:
	def __init__(self):
		self.n=" "
		self.m=" "
		self.r=" "
		self.dp=Date(00,00,0000)
		self.de=Date(00,00,0000)
		self.lp=" "
		self.li=list()
	
	def saisi_P(self):
		self.n=raw_input("Entrer le nom d'une recette :")
		self.m=raw_input("Entrer la marque d'une recette :")
		self.r=raw_input("Enrer une references :")
		self.dp.saisir()
		self.de.saisir()
		self.lp=raw_input("Entrer un lieu de production :")
		nb=input("Entrer un nombre d'ingredient :")
	
		for i in xrange(nb):
			x=Ingredient()
			x.saisi_I()
			
			self.li.append(x)
	
	def affichage(self):
		print "> Le nom du produit est :",self.n
		print "> Le nom de la marque est :",self.m
		print "> La reference du produit est :",self.r
		print "> La date de production du produit est :",self.dp.affichage()
		print "> La date d'expriration du produit est le :",self.de.affichage()
		print "> Le lieux de production du produit est : ",self.lp
		print "> Les ingredient necessaires sont :","\n"
		for i in self.li:
			x=i.affichage_I()
			
		print "\n","-"*25,"\n"

#---------------------------------------------------------------------

class Produit:
	def __init__(self):
		self.prod=list()
	
	def ajouter(self,PA):
		self.prod.append(PA)
	
	def chercher_n(self,nom):
		for i in self.prod:
			if i.n.lower()==nom.lower():
				return i
				
	def chercher_i(self, ingredient):
		for i in self.prod:
			for x in i.li:
				if x.n.lower()==ingredient.lower():
					return i
	
	def vente(self, vente):
		for i in self.prod:
			if i.n==vente:
				self.prod.remove(i)
		
	def date(self, date_exp):
		for i in self.prod:
			if i.de<date_exp:
				self.prod.remove(i)
				return self.prod
		
p1=PA()
p2=PA()
p3=PA()

p1.n="Gateau chocolat"
p1.m="Bonne maman"
p1.r="#1"
p1.dp="05,01,2017"
p1.de="07,05,2017"
p1.lp="Cavaillon"
p1.li.append(Ingredient("Farine", 600, "gr"))
p1.li.append(Ingredient("Chocolat", 250, "gr"))
p1.li.append(Ingredient("Oeuf", 4, ""))
p1.li.append(Ingredient("Levur", 10, "g"))


p2.n="Rizotto"
p2.m="Pascale"
p2.r="#2"
p2.dp="01,01,2017"
p2.de="25,01,2017"
p2.lp="Cavaillon"
p2.li.append(Ingredient("Viande", 600, "gr"))
p2.li.append(Ingredient("Riz", 1200, "gr"))
p2.li.append(Ingredient("Champignon", 200, "gr"))
p2.li.append(Ingredient("Sauce", 50, "cl"))

p3.n="Civet de chevreuil"
p3.m="Pascale"
p3.r="#3"
p3.dp="05,01,2017"
p3.de="15,01,2018"
p3.lp="Cavaillon"
p3.li.append(Ingredient("Chevreuil", 600, "g"))
p3.li.append(Ingredient("Sauce", 100, "g"))
p3.li.append(Ingredient("Pomme de terre", 200, "g"))
p3.li.append(Ingredient("Sel et Poivre", 2, "g"))

mag=Produit()
mag.ajouter(p1)
mag.ajouter(p2)
mag.ajouter(p3)

mag.vente("Rizotto").affichage()
