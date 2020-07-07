'''

Creating the key

mainly:

K = χₖ + ψₖ  

'''
# Imports
import json
from rotor_modules import rotor, rotorbank, CHI, PSI, MU


# Vernam Function
def vernam(k, m):
	c = "".join(["1" if i!=j else "0" for i, j in zip(k, m)])
	return c

with open("chi_rotors.json", "r") as x, open("psi_rotors.json", "r") as p, open("mu_rotors.json", "r") as m:
	CHIDICT = json.load(x)
	PSIDICT = json.load(p)
	MUDICT 	= json.load(m)

with open("letter_lookup.json", "r") as l:
	lookup = json.load(l)
	inv_lookup = dict([(v, k) for k,v in lookup.items()])

# Boiler plate 5-space display
def display(x:str)->str:
	return ' '.join([x[i:i+5] for i in range(0, len(x), 5)])

# Main machine class
class Lorenz:

	'''
	
	params
	chi 	-> 	chi bank
	mu 		->	mu bank
	psi 	-> 	psi bank

	methods
	encrypt	->	encrypt a msg:
		output string
		for letter in msg
			get key
			add (letter XOR key) to output
			advance chi
			advance mu
			advance psi base on mu

	'''

	def __init__(self, chi, mu, psi):
		self.chi 	= chi
		self.mu 	= mu
		self.psi 	= psi

	def getKey(self):
		return vernam(self.psi.keystream(), self.chi.keystream())

	def getAdvanceStates(self):
		return f"Rotor Settings -> χ{str(self.chi.getAdvancement())} μ{str(self.mu.getAdvancement())} ψ{str(self.psi.getAdvancement())}"

	def set(self, x, m, p):
		self.chi.set(*x)
		self.mu.set(*m)
		self.psi.set(*p)

	def encrypt(self, m):
		output = ""
		m = m.upper().replace(" ", "")

		for letter in m:
			m = lookup[letter]
			k = self.getKey()

			c = vernam(m, k)

			output += inv_lookup[c]

			self.chi.advance()
			self.mu.advance()
			self.psi.advance(self.mu)


		return output




# TESTING
if __name__=="__main__":

	def initialise_lorenz():
		chi1, chi2, chi3, chi4, chi5 	= [v for _, v in CHIDICT.items()]
		psi1, psi2, psi3, psi4, psi5 	= [v for _, v in PSIDICT.items()]
		mu1, mu2						= [v for _, v in MUDICT.items() ]


		chi1 = rotor(chi1)
		chi2 = rotor(chi2)
		chi3 = rotor(chi3)
		chi4 = rotor(chi4)
		chi5 = rotor(chi5)

		psi1 = rotor(psi1)
		psi2 = rotor(psi2)
		psi3 = rotor(psi3)
		psi4 = rotor(psi4)
		psi5 = rotor(psi5)

		mu1  = rotor(mu1)
		mu2  = rotor(mu2)
		
		chibank = CHI(chi1, chi2, chi3, chi4, chi5)
		psibank = PSI(psi1, psi2, psi3, psi4, psi5)
		mubank 	= MU(mu1, mu2)

		lorenz = Lorenz(chibank, mubank, psibank)

		return lorenz


	def shell(lorenz):
		x = input("\nINPUT\t\t>>>\t").upper()

		print(f"\nCIPHERTEXT\t>>>\t{display(lorenz.encrypt(x))}\n\n")








	l = initialise_lorenz()

	while True:
		print(l.getAdvanceStates())

		setBool = (input("\nWould you like to change the rotor settings (Y/N)\n>>>\t").upper() == "Y")
		if setBool: 
			a = [eval(i) for i in input("\nInput settings, each separated by a '|' \n>>>\t").split("|")]
			l.set(*a)

		shell(l)
