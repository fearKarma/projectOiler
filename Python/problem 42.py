""" 
the nth term of the sequence of triangle numbers is given by, Tn = 1/2n(n + 1) so the first ten trianle numbers are:
											1,3,6,10,15,21,28,36,45,55
By converting each letter in a word to a number corresponding to its 
alphabetical position and adding these values we form a word value. 
For example, the word value for SKY is 19 + 11 + 25 = 55 = T10. 
If the word value is a triangle number then we shall call the word a triangle word.	

"""

def TriangleNumberList():
	upper_limit = 26 * 26
	list_tri = []
	for i in range(1,upper_limit):
		test = i * (i + 1) / 2
		list_tri.append(int(test))
	return list_tri	

def GetAlphaSum(n):
	alphaValue = ['"',"A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
	tnums = TriangleNumberList()
	tWords = 0
	for i in n:
		tWords += alphaValue.index(i)
	if (tWords in tnums):
		return True
	else:
		return False

wordsTrue = []

words = open("words.txt", "r")
wordLife = words.read()
wordsFile = wordLife.split(",")




for x in wordsFile:
	if GetAlphaSum(x):
		wordsTrue.append(x)

print(len(wordsTrue))

#162
