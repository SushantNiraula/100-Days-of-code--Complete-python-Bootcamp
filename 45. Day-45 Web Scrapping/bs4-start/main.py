from bs4 import BeautifulSoup

with open("website.html",encoding="utf-8") as file:
    contents = file.read()

soup=BeautifulSoup(contents, 'html.parser')

# print(soup)
print(soup.title)
print(soup.title.string)
# print(soup.prettify())
print(soup.a) ## finding the first anchor tag
print(soup.p) ## finding the first paragraph tag
all_anchor_tags= soup.find_all(name='a')
for tag in all_anchor_tags:
    print(tag.get_text()) ## getting the text of the tag
    print(tag.get('href')) ## getting the href of the tag
## using css selectors to find elements
print(soup.find(name='h1',id='name'))
print(soup.select_one(selector="p a"))
print(soup.select(selector='#name'))