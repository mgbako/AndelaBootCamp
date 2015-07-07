import webbrowser 
import time

url = "http://www.google.com"

i = 0
while i < 3 :
	webbrowser.open(url)
	time.sleep(5)
	i += 1