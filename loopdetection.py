# detect loop and conditional statements
statements = ["while", "if", "else", "with", "def"]
index = dict(zip(statements, [0 for _ in range(len(statements))]))

# detection function
def detection(filename):
	with open(filename, "r") as file:
		lines = file.read().split("\n")
		for line in lines:
			if line.strip().split(" ")[0].lower() in statements:
				index[line.strip().split(" ")[0].lower()] += 1
	for idx, val in index.items():
		print(f"{idx}\t:{val}")

# driving code
if __name__ == "__main__":
	filename = input("Enter filename: ")
	detection(filename)
