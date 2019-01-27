#imports for currency values
from money.money import Money
from money.currency import Currency

#defines the way that one inputs the currency value 'i.e. no period as it's valued in cents not dollars&cents
def USD(cents): 
	return Money.from_sub_units(cents, Currency.USD)

#Combines Names list with totals in the records.py file for output in console
def shifts(names, totals):
	return list(zip(names, totals))


#weekday & Saturday tip counting
def weekdays(tip1, tip2, tip3, tip4, tip5):
  
    open_one = USD(tip1) + USD(tip2) + USD(tip3)
    open_three = open_one + USD(tip4)
    ten_close = USD(tip2) + USD(tip3) + USD(tip4) + USD(tip5)
    noon_close = ten_close - USD(tip2)
    return (open_one, open_three, ten_close, noon_close)
    
#Sunday tip counting
def sunday(tip1, tip2, tip3):
	
	all_day = USD(tip1) + USD(tip2) + USD(tip3)
	open_one = USD(tip1) + USD(tip2)
	ten_close = all_day - USD(tip1)
	return (all_day, open_one, ten_close)

