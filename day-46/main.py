import requests
from bs4 import BeautifulSoup
import spotipy
from spotipy.oauth2 import SpotifyOAuth

# Scraping Billboard 100
date = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD?: ")

res = requests.get(f"https://www.billboard.com/charts/hot-100/{date}")
res.raise_for_status()
contents = res.text

soup = BeautifulSoup(contents, "html.parser")

songs = [song.getText().strip() for song in soup.select(".o-chart-results-list-row-container h3.a-no-trucate")]
artists = [artist.getText().strip() for artist in soup.select(".o-chart-results-list-row-container span.a-no-trucate")]


# Spotify Authentication
sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="http://example.com",
        client_id="16e9c599266c4f9fbd28abe3d117047d",
        client_secret="b566d3ea55794744ab335a058cb13c52",
        show_dialog=True,
        cache_path="token.txt",
    )
)

user_id = sp.current_user()["id"]


# Searching Spotify for songs by title
song_uris = []
year = date.split("-")[0]

for song in songs:
    results = sp.search(q=f"track: {song} year: {year}")
    # print(f"{results['tracks']['items']}\n")
    try:
        uri = results["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


# Creating a new private playlist in Spotify
playlist = sp.user_playlist_create(user=user_id, name=f"{date} Billboard 100", public=False)
print(playlist)

# Adding songs found into the new playlist
sp.playlist_add_items(playlist_id=playlist["id"], items=song_uris)
