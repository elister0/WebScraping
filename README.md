#  Cybersecurity Web Scraping Project (JJ's House)

A python program that scrapes JJ's House (a dress website) to find prom dresses that meet the user input criteria. The user may input a color, minimum price, and/or maximum price.
The scraped results are compiled into a .csv file for easy viewing.

There are no additional files/dependencies needed to run this program.

## Command Line Arguments
There are three optional arguments for this program: One that takes in a color, one that takes in a minimum price, and one that takes in a maximum price.

- -c OR --color = Specifies the color that the user is looking for. If color has a space in the name, a dash must be added between the words (ex. hunter green must be "hunter-green")
- -mi OR --minimum = Specifies the minimum price the user wants to look at. If not specified, defaults to th automatic minimum of $59.
- -ma OR --maximum = Specifies the maximum price the user wants to look at. If not specified, defaults to th automatic maximum of $269.

Examples:
- python3 Prom_Dress_Finder.py 
- python3 Prom_Dress_Finder.py  -c hunter-green -mi 100 -ma 200
- python3 Prom_Dress_Finder.py  --color lilac --maximum 250
- python3 Prom_Dress_Finder.py  -mi 160

## Limitations
- The image link stored in the csv file is not easily clickable to view the image. The user must copy and paste the image link, which could get tedious.
