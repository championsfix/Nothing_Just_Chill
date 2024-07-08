# Norden's work
# Rayleigh Distribution

import math
import matplotlib.pyplot as plt

T = int(input("Total period: "))
td = int(input("Max value: "))
K = int(input("Area under curve: "))
E = list()	# effort

for t in range(T):
	E.append((K/(td**2))*t*(math.e**(-(t**2)/(2*(td**2))))*100)

plt.plot(list(range(T)), E)
plt.title("Norden's Distribution")
plt.xlabel("time (months)")
plt.ylabel("effort (manpower)")
plt.show()
