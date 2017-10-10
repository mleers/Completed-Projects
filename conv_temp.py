import re
class InvalidTemperatureError(ValueError): pass
class OutOfRangeError(ValueError): pass
	
print("Welcome to the temperature converter")
#def main():    #global module functions disabled for purpose of unit testing.  Can be re-enabled for restart option.	
table = {	
		"1": "C to F",
		"2": "F to C"
}
	
	
	
def c_to_f(x):    #Celsius to Farenheit converter
	'''converts Celsius integer to Farenheit'''
	if not x:
		raise InvalidTemperatureError('entry must not be blank')
	if not (-273.15 < float(x)):    
		raise OutOfRangeError('entry must be above absolute zero (-273.15 C)')
	
	y = (float(x)*(9/5) + 32)
	return y
	
def f_to_c(n):    #Farenheit to Celsius converter
	'''converts Farenheit integer to Celsius'''
	if not n:
		raise InvalidTemperatureError('entry must not be blank')
	if not (-459.67 < float(n)):
		raise OutOfRangeError('entry must be above absolute zero (-459.67 C)')
	m = (float(n) - 32)*(5/9)
	return m
	
	
for keys in table:
	print(keys, table[keys])
	
choice = input("Which conversion would you like to pick?")
while choice not in table:
	choice = input("You must pick 1 or 2")
	
if choice in table:
	print("You have chosen option {}, or {}".format(choice, table[choice]))
	
	
if choice == "1":
	x = input("Degrees Celsius: ")
	while not re.match("^-?[0-9]\d*(\.\d+)?$", x):    #regex for all numbers +/-, float type and "-" cause disagreement with "int" type
		x = input("You must enter a number to continue")
	while float(x) <= float(-273.15):
		x = input("You must enter a temperature greater than absolute zero (-273.15C)")
	print("{} degrees Farenheit".format(c_to_f(x)))
#	restart()
elif choice == "2":
	n = input("Degrees Farenheit: ")
	while not re.match("^-?[0-9]\d*(\.\d+)?$", n):    #optional negative (-) and decimal (.) signs to mediate float/int/str disagreement
		n = input("You must enter a number to continue")
	while float(n) <= float(-459.67):
		n = input("You must enter a temperature greater than absolute zero (-459.67F)")
	print("{} degrees Celsius".format(f_to_c(n)))
#	restart()

#def restart():    #reinitialize option
#	while True:
#		ans = input("Would you like to convert another temperature? (y/n)").lower()
#		while ans != "y" and ans != "n":
#			ans = input("You must pick (y/n)")
#		if ans == "y": True, main()
#		elif ans == "n": False, quit()

#main()
