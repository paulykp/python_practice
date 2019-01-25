
#weekday & Saturday tip counting
def tc(tip1, tip2, tip3, tip4, tip5):
  
  open_1 = tip1 + tip2 + tip3
  open_3 = open_1 + tip4
  10_close = tip2 + tip3 + tip4 + tip5
  12_close = 10_close - tip2

  print(open_1, open_3, 10_close, 12_close)

#Sunday tip counting
def sunday(tip1, tip2, tip3):
	
	all_day = tip1 + tip2 + tip3
	open_1 = tip1 + tip2
	10_close = all_day - tip1
	print(open_1, all_day, 10_close)

#hi tobin

