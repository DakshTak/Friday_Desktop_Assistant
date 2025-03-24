import pyttsx3
import speech_recognition as sr
import pyaudio
import datetime
import wikipedia
import webbrowser
import os

engine = pyttsx3.init('sapi5')
voices = engine.getProperty('voices')
#print(voices[0].id) #voices ke naam pata lagane ke liye
engine.setProperty('voice', voices[1].id)
recognizer=sr.Recognizer()

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        speak("Good Morning!")

    elif hour >= 12 and hour<18:
        speak("Good Afternoon")

    else:
        speak("Good Evening")

    speak("I am Friday Sir. Please tell me how may I help you")

def takeCommand():
    #It takes microphone command as input and returns string output

    r = sr.Recognizer() #Recognizer help to recognize audio
    with sr.Microphone() as mic:
        print("Listening...")
        r.pause_threshold = 0.9 # seconds of non-speaking audio before a phrase is considered complete
        r.energy_threshold = 900  # minimum audio energy to consider for recording
        audio = r.listen(mic)

    try:
        print("Recognizing...")  
        query = r.recognize_google(audio, language='en-IN')
        print(f"user said: {query}\n")


    except Exception as e:
        print("Pardon please. . .")
        return "None"    
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return "None"
    except sr.RequestError:
        print("Could not request results from Google Speech Recognition service")
        return "None"
    return query

    


if __name__ == "__main__":
    wishMe()
    
    while True:
        query = takeCommand().lower()

        #Logic for executing tasks based on query
        if 'wikipedia' in query:
            speak('Searching Wikipedia...')
            query = query.replace("wikipedia","")
            try:

                results = wikipedia.summary(query, sentences=1)
                speak("According to Wikipedia")
                print(results)
                speak(results)

            except wikipedia.exceptions.DisambiguationError as e:
                speak(f"There are several possible pages for {query}. Please be more specific.")
                print(f"Disambiguation Error: {e}")
            except wikipedia.exception.pageError:
                speak("Sorry, i couldnt find any information")
                print("No Matching Page found")
        

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'open chatgpt' in query:
            webbrowser.open("chatgpt.com")

        elif 'open google' in query:
            webbrowser.open("google.com")

        elif 'open youtube' in query:
            webbrowser.open("youtube.com")

        elif 'play music' in query: #import OS
            music_dir = 'E:\\DAKSH\\My space\\my songs'
            songs = os.listdir(music_dir)
            print(songs)
            os.startfile(os.path.join(music_dir, songs[0]))

        elif 'what is the time right now' in query:
            strTime = datetime.datetime.now().strftime("%H:%M:%S")
            speak(f"Sir the time is {strTime}")

        elif 'open vscode' in query:
            vscode ="C:\\Users\\hp\\AppData\\Local\\Programs\\Microsoft VS Code\\Code.exe" 
            os.stratfile(vscode)
        elif 'thank you friday' in query:
            speak(f"It's my pleasure")
            break
