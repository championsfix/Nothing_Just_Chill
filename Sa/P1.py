'''WAP in python for a function that computes the squareroot of the integer values in the range of 0 and 5000, determine the boundary value test suit in the dynamic way'''

import math
import unittest
res=[]	
class Square_test:
	def __init__(self,value):
		self.value=value
		
	def get_square_root(self):
		i=0
		for i in range(0,self.value+1):
			res.append(math.sqrt(self.value))
			print(res)
		return res	
	def set_width(self,value):
		self.value=value
		
class Test(unittest.TestCase):
	def runTest(self):
		number=(int)(input("Enter the value:"))
		
		if number<=5000 and number>=0:
			square=Square_test(number)
			self.assertEqual(square.get_square_root(),res,'Correct Output generated!')
		else:
			self.assertEqual(square.get_square_root(),res,'out of boundary array list')
unittest.main()
	


		
	
