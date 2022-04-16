import webbrowser
import pyttsx3
import datetime
import speech_recognition as sr
import wikipedia
import gtts
import pyjokes
import os 



print("\nFew Examples of commands\n")
print("Open 'Youtube'")
print("Open 'Facebook'")
print("Shahrukh Khan Wikipedia")
print("Search'Spotify'")
print("Where is 'London'")
print("Tell me a joke")
print('Say "BYE" to Exit' )


engine = pyttsx3.init()
voices = engine.getProperty("voices")
voice = engine.setProperty("voice", voices[1].id)

def speak(audio):
    engine.say(audio)
    engine.runAndWait()

def timemdate():
    hour = int(datetime.datetime.now().hour)
    if hour >=5 and hour <12:
        speak("Good Morning!")
    elif hour >12 and hour <16:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")



def intake():
    
        r = sr.Recognizer()
        with sr.Microphone() as source:

            print("\nListening...")
            audio = r.listen(source)
            r.pause_threshold=0.5
            try:
                print("\nFetching best results..")
                query = r.recognize_google(audio, language="en-in")
                print("\nYou said:\n", query)
                speak("You said")
                speak(query)
                
                
            

            except Exception as e:
                print(e)
                print("Im Afraid I could not get that")
                speak("Im Afraid I coould not get that")
                print("Could you please repeat it again?")
                speak("Could you please repeat it again?")
                return "None"
            return query





timemdate()
speak("My name is Mr.Marson Junior.!")
speak("How can I help you?")

if __name__ == "__main__":
    
    while True:
        query = intake().lower()

        if "bye" in query:
            print("Thank you! I hope I was helpful :)")
            speak("Thank you! I hope I was helpful")
            exit()

        elif "wikipedia" in query:
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")
            webbrowser.open("https://www.google.com/search?q="+query+" ")
            results = wikipedia.summary(title = query, sentences=1)
            speak("Ok, here it goes! According to Wikipedia")
            print(results)
            speak(results)
        # elif "youtube" in query:
        #     webbrowser.open("youtube.com")
        #     speak("Here you go to Youtube! Enjoyy!")
        elif 'open' in query:
            query = query.replace("open ","")
            query = query.replace(" ","")
            webbrowser.open("https://"+query+".com"+"")
            speak("Cool! This is what I found!")
        elif 'search' in query:
            query = query.replace(" ", "")
            query = query.replace("search", "")
            webbrowser.open(query+" ")
            speak("Right away in a jiffy!!")
        elif 'joke' in query:
            query = pyjokes.get_joke()
            print(query)
            speak(query)
        elif "where is" in query:
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" +location+ "")
        elif "time" in query:
            currtime = datetime.datetime.now().strftime("%H:%M")
            speak("The time is:")
            speak(currtime)
        elif "your name" in query:
            print("My name is Mr.Marson junior.")
            speak("My name is Mr.Marson Junior.")
        elif "close google chrome" in query:
            os.system("taskkill /im chrome.exe /f")
            speak("Browser Closed!")
        elif "close browser" in query:
            os.system("taskkill /im msedge.exe /f")
            speak("Browser Closed!")
        
        else:
            speak("Sorry, your command is unavailable, you can try saying, Mr.Marson..open Gaana or search Bollywood Songs!")


