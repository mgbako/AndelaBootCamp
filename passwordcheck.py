def upper(word) :
	count = 0
	password = list(word)
	for item in password:
		if item.isupper():
			count += 1
	return count

def lower(password):
	count = 0
	password = list(password)
	for item in password :
		if item.islower() :
			count += 1
	return count

def number(password) :
	count = 0
	password = list(password)
	for char in password :
		if char.isdigit() :
			count += 1
	return count


def check(password) :
	correct = 0
	lowers = 0
	uppers = 0
	numbers = 0

	passwords = open(password, 'r')
	for valid in passwords :
		lowers = lower(valid)
		uppers = upper(valid)
		numbers = number(valid)

		if (lowers > 2) and (uppers > 4) and (numbers > 4) :
			correct += 1

	#print "%s has %d valid passwords." %(password, correct)
	return "The {0} has {1} correct passwords.".format(password, correct)

print check('C:/AndelaBootcamp/problems/password.txt')