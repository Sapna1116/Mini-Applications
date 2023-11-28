#pip install --user pyshorteners
import pyshorteners as ps

url = input("Enter the URL :\n")

print("New URL is : ", ps.Shortener().tinyurl.short(url))