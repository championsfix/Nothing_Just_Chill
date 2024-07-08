# Putnam's Work

K = int(input("Total effort: ")) 	# total effort
td = int(input("Testing time: "))	# time of system and intregration testing
res = 0					# result
ch = int(input('''1. Poor development
2. Good development
3. Excellent development
= '''))
c = [2,8,11]
res = c[ch-1]*pow(K,1/3)*pow(td,4/3)

print(f"Product size in KLOC: {round(res)}")
