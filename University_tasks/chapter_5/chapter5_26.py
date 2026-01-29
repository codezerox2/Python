from sympy import harmonic
from math import log
n = int(input("inter a value n: "))
result = harmonic(n) + log(n)
print(f"result: {result}")
