import webbrowser 
import time

url1 = "http://www.google.com"
url2 = "http://www.cnn.com"
url3 = "http://www.bbc.com"
url4 = "http://www.goal.com"

lists = [ [url1, 10], [url2, 20], [url3, 30], [url4, 1] ]

c = 0
for l in lists :
	webbrowser.open(l[0])
	time.sleep(l[1])