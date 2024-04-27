def moduMod(n):
	lastTen = 0
	for i in range(1, n + 1):
		lastTen += i ** i % 10 ** 10
	return lastTen

print(moduMod(1000))