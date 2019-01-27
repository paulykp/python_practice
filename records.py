#imports the "pretty print" ----- DO THIS ALL THE TIME lol
from pprint import pprint

#imports from other .py files to get function information and list of employee names
from tip_counting_new import *
from people import *


# Archived list for pay period 1.20.2019 - 1.26.2019
week_1_20_2019 = {
	'1/20': shifts(
		(mikayla, rica, atticus),
		sunday(1108, 2321, 3310)),
	'1/21': shifts(
		(michael, mikayla, rica, tobin),
		weekdays(1159, 629, 385, 2019, 1832)),
	'1/22': shifts(
		(michael, tobin, mikayla, atticus),
		weekdays(3233, 994, 0, 1393, 2009)),
	'1/23': shifts(
		(tobin, michael, thea, atticus),
		weekdays(2544, 1105, 873, 1034, 1454)),
	'1/24': shifts(
		(rica, atticus, michael, tobin),
		weekdays(2719, 918, 0, 1252, 1965)),
	'1/25': shifts(
		(thea, tobin, rica, michael),
		weekdays(2548, 1136, 457, 924, 1626)),
	'1/26': shifts(
		(tamara, rica, mikayla, atticus),
		weekdays(1409, 1013, 527, 1567, 1638)),
}

# Archived list for pay period 1.27.2019 - 2.2.2019
week_1_27_2019 = {
	'1/27': shifts(
		()
		sunday()),
	'1/28': shifts(
		()
		weekdays()),
	'1/29': shifts(
		()
		weekdays()),
	'1/30': shifts(
		()
		weekdays()),
	'1/31': shifts(
		()
		weekdays()),
	'2/1': shifts(
		()
		weekdays()),
	'2/2': shifts(
		()
		weekdays()),
}

def main():
	pprint(week_1_20_2019)

if __name__ == '__main__':
	main()








