from bs4 import BeautifulSoup
import requests

url='https://www.empireonline.com/movies/features/best-movies-2/'
response=requests.get(url)
webpage=response.text
soup=BeautifulSoup(webpage,'html.parser')
# print(soup.prettify())
titles=soup.select('h2 strong')
top100_movies=[]
for title in titles:
    actual=title.get_text()
    top100_movies.append(actual)
## reverse the list from 1 to 100
top100_movies.reverse()
with open('movies.txt','w') as file:
    for movie in top100_movies:
        file.write(f"{movie}\n")
print("Top 100 movies have been written to movies.txt")
