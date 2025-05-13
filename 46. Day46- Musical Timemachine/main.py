from bs4 import BeautifulSoup
import requests
import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope='user-library-read'

date_=input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")
print(date_)

header={
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.3",

}
response=requests.get(f'https://www.billboard.com/charts/hot-100/{date_}/',headers=header)
webpage=response.text
soup=BeautifulSoup(webpage,"html.parser")
songs=soup.select('li ul li h3')
song_names=[song.getText().strip() for song in songs]

print("Here are the top 100 songs from that date:")
# print(song_names)

sp=spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope,))