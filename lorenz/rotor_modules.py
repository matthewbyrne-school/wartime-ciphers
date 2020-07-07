'''

ALL CLASSES for rotors




classes involved:

generic
rotor 		->		this is a non-descript, all-purpose rotor class
rotorbank 	->		this is an all-purpose rotorbank class

specific
CHI			->		this is a subclass of rotorbank for the CHI type rotors
PSI			-> 		this is a subclass of CHI class for the PSI type rotors
MU 			->		this is a standalone rotorbank class for the MU type rotors 
'''



# Rotor class
class rotor:
	'''
	params
	
	cams 		->	all cams
	state 		-> 	current first bit
	size		->	size of the rotor
	advstate	->	the amount of turns the machine has done


	methods

	advance	->	advance wheel by 1
	'''

	def __init__(self, rotor):
		self.size 		= rotor["n_cams"]
		self.cams 		= rotor["cams"]
		self.state		= self.cams[0]
		self.advstate	= 0

	def advance(self):
		self.cams 		= 	self.cams[1:] + [self.cams[0]]
		self.state 		=	self.cams[0]
		self.advstate	=	(self.advstate+1) % (self.size) # dont touch this


# Rotorbank class
class rotorbank:
	'''
	params

	rotors		->	all rotors involved
	

	methods

	keystream	->	the states of all of the rotors in order
	

	'''

	def __init__(self, *rotors):
		self.rotors = list(rotors)
		self.r1, self.r2, self.r3, self.r4, self.r5 = rotors

	def getAdvancement(self):
		return [r.advstate for r in self.rotors]

	def keystream(self):
		k = ""

		for rotor in self.rotors:
			k += rotor.state

		return k

class CHI(rotorbank):
	def advance(self):

		self.r1.advance()
		if self.r1.advstate == 0:

			self.r2.advance()
			if self.r2.advstate == 0:

				self.r3.advance()
				if self.r3.advstate == 0:

					self.r4.advance()
					if self.r4.advstate == 0:

						self.r5.advance()

	def set(self, I, II, III, IV, V):
		while self.r1.advstate != I:
			self.r1.advance()

		while self.r2.advstate != II:
			self.r2.advance()

		while self.r3.advstate != III:
			self.r3.advance()

		while self.r4.advstate != IV:
			self.r4.advance()

		while self.r5.advstate != V:
			self.r5.advance()

class PSI(CHI):
	def advance(self, mu_bank):
		if mu_bank.doAdvance == True:
			super().advance()


class MU(rotorbank):
	def __init__(self, mu1, mu2):
		self.I 	= mu1 if mu1.size == 61 else mu2
		self.II = mu2 if self.I == mu1 else mu1

		self.rotors = [mu1, mu2]

		self.doAdvance = (self.II.state == "1") # allow psi bank to advance

	def advance(self):
		self.I.advance()

		if self.I.state=="1":
			self.II.advance()

		self.doAdvance = (self.II.state == "1")

	def set(self, I, II):
		while self.I.advstate != I:
			self.I.advance()

		while self.II.advstate != II:
			self.II.advance()