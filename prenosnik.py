"""
tutorial vzet od: https://www.youtube.com/watch?v=XQgXKtPSzUI&t=1519s
ostali resourci:
-https://stackoverflow.com/questions/2957013/beautifulsoup-just-get-inside-of-a-tag-no-matter-how-many-enclosing-tags-there
-https://stackoverflow.com/questions/1936466/beautifulsoup-grab-visible-webpage-text
-https://stackoverflow.com/questions/46718366/beautifulsoup-and-class-with-spaces
-https://stackoverflow.com/questions/46718366/beautifulsoup-and-class-with-spaces
-https://www.crummy.com/software/BeautifulSoup/bs4/doc/
-https://www.w3schools.com/python/python_comments.asp
-https://www.youtube.com/watch?v=lOIJIk_maO4
"""
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

import string

my_url = 'https://www.mimovrste.com/ultrabooki?o=price&b%5B%5D=asus'

# opening up connection, grabbing the page
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

# html parsing
page_soup = soup(page_html, "html.parser")

# grabs each product
containers = page_soup.findAll("article")

# shows hom many articles
len(containers)

container = containers[0]

filename = "products.csv"
f = open(filename, "w")

headers = "produkt; cena\n"

f.write(headers)

for container in containers:
    #brand = container.a["href"]
    #reference of a class with spaces in between can be refered as to one of the names seperated by the spaces
    title_container = container.findAll("a", {"class":"lay-block"})
    product_name = title_container[0].text #text prikazuje text med tags

    price_container = container.findAll("span", {"class":"lst-product-item-price-value"})
    price_real = price_container[0].text

    price = price_real.strip()
    price = price.translate({ord(c): None for c in string.whitespace})

    name = product_name.strip()
    name = name.translate({ord(c): None for c in string.whitespace})

    print("Ime produkta: " + name)
    print("Cena: " + price)

    f.write(name + ";" + price + "\n")

f.close()
