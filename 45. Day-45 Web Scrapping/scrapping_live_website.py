from bs4 import BeautifulSoup
import requests
response=requests.get("https://news.ycombinator.com/news")
yc_webpage=response.text
soup=BeautifulSoup(yc_webpage,'html.parser')
articles=soup.find_all(name='span',class_='titleline')
article_upvotes=soup.find_all(name='span',class_='score')
# print(article_upvotes)
article_texts=[]
article_links=[]
for article in articles:
    title=article.find(name='a').getText()
    article_texts.append(title)
    link=article.find(name='a').get('href')
    article_links.append(link)
article_upvotes=[ score.getText() for score in article_upvotes]
final_upvotes=[] 
for i in article_upvotes:
    score,_=i.split()
    final_upvotes.append(int(score))
# print(article_texts[0:5],article_links[0:5],article_upvotes[0:5])
index_of_max=final_upvotes.index(max(final_upvotes))
print(f'{article_texts[index_of_max]} has {article_upvotes[index_of_max]} upvotes visit {article_links[index_of_max]} to view it.' )
