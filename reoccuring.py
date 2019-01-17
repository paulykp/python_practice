# my solution to reoccuring letters problem





def find_sames( theList ) : 
	
	letters = {}


	for item in theList :
		if item in letters : 
			letters[item] += 1
		else : 
			letters[item] = 1

# // for when you are looking for multiple reoccurances
#	for key in letters : 
#		if letters[key] > 1 : 
#			print(key)


# // for when you are looking for char that reoccurs the most
	first_place = list(letters.keys())[0]

	for key in letters :
		if letters[key] > letters[first_place] :
			first_place = key

	print(first_place)





list_1 = ['A', 'B', 'C', 'A', 'B', 'B', 'B', 'C']

print(' '.join(list_1))

find_sames(list_1)