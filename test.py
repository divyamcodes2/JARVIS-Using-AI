import requests
def tell_joke():
    try:
        url = "https://official-joke-api.appspot.com/random_joke"
        response = requests.get(url)
        joke_data = response.json()
        joke = f"{joke_data['setup']} ... {joke_data['punchline']}"
        print(joke)
    except Exception as e:
        print("Sorry, I couldn't fetch a joke right now.")
        print("Error:", e)

tell_joke()

# Note: Unfortunately, the Last.fm API does not provide a direct way to play the song.
# You may need to use a different API or service to play the song.