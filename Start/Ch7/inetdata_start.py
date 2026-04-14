# LinkedIn Learning Python course by Joe Marini
# Example file for retrieving data from the internet
#
import urllib.request as ur

web_url = ur.urlopen("http://www.example.com")
print("Reuslt code:", web_url.getcode())
data = web_url.read()
print(data)