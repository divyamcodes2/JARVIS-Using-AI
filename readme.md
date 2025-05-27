# 🤖 JARVIS - Your Personal Desktop Assistant 🧠💻

Welcome to **JARVIS**, a powerful voice-activated desktop assistant built with Python!  
It’s smart, speaks to you, listens to your commands, and even interacts with AI APIs 🤯  
Perfect for automating everyday desktop tasks with just your voice! 🎤🎧

---

## 🚀 Features

✨ **Voice Control** – Issue commands naturally using your voice  
🌐 **Open Websites** – Launch YouTube, Google, Wikipedia, and more with ease  
🎵 **Play Music** – Fire up your favorite songs in seconds  
🕒 **Tell Time** – Ask for the current time and get a spoken response  
📝 **Open VS Code** – Quickly launch and create files in Visual Studio Code  
🧠 **AI Integration** – Use Together API to get smart responses to your prompts  
🛑 **Exit Command** – End your session with a simple phrase  
🗣️ **Text to Speech** – JARVIS talks back using `pyttsx3`  
🎙️ **Speech Recognition** – Powered by `speech_recognition`

---

## 🧠 Functions Explained

### 🔊 `say(text)`

Converts the given text into speech using `pyttsx3`.

### 🧏‍♂️ `takeCommand()`

Listens to the user's voice and returns the recognized text using `speech_recognition`.

### 🧠 `ai(prompt)`

Uses the **Together API** to generate intelligent responses for a given prompt.

- Saves response in `Answer/` folder
- API model used: `Qwen/Qwen3-235B-A22B-fp8-tput`

### 🧪 `__main__` Logic

A loop that:

- Speaks "I am jarvis AI"
- Waits for your voice command
- Performs the following actions:

#### 🌍 Open Websites

Opens:

- YouTube
- Google
- Wikipedia  
  ➡️ Trigger phrases: “open youtube”, “open google”, “open wikipedia”

#### 🎵 Play Music

Plays a local MP3 file  
➡️ Trigger phrase: “play music”

#### 🕓 Tell the Time

Speaks current time  
➡️ Trigger phrase: “tell the time”

#### 🧑‍💻 Open VS Code

Launches VS Code and asks for a file name to open/create  
➡️ Trigger phrase: “open vs code”

#### 🤖 AI Responses

Uses the Together AI model to respond to your custom prompts  
➡️ Trigger phrase: “using artificial intelligence [your prompt]”

#### ❌ Exit

Ends the assistant session  
➡️ Trigger phrase: “I want to exit”

#### 🃏It can crack jokes

Uses the official joke by google api to fetch jokes 
➡️ Trigger phrase: “Tell me a joke”
---

## 📁 Project Structure

📁 Jarvis/
├── main.py # Main logic
├── config.py # Contains your Together API key
├── Answer/ # Stores AI-generated responses
└── README.md # This file!

# 🙌 Credits
Developed with ❤️ by Me

Uses:

🔗 Together AI

🔈 pyttsx3

🎤 speech_recognition

🌍 webbrowser, os, datetime, subprocess

# 🧠 Final Thoughts


JARVIS is not just a script, it’s a talking assistant for your daily tasks!
Try saying: “Open Google”, “Play music”, or “Using artificial intelligence write a poem” – and see the magic 🪄

Happy Automating! 🤖✨
