import speech_recognition as sr
import pyttsx3
import datetime
import time

engine = pyttsx3.init('sapi5')
engine.setProperty('rate', 170)

def speak(text):
    print("Assistant:", text)
    engine.say(text)
    engine.runAndWait()
    time.sleep(0.5)   # IMPORTANT pause

def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        r.adjust_for_ambient_noise(source, duration=1)
        audio = r.listen(source, timeout=5, phrase_time_limit=5)

    try:
        print("Recognizing...")
        command = r.recognize_google(audio)
        print("You said:", command)
        return command.lower().strip()
    except:
        return ""

# ---- MAIN LOOP (ONLY ONE LOOP) ----
speak("Good evening")

while True:
    query = take_command()

    if query == "":
        continue

    print("Final query:", query)

    if "good evening" in query:
        speak("Good evening! How can I help you?")

    elif "hello" in query:
        speak("Hello! How can I help you?")

    elif "time" in query:
        speak(datetime.datetime.now().strftime("The time is %H:%M"))

    elif "help" in query:
        speak("I can tell time, date, and exit the program")

    elif "exit" in query or "quit" in query:
        speak("Goodbye")
        break

    else:
        speak("Sorry, I did not understand that")
