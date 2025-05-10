import subprocess
import speech_recognition as sr
import pyttsx3
import webbrowser
import os
import datetime
from together import Together
from config import api_key

chatStr = ""


def chat(query):

    # The function accesses a global variable chatStr, which is likely a string that stores the conversation history.
    global chatStr

    client = Together(
        # This line creates an instance of the Together class, which is a client for the Together API.
        api_key=api_key)

    # The function appends the user's input (query) to the conversation history (chatStr) with a prefix "Divyam: " and a suffix " \n Jarvis".
    chatStr += f"Divyam: {query} \n Jarvis"

    # This line sends a request to the Together API to generate a completion for the given prompt.
    response = client.chat.completions.create(

        # The name of the model to use for generating the completion.
        model="Qwen/Qwen3-235B-A22B-fp8-tput",
        messages=[
            {"role": "user", "content": chatStr}]
    )

    # The function prints the content of the first choice in the response from the API using the say function
    say(response.choices[0].message.content)

    # The function appends the response content to the conversation history (chatStr).
    chatStr += response.choices[0].message.content

    # The function returns the response content.
    return response.choices[0].message.content


def ai(prompt):
    try:
        client = Together(
            # This line creates an instance of the Together class, which is a client for the Together API.
            api_key=api_key)

        # This line creates a string variable text that contains a message indicating that the response is from an AI. The message includes the original prompt. The f before the string indicates that it's a formatted string literal (f-string), which allows you to embed expressions inside the string.
        text = f"AI response for prompt: {prompt} \n ****************** \n\n"

        # This line sends a request to the Together API to generate a completion for the given prompt.
        response = client.chat.completions.create(

            # The name of the model to use for generating the completion.
            model="Qwen/Qwen3-235B-A22B-fp8-tput",
            messages=[
                {"role": "user", "content": prompt}]
        )

        # This line prints the content of the first choice in the response from the API.
        print(response.choices[0].message.content)

        # This line appends the content of the completion to the text variable.
        text += response.choices[0].message.content

        # This line checks if a directory named "Answer" exists. If it doesn't exist, the os.mkdir function is called to create the directory.
        if not os.path.exists("Answer"):
            os.mkdir("Answer")

        # This line opens a file in the "Answer" directory with a name that includes the first 30 characters of the prompt. The file is opened in write mode ("w"). # UTF-8 is a variable-length character encoding standard that supports all Unicode characters and is widely used as a default encoding.
        with open(f"Answer/prompt- {prompt[0:30]}.txt", "w", encoding="utf-8") as f:

            # This line writes the contents of the text variable to the file.
            f.write(text)

    except Exception as e:
        print("Some error occured", e)


def say(text):
    # pyttsx3 is a Python library for text-to-speech (TTS) conversion. * init() is a method that initializes the TTS engine. * The engine variable now holds an instance of the TTS engine.
    engine = pyttsx3.init()

    # say() is a method of the TTS engine that takes a string (text) as input. * The text parameter is the text that you want the engine to speak. * The say() method adds the text to the engine's speech queue.
    engine.say(text)

    # runAndWait() is a method that starts the speech synthesis process. * The engine will speak the text that was added to the queue using say(). * The runAndWait() method blocks until the speech synthesis is complete, meaning that the program will wait until the text has been spoken before continuing.
    engine.runAndWait()


def takeCommand():
    # sr is the speech_recognition library. * Recognizer is a class within the speech_recognition library that provides speech recognition capabilities. * r is an instance of the Recognizer class, which will be used to recognize speech.
    r = sr.Recognizer()

    # sr.Microphone() creates a new instance of the Microphone class, which represents the computer's microphone. * The with statement is used to create a context manager for the microphone, which ensures that the microphone is properly closed when we're done with it. * source is the variable that represents the microphone.
    with sr.Microphone() as source:

        # pause_threshold is an attribute of the Recognizer class that determines how long the recognizer should wait before considering the speech input complete. * In this case, we're setting the pause_threshold to 1 second, which means that the recognizer will wait for 1 second of silence before considering the speech input complete.
        r.pause_threshold = 1

        # listen() is a method of the Recognizer class that listens to the microphone and returns an AudioData object containing the recorded audio. * source is the microphone instance that we created earlier. * audio is the variable that holds the recorded audio.
        audio = r.listen(source)
        try:

            # recognize_google() is a method of the Recognizer class that sends the recorded audio to the Google Speech Recognition API and returns the recognized text. * audio is the recorded audio that we obtained earlier. * language="en-in" specifies the language and dialect of the speech input (in this case, English as spoken in India). * query is the variable that holds the recognized text.
            query = r.recognize_google(audio, language="en-in")

            # This line prints the recognized text to the console, along with a message indicating that the user spoke the text.
            print(f"User said: {query}\n")

            # This line returns the recognized text from the function.
            return query

        # This line catches any exceptions that might occur during the execution of the code within the try block. * Exception is the base class for all exceptions in Python. * e is the variable that holds the exception object.
        except Exception as e:
            return "Some error occured"


if __name__ == "__main__":
    say("I am jarvis AI")
    while True:
        print("Listening...")
        query = takeCommand()
        # A list of lists in Python is a data structure where a list contains other lists as its elements. It's a way to represent a collection of collections.
        sites = [["youtube", "https://www.youtube.com/"], ["google",
                                                           "https://www.google.com/"], ["wikipedia", "https://www.wikipedia.com/"]]

        for site in sites:

            # So, if the query contains the phrase "open youtube" (in any case), this condition will be True.
            if f"open {site[0]}".lower() in query.lower():
                # This line says f"Opening {name of the website}"
                say(f"Opening {site[0]}")

                # To access the URL, you need to use the index 1, because the URL is the second element in the inner list
                webbrowser.open(site[1])

            # Check if the user's query contains the phrase "Play Music" (case-insensitive)
            if "Play Music".lower() in query.lower():

                # When you prefix a string with r, Python treats the string as a raw string, which means it doesn't interpret any special characters or escape sequences in the string. This is useful when working with file paths
                musicPath = r"C:\Users\jdivy\Downloads\warriyo.mp3"
                os.startfile(musicPath)

            # We use the .lower() function in this line of code to ensure that the comparison between the phrase "Tell the time" and the user's query is case-insensitive.
            if "Tell the time".lower() in query.lower():
                strTime = datetime.datetime.now().strftime("%H:%M")
                say(f"The time is {strTime}")
                break  # This break will make it tell the time for once

            if "Open VS code".lower() in query.lower():
                codePath = r"C:\Users\jdivy\AppData\Local\Programs\Microsoft VS Code\Code.exe"
                say("Name the file you want to create")
                filename = input("Enter the name of the file: ")

                # Open Visual Studio Code with a specific file
                # subprocess.run() is used to run the Code.exe executable with the file as an argument
                # codePath is the path to the Code.exe executable
                # filename is the name of the file to be opened
                subprocess.run([codePath, filename])
                break

            if "Using artificial intelligence".lower() in query.lower():
                # Extract the prompt from the user query
                prompt = query.replace(
                    "Using artificial intelligence", "").strip()
                ai(prompt=prompt)
                break

            if "i want to exit".lower() in query.lower():
                say("Goodbye")
                exit()
                break

            else:
                print("Chatting...")
                chat(query)

# say(query)
