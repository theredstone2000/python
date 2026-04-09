import math
import modulo
m = 999999999999
a = modulo.mod(m, 19)
b = modulo.mod(m, 4)
c = modulo.mod(m, 7)
d = modulo.mod(19 * a + 24, 30)
e = modulo.mod(2 * b + 4 * c + 6 * d + 5, 7)
e = math.floor(e)
if d + e < 9 or d + e == 9:
    print(d + e + 22, end="mars")
else:
    print(d + e - 9, end="avril")
