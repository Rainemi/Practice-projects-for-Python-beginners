#import urllib
#use urllib.request to get data from the url
#write a function that takes a url
#return a response

import urllib.request as urllib

def check(url):
    print("Checking connectivity ")

    response = urllib.urlopen(url)
    print("Connected to " , url, "succesfully")
    print("The response code was: ", response.getcode())

input_url = input("Enter the url of the site you want to check : ")

check(input_url)
