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


filename = "imena.csv"
f = open(filename, "w")

headers = "ime; id\n"

f.write(headers)


i = 1921000
while i <= 1923000:
    id = str(i)
    print(i, "/1925900")
    my_url = 'https://www.mondialtravel.si/wp-content/themes/collegium-si/G-TA3/index.php?id='
    my_url = my_url + id
    uClient = uReq(my_url)
    page_html = uClient.read()
    uClient.close()
    page_soup = soup(page_html, "html.parser")
    containers = page_soup.findAll("div", {"class": "nme"})
    i += 1
    dol = (len(containers))
    print(dol)
    if dol == 0: continue
    else:
        container = containers[0]
        ime = container.text
        container = containers[1]
        id = container.text
        f.write(ime + ";" + id + "\n")

f.close()


print("KONEC")