# COCOMO COST ESTIMATION
# Suvasish 2024
def kloc(filename, path=""):
	'''
	Args:	filename (string): input file to count total KLOC
		path (string): 	path to the source file
				default = ""
	Return: total kilo lines of code in that file
	'''
	with open(path+filename, "r") as file:
		content = file.read().split("\n")
		
	# count all valid lines
	counter = 0
	flag = False
	for line in content:
		if line.strip().startswith("#") or line.strip() == "":
			continue
		elif flag == False and line.strip().startswith("'''"):
			flag = True
		elif flag == True and line.strip().endswith("'''"):
			flag = False
		elif flag == False:
#			print(line)
			counter += 1
	return counter
	
def estimation(kloc, type):
	'''
	Args:	kloc (int): total kilo lines of code
		type (int): type of model {0:ORGANIC, 1:SEMIDETECH, 2:EMBIDDED}
	Return:	None
	'''
	a1 = [2.4, 3.0, 3.6]
	a2 = [1.05, 1.12, 1.20]
	b1 = [2.5, 2.5, 2.5]
	b2 = [0.38, 0.35, 0.32]
	effort = a1[type]*(kloc**a2[type])
	tdev = b1[type]*(effort**b2[type])
	print(f'Effort: {round(effort)} person month')
	print(f'Time to development: {round(tdev)} months')
	
# driving code
if __name__ == "__main__":
	filename = input("Enter Filename: ")
	type = int(input('''Select type of model:
	1. Organic
	2. Semideteched
	3. Embidded
	= '''))
	kloc = kloc(filename)
	print(f'Total kilo-line-of-code in {filename}: {kloc}')
	estimation(kloc, type-1)
	
