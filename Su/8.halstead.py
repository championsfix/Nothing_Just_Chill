# Halstead Software Science
import math

# readfiles
filename = input("filename: ")
operator = ["+", "-", "*", "/", "%", "="]
opcount = dict(zip(operator, [0 for _ in range(len(operator))]))

# open file
with open(filename, "r") as file:
	lines = file.read().split("\n")
	for line in lines:
		for a in list(line):
			if a in operator:
				opcount[a] += 1
	print(opcount)

# counts
n1 = int(input("unique operators: "))	# unique operators
n2 = int(input("unique operands: "))	# unique operands
N1 = int(input("total operators: "))	# total operators
N2 = int(input("total operands: "))		# total operands

# total counts
N=N1+N2
n = n1+n2
print("="*20)

# program volume
V = round(N*math.log2(n))
print(f"Program volume: {V}")

# estimated length
print(f"Estimated length: {round((n1*math.log2(n1))+(n2*math.log2(n2)))}")

# effort time
_V = (2+n2)*math.log2(2+n2)
L = _V/V
E = V/L
S = 18	# mental discrimination level (recommended)
T = E/S
print(f"time: {T}")
print(f"effort: {round(E)}")
print("="*20)
