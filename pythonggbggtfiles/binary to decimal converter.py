l = input("longueur de ton nombre binaire ")
i = int(l)
nb = 0
c = 1
while i > -1:
	d = input("0 ou 1 ?")
	b = int(d)
	nb = nb + b * c
	c = c * 2
	i = i - 1
print(nb)