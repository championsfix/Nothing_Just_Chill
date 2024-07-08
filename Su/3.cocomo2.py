# COCOMO 2
class COCOMO2:
	def __init__(self):
		self.screen = 0
		self.screen_complexity = []
		self.report = 0
		self.report_complexity = []
		self.modules = 0
		self.screen_table = [1,2,3]
		self.report_table = [2,5,8]
		self.productivity = 0
		self.productivity_table = [4,7,13,25,50]
		self.reuse = 0.10

	# screen, report, modules
	def get_values(self):
		self.screen, self.report, self.modules = map(int, input("Enter number of [screen, report, modules]:").split())
# 		print(self.screen)
		print("Enter Complexity (0: simple, 1: medium, 2: difficult)")
		print("Screen\n")
		for i in range(len(self.screen)):
			self.screen_complexity.append(self.screen_table[int(input(f"Screen {i}: "))])
		
		print("Report\n")
		for i in range(len(self.report)):
			self.report_complexity.append(self.report_table[int(input(f"Report {i}: "))])

	# productivity
	def productivity(self):
		self.productivity = self.productivity_table[int(input("Enter Productivity according developers experience-\n0. very low\n1. low\n2. norminal\n3. high\n4. very high"))]

	# final estimation
	def estimation(self):
		self.get_values()
		self.productivity()
		object_point = sum(self.screen_complexity) + sum(self.report_complexity)
		
# driving code
if __name__ == "__main__":
	cocomo = COCOMO2()
	cocomo.estimation()	
	
	
	
