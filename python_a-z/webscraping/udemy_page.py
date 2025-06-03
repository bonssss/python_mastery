import requests
from bs4 import BeautifulSoup

response= requests.get("http://books.toscrape.com")
response.encoding = "utf-8"  # Set proper encoding
print(response)  # Print the status code of the response

soup = BeautifulSoup(response.text, "html.parser")

# print(soup.prettify)

# val1= soup.find_all("ul" ,class_="nav nav-list")
# for i in val1:
#     print(i.text)  # Print the text of each <h3> tag
#     # print(val1.index(i))  # Print the index of each <h3> tag
# # print(val1[0])  # Print all <h3> tags

val2 =soup.find_all("h3")
val3=soup.find_all("p", class_="price_color")


for i in val2:
    print(i.text)  # Print the text of each <h3> tag
    # print(val2.index(i))  # Print the index of each <h3> tag
for i in val3:
    print(i.text)  # Print the text of each <h3> tag
    # print(val3.index(i))  # Print the index of each <h3> tag