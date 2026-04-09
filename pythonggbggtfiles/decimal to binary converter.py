import math
l = input("longueur du nombre en binaire ")
i = int(l)
n = input("nombre a transformer ")
nb = int(n)
bn = ""
while i > -1:
	c = math.pow(2, i)
	if nb > c or nb == c:
		bn = bn, "1"
		nb = nb - c
	else:
		bn = bn, "0"
	i = i - 1
print(bn)
