# Jensen model

Cte = int(input("Effective technology constant: "))
td = int(input("Time to develop the software: "))
K = int(input("Effort needed to develop: "))

print(f"product size in KLOC: {round(Cte*td*pow(K,1/2))}")
