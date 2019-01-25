
#weekday & Saturday tip counting
def tc(tip1, tip2, tip3, tip4, tip5):
  
    open_one = tip1 + tip2 + tip3
    open_three = open_one + tip4
    ten_close = tip2 + tip3 + tip4 + tip5
    noon_close = ten_close - tip2
    print(" Shift 1 : %.2f \n Shift 2 : %.2f \n Shift 3 : %.2f \n Shift 4 : %.2f \n \n" % (open_one, open_three, ten_close, noon_close))

#Sunday tip counting
def sunday(tip1, tip2, tip3):
	
	all_day = tip1 + tip2 + tip3
	open_one = tip1 + tip2
	ten_close = all_day - tip1
	print(" Shift 1 : %.2f \n Shift 2 : %.2f \n Shift 3 : %.2f \n \n" % (open_one, all_day, ten_close))

#hi tobin

