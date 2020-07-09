'''

full shell

'''

from main_lorenz import *

# Main Function
def shell(LORENZ):
	command = input("\n\n>>>\t").upper().split(" ")

	if command[0] == "SET":
		if command[1] == "CHI":
			LORENZ.chi.set(*eval("[" + ', '.join(command[2:]) + "]"))

		elif command[1] == "MU":
			LORENZ.mu.set(*eval("[" + ', '.join(command[2:]) + "]"))

		elif command[1] == "PSI":
			LORENZ.psi.set(*eval("[" + ', '.join(command[2:]) + "]"))

		elif command[1][0] == "Ψ":
			a, b, c = [eval(i) for i in " ".join(command[1:]).replace("Ψ", "").replace("Μ", "|").replace("Χ", "|").split(" |")]
			LORENZ.chi.set(*[i for i in reversed(c)])
			LORENZ.mu.set(*[i for i in reversed(b)])
			LORENZ.psi.set(*[i for i in reversed(a)])



	elif command[0] == "ENC":
		print(display(LORENZ.encrypt(" ".join(command[1:]))))

	elif command[0] == "SHOW":
		print("\n" + LORENZ.getAdvanceStates())

	elif command[0] == "RANDOM":
		LORENZ.chi.random()
		LORENZ.mu.random()
		LORENZ.psi.random()

	elif command[0] == "RESET":
		LORENZ.chi.set(0,0,0,0,0)
		LORENZ.mu.set(0,0)
		LORENZ.psi.set(0,0,0,0,0)

	elif command[0] == "CLEAR":
		pass

	elif command[0] == "FORMAT":
		if command[1] == "OUTPUT":
			message = "".join(command[2:])
			print(message.replace("9", " ").replace("8", "-").replace("5", "+").replace("4", "<lf>").replace("3", "<cr>"))

		elif command[1] == "INPUT":
			message = " ".join(command[2:])
			print(display(message.replace(" ", "9").replace("-", "8").replace("+", "5").replace("&", "5").replace("<lf>", "4").replace("<cr>", "5")))

	return LORENZ

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

if __name__ == "__main__":
	l = initialise_lorenz()
	print("LORENZ Cipher Python 3 Shell")

	while True:
		l = shell(l)
