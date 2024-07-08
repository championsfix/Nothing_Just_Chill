import matplotlib.pyplot as plt
EffortBox=[]
TimeBox=[]
PersonBox=[]
def calculation(table,mode,KLOC):
	Effort = 0
	Time = 0
	Person = 0
	model = 0
	if(KLOC >= 2 and KLOC <= 50):
		model = 0
	elif(KLOC> 50 and KLOC <= 300):
		model = 1
	elif(KLOC > 300):
		model = 2
	
	print("Model: ", mode[model])
	
	Effort = table[model][0]*pow(KLOC, table[model][1])
	
	Time = table[model][2]*pow(Effort, table[model][3])
	
	Person = Effort/Time
	
	'''print("Effort = {} Person-Month".format(round(Effort)))
	print("Development Time = {} Months".format(round(Time)))
	print("Average Staff Required = {} Persons".format(round(Person)))'''
	
	EffortBox.append(Effort)
	TimeBox.append(Time)
	PersonBox.append(Person)

def graph(KLOC):
	table = [[2.4,1.05,2.5,0.38],[3.0,1.12,2.5,0.35],[3.6,1.20,2.5,0.32]]
	mode = ["Organic","Semi-Detached","Embedded"]
	#KLOC = int(input("Enter the size: "))
	calculation(table,mode, KLOC)

def main():
	global EffortBox,TimeBox,PersonBox
	arraylist=[]
	for i in range(1,5000):
		arraylist.append(i)
		graph(i)
	
	#fig, axs=plt.subplots(3)	
	#axs[0].plot(arraylist,PersonBox)
	plt.plot(arraylist,PersonBox)
	plt.show()
	#axs[0].plot(arraylist,TimeBox)
	plt.plot(arraylist,TimeBox)
	plt.show()
	#axs[0].plot(arraylist,EffortBox)
	plt.plot(arraylist,EffortBox)
	plt.show()
	#plt.show()	

if __name__ == '__main__':
	main()
