def main():
	import json
	from collections import Counter
	from bokeh.plotting import figure, show, output_file
	
	birthday = {}
	months = []
	
	with open("birthday_list.json", "r") as f:    #json file made externally in python
		birthday = json.load(f)
	
	month_to_name = {
		1: "January",
		2: "February",
		3: "March",
		4: "April",
		5: "May",
		6: "June",
		7: "July",
		8: "August",
		9: "September",
		10: "October",
		11: "November",
		12: "December"
	}
	
	for name, birthdays in birthday.items():    #converts birthday months from categorical to numerical
		month = int(birthdays.split("/")[0])
		months.append(month_to_name[month])

	count = (Counter(months))
	print("Welcome to the birthday selector.  Birthdays of the following people are known: ")
	for x in birthday:
		print(x)
	print("The amount of birthdays per month so far is as follows: {} ".format(count))
	
	choice= input("Who's birthday do you want to look up?").title()		     #input handling
	while len(choice) - choice.count(' ') == 0:				     #blank input
		choice = input("Input must not be blank.  Pick again").title()	     #
	while len(choice) < 2:							     #invalid name length
		choice = input("Input too short.  Pick again: ").title() 	     #
	while not all(x.isalpha() or x.isspace() for x in choice):		     #non-letter input
		choice = input("Input must be a name.  Pick again: ").title()	     #
		
	if choice in birthday:
		print("The birthday of {} is {} ".format(choice, birthday[choice]))
	elif choice not in birthday:
		not_found = input("Name not found.  Add name to list? (y/n)").upper()
		if not_found == 'N':
			quit()
		elif not_found == 'Y':
			add_date = input("Enter birthdate in m/d/yyyy format: ")
			birthday[choice] = add_date
			correct_date = input(("{} was added to the birthday list with birthday of {}.  Is this correct? (y/n)".format(choice, add_date))).upper()
			while correct_date != 'Y':
				add_date = input("Enter correct birthdate in m/d/yyyy format: ")
				correct_date = input(("{} was added to the birthday list with birthday of {}.  Is this correct? (y/n)".format(choice, add_date))).upper()
			if correct_date == 'Y':
				with open("birthday_list.json", "w") as f:
					json.dump(birthday, f)    #writes good input to json file
	
	
	#graphing options
	x = []
	x_categories = []
	y = []
	
	output_file("month_freq.html")
	for key, value in count.items():
		x.append(key)    #frequency of birthdays per month
		y.append(value)    #name of month per birthday
	
	for key, value in month_to_name.items():
		x_categories.append(value)    #months categorical not numerical
	
	p = figure(x_range = x_categories, title = "Number of Birthdays by Month")
	p.vbar(x=x, top=y, width = 0.5)
	p.xaxis.axis_label = "Month"
	p.yaxis.axis_label = "Frequency"
	
	
	show_graph = input("Would you like to see a bar graph of cataloged birthdays? (y/n)").upper()
	while show_graph != 'Y' and show_graph != 'N':
		show_graph = input("You must pick y/n").upper()
	if show_graph == 'Y':
		show(p), restart()
	if show_graph == 'N':
		restart()

def restart():    #reinitialize option
	while True:
		answer = input("Would you like to enter a new name or exit? (enter/exit)").upper()
		while answer != "ENTER" and answer != "EXIT":
			answer = ipnut("You mist pick (enter/exit)").upper()
		if answer == "ENTER": True, main()
		elif answer == "EXIT": False, quit()
	
main()
