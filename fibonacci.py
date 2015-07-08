def fibonacci(n=None):
	if type(n) == float:
		return -1
	if type(n) != int:
		return -1
	if n < 0 :
		return -1
	if n is None:
		return -1
	if type(n) != list:
		return -1

	i = 1
	j = 1

	for f in range(n-1):
		i = j
		j = i + j
	return i

num = list()
fibonacci()