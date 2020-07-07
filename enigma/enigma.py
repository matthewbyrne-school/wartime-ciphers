'''
Enigma machine based on Enigma I with original 3 rotors

input -> plug -> I -> II -> III -> reflector -> III -> II -> I -> plug -> output
then spin I, checkspin for II and III
'''

# Imports
import json

# Boiler plate
with open("rotors.json", "r") as f:
	rotors = json.load(f)
	I = rotors["I"]
	II = rotors["II"]
	III = rotors["III"]
	reflectorA = rotors["reflectorA"]
	reflectorB = rotors["reflectorB"]
	reflectorC = rotors["reflectorC"]
	T = rotors["testRotor"]

def copy(x, *without): # copy a dictionary without certain items
	h = dict([(k, v) for k, v in x.items() if k not in without])
	return h




# Function for the enigma machine to function
def rotorSpin(rotor): # spin a rotor
	k = list(rotor.keys())
	v = [i for _, i in rotor.items()]
	v = v[1:] + [v[0]] 

	newRotor = dict([(i, j) for i, j in zip(k, v)])
	return newRotor

# Main enigma class
class Enigma:
	def __init__(self, I, II, III, reflector, setting=[0, 0, 0]):
		self.I = copy(I, "turnover") 		# first rotor
		self.II = copy(II, "turnover")		# second rotor
		self.III = copy(III, "turnover")	# third rotor
		self.refl = reflector 				# reflector

		self.i = I["turnover"]				# notch on the first rotor
		self.ii = II["turnover"]			# notch on the second rotor
		self.iii = III["turnover"]			# notch on the third rotor
		
		self.plugboard = dict([(chr(i), chr(i)) for i in range(65, 91)]) # {'A':'A', 'B':'B', ...}
		
		self.set(*setting)

	def set(self, a, b, c):
		a = a % 27 if a != 0 else 1
		b = b % 27 if b != 0 else 1
		c = c % 27 if c != 0 else 1

		while self.I["A"] != chr(a+64):
			self.I = rotorSpin(self.I)

		while self.II["A"] != chr(b+64):
			self.II = rotorSpin(self.II)

		while self.III["A"] != chr(c+64):
			self.III = rotorSpin(self.III)

	def addPlug(self, a, b):
		self.plugboard[a] = b
		self.plugboard[b] = a

	def spin(self):
		self.I = rotorSpin(self.I)

		if self.I["A"] == self.i:
			self.II = rotorSpin(self.II)

			if self.II["A"] == self.ii:
				self.III = rotorSpin(self.III)
				
	def encryptLetter(self, x):
		x = self.I[x]
		x = self.II[x]	
		x = self.III[x]	
		x = self.refl[x]		
		x = self.III[x]	
		x = self.II[x]	
		x = self.I[x]	
		
		return x
		
	def encrypt(self, msg):
		ciphertext = ""
		for m in msg.upper():
			if m == " ": ciphertext += " "; pass
			else:
				#'''
				c = self.plugboard[m]
				c = self.encryptLetter(c)				
				p = self.plugboard[c]
				#'''

				ciphertext += p # self.encryptLetter(m)
				self.spin()

		return ciphertext

	def decryptLetter(self, x):
		I = dict([(v, k) for k, v in self.I.items()])
		II = dict([(v, k) for k, v in self.II.items()])
		III = dict([(v, k) for k, v in self.III.items()])

		x = I[x]
		x = II[x]	
		x = III[x]	
		x = self.refl[x]		
		x = III[x]	
		x = II[x]	
		x = I[x]	
		
		return x

	def decrypt(self, msg):
		ciphertext = ""
		for m in msg.upper():
			if m == " ": ciphertext += " "; pass
			else:
				#'''
				c = self.plugboard[m]
				c = self.decryptLetter(c)				
				p = self.plugboard[c]
				#'''

				ciphertext += p # self.encryptLetter(m)
				self.spin()

		return ciphertext

def shell():
	while True:
		rotors = [eval(i) for i in input("Input a rotor order (default is: I II III)\n>>>\t").split(" ")]
		x=input('\nChoose a reflector (A, B, or C)\n>>>\t')
		reflector = eval(f"reflector{x.upper()}")
		setting = [int(i) for i in input("\nInput a setting (default is: 1 1 1)\n>>>\t").split(" ")]
		plugNumber = int(input("\nHow many plugs would you like to use\n>>>\t"))

		e = Enigma(*rotors, reflector, setting=setting)
		for _ in range(plugNumber):
			a, b = input("\nAdd a plug (in the form 'x-x', e.g. 'a-b')\n>>>\t").split("-")
			e.addPlug(a, b)

		while True:
			ed = input("\nE/D\n>>>\t").upper().replace(" ", "")
			if ed not in ["E", "D"]: print("\n"*5);break;
			msg = input("\n\n>>>\t")
			print("\n" + e.decrypt(msg) if ed == "D" else e.encrypt(msg))



# Runtime env
if __name__ == "__main__":
	e = Enigma(I, II, III, reflectorA, [5, 4, 3])
	print("HELLO WORLD ->", e.encrypt("HELLO WORLD"))	