from tkinter import Place
import webbrowser  #This module helps in opening the web browsers
import pyttsx3  #This module helps the computer to speak
import datetime #To fetch the current time
import speech_recognition as sr #Helps to recognize the speech of the user as sr so instead of writing speech_recognition, can simply write sr
import wikipedia #Gives access to Wikipedia
import pyjokes #Gives access to jokes
import os #Gives access to perform tasks of local machine
import time #Helps in timer


 
print("\nFew Examples...\n")  
print("Open 'Youtube'")
print("Open 'Facebook'")
print("Shahrukh Khan Wikipedia")
print("Search'Spotify'")
print("Where is 'London'")
print("Tell me a joke")
print('Say "BYE" to Exit' )


engine = pyttsx3.init()  #Initializing the pyttsx3 so the machine can speak the commands
voices = engine.getProperty("voices") #Listing the male/female voice to set as default and store it in "voices"
voice = engine.setProperty("voice", voices[1].id)  #The voice is set is 1. (0 for male and 1 for female)

def speak(audio): #passing an argument to let the machine speak
    """This function helps in letting the machine say"""
    engine.say(audio)  #This is the syntax which let the machine speaks what ever is written inside the braces.
    engine.runAndWait() #The engine will first run and wait until the user finishes the query and returns the value


def timemdate():  
    """This function is to greet the user according to the time"""
    hour = int(datetime.datetime.now().hour)  #syntax for time and adding '.hour' at the end to that instead of full time string, the computer can easily decides from the hour also typecast in 'int' for conditional operators.
    if hour >=5 and hour <12:
        speak("Good Morning!")
    elif hour >12 and hour <16:
        speak("Good Afternoon!")
    else:
        speak("Good evening!")



def intake():
        """This function is to receive the command from the user"""   
    
        r = sr.Recognizer()  #It is a class which helps in recognize the voice of the user
        with sr.Microphone() as source: #The audio input of the user is taken from Microphone as naming as source

            print("\nListening...")
            audio = r.listen(source)    #syntax to listen to source taken from microphone and store it in 'audio'
            r.pause_threshold=0.5  #The machine will wait for 0.5 sec after the user query phrase to return the value.
            try:  #We are asking the machine ti try these, because even after the machine throws an error, the code must not stop
                print("\nFetching best results..")
                query = r.recognize_google(audio, language="en-in")  #The user queries are recognized by google engine of english language indian accent
                print("\nYou said:\n", query.capitalize())
                speak("You said")
                speak(query)   #The machine will speak what ever the query is given from the user
                if "bye" in query:
                    print("Thank you! I hope I was helpful :)")
                    speak("Thank you! I hope I was helpful")
                    exit()  #If user tells "bye" the program will exit
            except Exception as e:  #If by any chance, the machine is unable to give output of the above 'try:' statements, The below 'exception' commands will be executed
                # print(e)
                print("Im Afraid I could not get that")
                speak("Im Afraid I coould not get that")
                print("Could you please repeat it again?")
                speak("Could you please repeat it again?")
                speak("You can try saying, open Gaana or search Bollywood Songs!")
                query = intake().lower()  #The query will be taken in lower case
                return query  #It returns the value of the query 
            return query  #This also returns the value of the query

timemdate()  #We are calling the timedate function, to greet the user according to the time
speak("My name is Mr.Marson Junior.!")
speak("How can I help you?")
if __name__ == "__main__":   #main function
    while True:  #The below statements will be looping if the queries are found in the below statements
        query = intake().lower()

        if "no thanks" in query:  #The programe will exit when the user says "no thanks"
            print("Thank you! I hope I was helpful :)")
            speak("Thank you! I hope I was helpful")
            exit()

        elif "wikipedia" in query:  #If the machine sense wikipedia in the user's query, the following will be executed
            speak("searching wikipedia...")
            query = query.replace("wikipedia", "")  #Eg.use says, Tom Cruise wikipedia  , This line will replace 'wikipedia' to blank. After replacing it will look as Tom Cruise 
            webbrowser.open("https://www.google.com/search?q="+query+" ")  #It will open the browser and search for https://www.google.com/search?q=tom cruise 
            results = wikipedia.summary(title = query, sentences=1)  #We are instructing the machihne to read the 1 sentence from wiki of the query
            speak("Ok, here it goes! According to Wikipedia")
            print(results)  #It will print the wiki statements
            speak(results)
            time.sleep(6)  #After performing the task, will be silent for 6 secs
            speak("Is there anything else you want me to do?")  #This statement will be executed after 6 secs
            # intake()
        elif 'open' in query:  #If machine senses open in the query, the following code will be executed like "open Youtube, Open Spotify"
            query = query.replace("open ","")   
            query = query.replace(" ","")
            webbrowser.open("https://"+query+".com"+"")
            speak("Cool! This is what I found!")
            time.sleep(5)
            speak("Is there anything else you want me to do?")
            # intake()
        elif 'search' in query:
            query = query.replace("search ", "")
            query = query.replace(" ","")
            webbrowser.open(query+" ")
            speak("Right away in a jiffy!!")
            time.sleep(10)
            speak("Is there anything else you want me to do?")
            # intake()
        elif 'joke' in query:
            query = pyjokes.get_joke(language="en", category="all")
            print(query)
            speak(query)
            time.sleep(5)
            speak("Is there anything else you want me to do?")
            # intake()
        elif "where is" in query:
            Place = query
            query = query.replace("where is", "")
            location = query
            speak("User asked to Locate")
            speak(location)
            webbrowser.open("https://www.google.com/maps/place/" +location+ "")
            time.sleep(6)
            speak("Is there anything else you want me to do?")
            # intake()
        elif "time" in query:
            currtime = datetime.datetime.now().strftime("%H:%M")
            speak("The time is:")
            speak(currtime)
            print(currtime)
            time.sleep(2)
            speak("Is there anything else you want me to do?")
            # intake()
        elif "your name" in query:
            print("My name is Mr.Marson junior.")
            speak("My name is Mr.Marson Junior.")
            time.sleep(2)
            speak("Is there anything else you want me to do?")
            # intake()
        elif "close google chrome" in query:
            os.system("taskkill /im chrome.exe /f")
            speak("Browser Closed!")
            time.sleep(1)
            speak("Is there anything else you want me to do?")
            # intake()
        elif "close browser" in query:
            os.system("taskkill /im msedge.exe /f")
            speak("Browser Closed!")
            time.sleep(1)
            speak("Is there anything else you want me to do?")
            # intake()
        elif "no" in query:
            print("Thank you! I hope I was helpful :)")
            speak("Thank you! I hope I was helpful")
            exit()
        elif "bye" in query:
            print("Thank you! I hope I was helpful :)")
            speak("Thank you! I hope I was helpful")
            exit()

        
        


