# library used to break down HTML information into easily traversable objects
from bs4 import BeautifulSoup
# library used to access URLs from the internet
import urllib.request
# library used to put dress information into a file
import csv
# library to run code from the command line with arguments
import argparse

# Accessing different arguments from the command line, -c or --color relates to color of the dress,
# -mi or --min relates to the minimum cost a person wants their dress to be
# -ma or --max relates to the maximum cost a person wants their dress to be
parser = argparse.ArgumentParser()
parser.add_argument('-c', '--color', type = str, default = False)
parser.add_argument('-mi', '--min', type = int, default = False)
parser.add_argument('-ma', '--max', type = int, default = False)
args = parser.parse_args()

# stores the correct input into a variable (if inputted into arguments)
color = args.color
minimum = args.min
maximum = args.max

# the base URL that will be built off of or defaulted to if no arguments are given
base_url = "https://www.jjshouse.com/all/prom-dresses?sort=new-arrivals"

# if a color is inputted, adds the color into the correct place in the url so that the dresses
# will be filtered by their color
if color:
    base_url = base_url[0:42] + "/color/" + color +"?"+ base_url[42:]

# checks if a minimum is inputted (without a max), and will add the inputted minimum value and default maximum value
# of 269.
# if a maximum is inputted (without a min), it will add default minimum value of 59 and the maximum inputted
# Adds the minimum and maximum info (if min and/or max is inputted; else doesn't change) to the URL to filter by cost
if (minimum and not maximum):
    base_url = base_url + "&price=" + str(minimum) + "-269"
elif(minimum and maximum):
    base_url = base_url + "&price=" + str(minimum) + "-" + str(maximum)
elif(maximum):
    base_url = base_url + "&price=59-" + str(maximum)

# prints the url being used
print(base_url)

# Accesses the modified URL to filter the dresses utilizing a user agent to avoid Forbidden 404 Error
req = urllib.request.Request(
    base_url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)

# Stores the open requested file into variable f
f = urllib.request.urlopen(req)

# Opens a beautiful soup object utilizing the f variable and the type of parser (html)
soup = BeautifulSoup(f, "html.parser")

# Stores all dress names, prices, and images found on the page in HTML
dress_name = soup.findAll("h2", attrs={"class":"goods-name"})
price = soup.findAll("div", attrs={"class":"p_price"})
image = soup.findAll("a", attrs = {"class":"mt-common-click mt-common-exposure"})

# Creates list to hold the plain text of dresses, costs, and images
dresses = []
costs = []
images = []

# variable to throw exceptions
count = 0

# Goes through the dress names stored in HTML and stores the plain text of the name into the dresses list
for d in dress_name:
     dresses += [(d.text.strip())]

# Goes through the costs stored in HTML and stores the plain text of the price into the costs list
for c in price:
    costs += [c.text.strip()]

# Goes through the images stored in HTML and stores the plain text of the image link into the costs list
# tries to find the index of the HTML that says "data-src" which stored the jpeg image
# If the index is not found, throws an error so the code doesn't break
for i in image:
    try:
        first=str(i).index("data-src=")+10
        last = str(i).index("orgin=")-2
        images += [str(i)[first:last]]

    except:
        count+= 1


# opens the csv file that stores all the information about the dress
dress_file = open("Prom_Dresses.csv", "w")

# creates a csv writer to write in the file
writer = csv.writer(dress_file)

# writes a header so the reader of the file easily knows what they're looking at
writer.writerow(["Dress, Cost, Image"])

# Accesses each element in all three lists storing the dress name, price, and image link and puts it in the csv file
for n, p, i in zip(dresses, costs, images):
    writer.writerow([n, p, i])

# Closes the file to be read
dress_file.close()
