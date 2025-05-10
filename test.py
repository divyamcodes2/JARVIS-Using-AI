# from together import Together


# def ai(prompt):


# # auth defaults to os.environ.get("TOGETHER_API_KEY")
#     client = Together(
#         api_key="9de8a07254aa3162a37a46f2b91e9673d0ef0c4bb82ad7851975db0c9b14106a")

#     response = client.chat.completions.create(
#         model="Qwen/Qwen3-235B-A22B-fp8-tput",
#         messages=[
#             {"role": "user", "content": prompt}]
#     )
#     print(response.choices[0].message.content)

import spotipy
from spotipy.oauth2 import SpotifyOAuth

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="39945aa3896c4fa28501e37705e4179a",
                                               client_secret="5d68f7ed8cfb4c9cb6f0fce9a342c3ee",
                                               redirect_uri='http://localhost:8888/callback',
                                               scope='user-read-playback-state,user-modify-playback-state'))


# Search for a song
def search_song(song_name):
    results = sp.search(q=song_name, type='track')
    return results

# Play a song


def play_song(track_uri):
    sp.start_playback(uris=[track_uri])

# Main function


def main():
    song_name = input("Enter a song name: ")
    results = search_song(song_name)
    if results['tracks']['total'] > 0:
        track_uri = results['tracks']['items'][0]['uri']
        play_song(track_uri)
        print(f"Now playing: {song_name}")
    else:
        print(f"Song not found: {song_name}")


if __name__ == '__main__':
    main()
