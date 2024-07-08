def calculation(table,mode ,KLOC):
	Effort = 0
	Time = 0
	Person_Required = 0
	model = 0
	if(KLOC >= 2 and KLOC<= 100):
		model = 0
	elif(KLOC > 100 and KLOC <= 500):
		model = 1
	elif(KLOC > 500):
		model = 2
	print("Model: ", mode[model])

	Effort = table[model][0]*pow(KLOC, table[model][1])
	Time = table[model][2]*pow(Effort, table[model][3])
	Person_Required = Effort/Time
	
	print("Effort = {} Person-Month".format(round(Effort)))
	print("Development Time = {} Months".format(round(Time)))
	print("Average Staff Required = {} Persons".format(round(Person_Required)))

def main():
	table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
	mode = ["Organic","Semi-Detached","Embedded"]
	KLOC = 1800
	calculation(table, mode, KLOC)

if __name__ == '__main__':
	main()
