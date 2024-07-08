# COCOMO cost estimation using function point matrix

class Matrix:
	def __init__(self):
		self.matrix = [0,0,0,0,0]
	
	def calculate_matrix(self, inputs, outputs, inquiries, files, interfaces):
		self.matrix = [inputs, outputs, inquiries, files, interfaces]
	
	def calculate_matrix_from_file(self, filename):
		# code
		pass
	
	def calculate_cost(self):
		print("Enter DOF between 0 to 6:")
		print("0 - No Influence\n1 - Incidental\n2 - Moderate\n3 - Average\n4 - Significant\n5 - Essential ")
		lines = '''1. Requirement for reliable backup and recovery = 
2. Requirement for data communication = 
3. Extent of distributed processing = 
4. Performance requirements = 
5. Expected operational enviornment = 
6. Extent of online data entries = 
7. Extent of multi-screen or multioperation online data input = 
8. Extent of online updating of master files = 
9. Extent of complex inputs outputs online queries and files = 
10. Extent of complex data processing = 
11. Extent that currently developed code can be designed for reuse = 
12. Extent of conversion and installation included in the design = 
13. Extent of multiple installations in an organization and variety of customer organizations = 
14. Extent of change and focused on ease of use = '''.split("\n")
		dof = []
		for line in lines:
			dof.append(int(input(line)))
		UFP = (self.matrix[0]*4)+(self.matrix[1]*5)+(self.matrix[2]*4)+(self.matrix[3]*10)+(self.matrix[4]*7)
		TCF = 0.65 + (0.01*sum(dof))
# 		print(TCF)
		return round(UFP * TCF)

# driving code
if __name__ == "__main__":
	matrix = Matrix()
	matrix.calculate_matrix(2,1,4,1,2)
	print(f'Estimated Cost: {matrix.calculate_cost()} months')
