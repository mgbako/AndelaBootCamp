import webbrowser 
import time

url1 = "http://www.google.com"
url2 = "http://www.cnn.com"
url3 = "http://www.bbc.com"

lists = [ [url1, 10], [url2, 20], [url3, 30] ]

for l in lists :
	for t in l :
		webbrowser.open()
		time.sleep()