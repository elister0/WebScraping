# Importing classes; Beautiful Soup library for webscraping, urllib.request library
# for accessing urls, csv library for turning database into a spreadsheet
from bs4 import BeautifulSoup
import urllib.request
import csv
import re
import os
# Makes a request to access the url utilizing a user agent to prevent error 403
req = urllib.request.Request(
    "https://www.jjshouse.com/all/prom-dresses/color/dark-green?sort=new-arrivals",
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Opens the url and stores inspect items in f
f = urllib.request.urlopen(req)
# Creates a beautiful soup object for f
soup = BeautifulSoup(f, "html.parser")
# Finds the names of all the dresses on the page
dress_name = soup.findAll("h2", attrs={"class":"goods-name"})
price = soup.findAll("div", attrs={"class":"p_price"})
image = soup.findAll("a", attrs = {"class":"mt-common-click mt-common-exposure"})
# Prints the names

dresses = []
costs = []
images = []
for d in dress_name:
     dresses += [(d.text.strip())]

for c in price:
    costs += [c.text.strip()]

# Create a directory to save the images
for i in image:
    try:
        first=str(i).index("data-src=")+10
        last = str(i).index("orgin=")-2
        images += [str(i)[first:last]]

    except:
        print("no")
# Iterate over the image links and download the images


# Creates a new file called Prom Dresses to store the prom dress information
dress_file = open("Prom_Dresses.csv", "w")
# creates a writer to put the information in the spreadsheet based on file
writer = csv.writer(dress_file)
# Creates a header
writer.writerow(["Dress"])
# Goes through each dress name and puts it in the file
for n, p, i in zip(dresses, costs, images):
    writer.writerow([n, p, i])
dress_file.close()
