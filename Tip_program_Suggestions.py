
#weekday & Saturday tip counting
def tc(shift_1, shift_2, shift_3, shift_4, shift_5):

    # Commenting code is a good skill to cultivate now
    # even if it seems self explanitory, it's good to comment the logic behind the code.
    #   esp. when the code is not obvious
    
    open_1 = shift_1 + shift_2 + shift_3
    
    open_3 = open_1 + shift_4
    
    ten_close = shift_2 + shift_3 + shift_4 + shift_5
    
    twelve_close = ten_close - shift_2
    
    print( " Shift 1 : %.2f \n Shift 2 : %.2f \n Shift 3 : %.2f \n Shift 4 : %.2f \n \n" 
        % (open_1, open_3, ten_close, twelve_close))    


#Sunday tip counting
def sunday(shift_1, shift_2, shift_3) :
	
	all_day = shift_1 + shift_2 + shift_3
	open_1 = shift_1 + shift_2
	10_close = all_day - shift_1

	print(open_1, all_day, 10_close)

