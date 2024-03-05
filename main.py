from bs4 import BeautifulSoup
import urllib.request
import csv
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('-c', '--color', type = str, default = False)
parser.add_argument('-mi', '--min', type = int, default = False)
parser.add_argument('-ma', '--max', type = int, default = False)
args = parser.parse_args()

color = args.color
minimum = args.min
maximum = args.max

base_url = "https://www.jjshouse.com/all/prom-dresses?sort=new-arrivals"

if color:
    base_url = base_url[0:42] + "/color/" + color +"?"+ base_url[42:]

if (minimum and not maximum):
    base_url = base_url + "&price=" + str(minimum) + "-269"
elif(minimum and maximum):
    base_url = base_url + "&price=" + str(minimum) + "-" + str(maximum)
elif(maximum):
    base_url = base_url + "&price=59-" + str(maximum)

print(base_url)
req = urllib.request.Request(
    base_url,
    data=None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
)


f = urllib.request.urlopen(req)

soup = BeautifulSoup(f, "html.parser")

dress_name = soup.findAll("h2", attrs={"class":"goods-name"})
price = soup.findAll("div", attrs={"class":"p_price"})
image = soup.findAll("a", attrs = {"class":"mt-common-click mt-common-exposure"})


dresses = []
costs = []
images = []
count = 0
for d in dress_name:
     dresses += [(d.text.strip())]

for c in price:
    costs += [c.text.strip()]

for i in image:
    try:
        first=str(i).index("data-src=")+10
        last = str(i).index("orgin=")-2
        images += [str(i)[first:last]]

    except:
        count+= 1


dress_file = open("Prom_Dresses.csv", "w")

writer = csv.writer(dress_file)

writer.writerow(["Dress, Cost, Image"])

for n, p, i in zip(dresses, costs, images):
    writer.writerow([n, p, i])
dress_file.close()
