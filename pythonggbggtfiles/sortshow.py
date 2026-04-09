import my_modules.sort as sort
import random as rng
a = [rng.randint(1,10),rng.randint(1,10),rng.randint(1,10),rng.randint(1,10),rng.randint(1,10)]
print("bubble : ", a)
sort.bubble(a)
print("bubble : ", a)
b = [rng.randint(1,10),rng.randint(1,10),rng.randint(1,10),rng.randint(1,10),rng.randint(1,10)]
print("bogo", b)
sort.bogo(b)
print("bogo", b)