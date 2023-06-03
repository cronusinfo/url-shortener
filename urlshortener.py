import pyshorteners
url = input("Enter your URL: ")
s = pyshorteners.Shortener().tinyurl.short(url)
print("Your shorted url is: ", s)