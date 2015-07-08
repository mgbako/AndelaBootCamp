import re

password = open('C:/AndelaBootcamp/problems/password.txt', 'r')
rl = password.readlines()
# pattern = "(?=.*\d)(?=.*[a-z])(?=.*[A-Z])(?=.[\W]).{6,20}"
# 
pattern = "(?=.*\d){4}(?=.*[a-z]){2}(?=.*[A-Z]){4}.{4}"
j = 0
for i in rl :
	if re.match(pattern, i):
		j += 1

print "We have only %d valide passwords." %(j)