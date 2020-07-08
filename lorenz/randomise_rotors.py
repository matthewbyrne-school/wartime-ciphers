'''

RUNNING THIS FILE RANDOMISES THE ROTOR FILES ONLY RUN IF YOU WANT TO CHANGE THESE FILES

Make random Psi, Chi, and Mu rotors

'''

# Imports
from random import randint as rand
import json

# Importing the rotor files
with open("psi_rotors.json", "r") as p, open("chi_rotors.json", "r") as x, open("mu_rotors.json", "r") as m:
	psi = json.load(p)
	chi = json.load(x)
	mu 	= json.load(m)

# Main rotor gen
def rotorGen(rotor):
	rotor["cams"] = []
	for _ in range(rotor["n_cams"]):
		rotor["cams"].append(str(rand(0, 1)))
	return rotor

# Main runtime
if __name__ == "__main__":
	for k, p in psi.items():
		psi[k] = rotorGen(p)

	for k, x in chi.items():
		chi[k] = rotorGen(x)

	for k, m in mu.items():
		mu[k] = rotorGen(m)

	with open("psi_rotors.json", "w") as p, open("chi_rotors.json", "w") as x, open("mu_rotors.json", "w") as m:
		json.dump(psi, p)
		json.dump(chi, x)
		json.dump(mu,  m)
