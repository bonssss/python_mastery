import requests

from bs4 import BeautifulSoup

response = requests.get("https://www.century21.com/")
print(response)  # Print the status code of the response

soup = BeautifulSoup(response.text, "html.parser")
price =soup.find_all("div", class_="property_features")
# print(price)  # Print the prettified HTML content
for i in price:
    print(i.text)  # Print the text of each <h3> tag
    # print(price.index(i))  # Print the index of each <h3> tag