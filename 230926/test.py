# def sum(x, y) :
#     return x + y

# a = 10
# b = 20
# c = sum(a, b)
# print(c)

# import unittest
import myfunction

# class MyTest(unittest.TestCase) :
#     def test_sum(self):
#         self.assertEqual(myfunction.sum(2, 5), 7)
        
#     def test_multiple(self):
#         self.assertEqual(myfunction.multiple(2, 5), 10)
# python -m unittest test.py

def  test_sum() :
    assert myfunction.sum(2, 5) == 7
    assert myfunction.sum(2.3, 5.2) == 7.5
    
def test_multiple() :
    assert myfunction.multiple(2, 5) == 10
    assert myfunction.multiple(2.0, 5.0) == 10.0
# pytest test.py