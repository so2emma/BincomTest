from bs4 import BeautifulSoup
import numpy
import pandas
import lxml
import re

DAYS_OF_THE_WEEK = ["MONDAY", "TUESDAY", "WEDNESDAY", "THURSDAY", "FRIDAY"]
ALL_COLORS = []
dict_of_colors = {}

with open("index.html", "r") as HtmlFile:
    content = HtmlFile.read()

soup = BeautifulSoup(content, 'lxml')
table = soup.find("table")

for i in table.find_all("td"):
    title = i.text.strip("\n")
    if title not in DAYS_OF_THE_WEEK:
        ALL_COLORS.append(title + ", ")

colors_string = "".join(ALL_COLORS)
colors = colors_string.split(", ")

# green = re.findall("GREEN", colors)
# yellow = re.findall("YELLOW", colors)
# brown = re.findall("BROWN", colors)
# blue = re.findall("BLUE", colors)
# pink = re.findall("PINK", colors)
# cream = re.findall("CREAM", colors)
# orange = re.findall("ORANGE", colors)
# red = re.findall("RED", colors)
# white = re.findall("WHITE", colors)
# arsh = re.findall("ARSH", colors)
# print(arsh)
# print(colors)

mean_color = numpy.mean(colors)

position = 0
different_colors = []

for i in colors:
    choice = colors[0]
    if choice in different_colors:
        dict_of_colors[f"{choice}"] += 1
    else:
        dict_of_colors[f"{choice}"] = 1
        different_colors.append(choice)
    colors.remove(choice)

print(colors)
print(len(colors))
print(dict_of_colors)
