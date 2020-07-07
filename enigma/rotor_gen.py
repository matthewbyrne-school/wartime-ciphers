'''

ROTOR GENERATOR

Input: 	whatever the ROTOR maps ABCDEFGHIJKLMNOPQRSTUVWXYZ to 
Output:	JSON dict for that rotor
'''

x = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
def f(y):
	dic = {}
	for i, j in zip(x, y):
		dic[i]= j.upper()

	return dic

print(f("ABCDEFGHIJKLMNOPQRSTUVWXYZ"))