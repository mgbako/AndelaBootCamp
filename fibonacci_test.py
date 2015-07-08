import unittest, fibonacci

class FibonacciTest(unittest.TestCase) :
	def testNonInt(self):
		self.assertEqual(fibonacci.fibonacci("dfgdsd"), -1, msg="Number must return false if it is alphatical")

	def testPositiveNumber(self):
		self.assertEqual(fibonacci.fibonacci(5), 5, msg="Number must return 5")

	def testNegativeNumber(self):
		self.assertEqual(fibonacci.fibonacci(-4), -1, msg="Number must return false if it is less than 0")

	def testOptionalParameter(self):
		self.assertEqual(fibonacci.fibonacci() -1, msg="Number must return false if parameter is not set set")

	def testDecimalInput(self):
		self.assertEqual(fibonacci.fibonacci(2.33), -1, msg="Number must return false if it is a decimal number")

	# def testTypeOfParameter(self):
	# 	self.assertEqual(fibonacci.fibonacci(list(2,2,4)), -1, msg="Number must return false if it is not a list")

if __name__ == '__main__':
	unittest.main()		