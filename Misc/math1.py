a = 2017
b = 1
for i in range (1,2016, 2):
	a = a + (i * (i + 1))
for i in range (2, 2017, 2):
	b = b + (i * (i + 1))
print(b - a)
