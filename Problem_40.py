# Champernowne's Constant
# problem 40

# an irrational decimal fraction is created by concatenating the positive integers:

# 				0.123456789101112131415161718192021...

# it can be seen that the Dn12 digit of the fractional part is 1
# if Dn, represents the nth digit of the fractorial part , find the value of the following expression
# Dn1 * Dn10 * Dn100 * Dn1,000 * Dn10,000 * Dn100,0000 * Dn1,000,000

def Champernowne():
	Champ = "0.1"
	for i in range(2,30000000):
		Champ += str(i)
	return Champ

jo = Champernowne()
Dn = int(jo[2]) * int(jo[11]) * int(jo[101]) * int(jo[1001]) * int(jo[10001]) * int(jo[100001]) * int(jo[1000001])

print(Dn)
# 210



