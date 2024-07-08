import unittest

def array_sum(arr):
    return sum(arr)

def array_max(arr):
    return max(arr)

def array_min(arr):
    return min(arr)

def array_function(arr):
    a = array_sum(arr)
    b = array_max(arr)
    c = array_min(arr)

    return [a,b,c]

class TestStringMethods(unittest.TestCase):
    def test_strings_a(self):
        self.assertEqual(array_function([1,3,5]),[9,5,1],"Prctice More!!")
    
  
if __name__ == '__main__':
    unittest.main()
