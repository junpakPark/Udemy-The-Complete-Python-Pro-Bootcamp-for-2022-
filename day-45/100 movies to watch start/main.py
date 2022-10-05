from operator import mod
import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇
res = requests.get(URL)
res.raise_for_status()
contents = res.text

soup = BeautifulSoup(contents, 'html.parser')

all_movies = soup.find_all(name="h3", class_="title")
# movies = []
# for title in titles:
#     movies.append(title.getText())
movies = [movie.getText() for movie in all_movies]

with open("movies.txt", mode="w") as txt:
    for movie in movies[::-1]:
        txt.write(f"{movie}\n")
