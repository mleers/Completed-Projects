'''Unit test for conv_temp.py'''
#Enter values to simulate run, unittest tries function exceptions

import unittest
import conv_temp

n = float(input("Degrees Farenheit: "))    #test variable mirrored in parent module

class c_to_fBadInput(unittest.TestCase):    #defines test for blank Celsius inputs
	def test_Blank(self):
		'''c_to_f should fail with 0 input'''
		self.assertRaises(conv_temp.InvalidTemperatureError, conv_temp.c_to_f, '')

	def test_absolutezero(self):    #defines test for passing temperature limit (absolute zero in Celsius)
		'''c_to_f should fail when queried past absolute zero (-273.15)'''
		self.assertRaises(conv_temp.OutOfRangeError, conv_temp.c_to_f, -273.15)


class f_to_cBadInput(unittest.TestCase):    #defines test for blank Farenheit inputs
	def test_Blank(self):
		'''f_to_c should fail with 0 input'''
		self.assertRaises(conv_temp.InvalidTemperatureError, conv_temp.f_to_c, '')
	
	def test_absolutezero(self):    #defines test for passing temperature limit (absolute zero in Farenheit)
		'''f_to_c should fail when queried past absolute zero (-459.67)'''
		self.assertRaises(conv_temp.OutOfRangeError, conv_temp.c_to_f, -459.67)

class RoundTripCheck(unittest.TestCase):    #test for converting converted input to ensure original input is returned
	def test_Roundtrip(self):
		'''c_to_f(f_to_c(x)) == x for all x > -273.15'''
		if n > -459.67:
			temperature = conv_temp.f_to_c(n)
			result = conv_temp.c_to_f(temperature)
			self.assertEqual(n, result)


if __name__ == '__main__':
	unittest.main()
