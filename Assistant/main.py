import pyttsx3  #This module helps in to convert the text into speech.  "pip install pyttsx3"
import datetime #This module helps in to fetch the date/time.
import speech_recognition as sr  #This module helps to recognize the speech of the user. Instead of writing speech_recognition all the time, It allows the programmer to write 'sr'.




engine = pyttsx3.init('sapi5')  #Initializing the pyttsx3 module  and setting 'sapi5' for voice output. sapi5 is used for windows.
voices = engine.getProperty("voices")  #Asking engine to get voices
engine.setProperty("voices", voices[0].id)  #Setting the voice (0 for Male, 1 for Female)




def speak(audio):  #passing an argument to let the machine speak
    engine.say(audio) #We are asking the engine to say whatever written in "Speak"
    engine.runAndWait()  #The engine will first run and wait until the user finishes the query and returns the value

def greetings(): 
    """This function is to greet the user according to the time"""

    hour = int(datetime.datetime.now().hour)   #syntax for time and adding '.hour' at the end to that instead of full time string, the computer can easily decides from the hour also typecast in 'int' for conditional operators.

    if hour>=0 and hour<=12:
        speak("Good Morning!")
    elif hour >=12 and hour <=17:
        speak("Good Afternoon!")
    else:
        speak("Good Evening!")

    speak("I am Mr.Marson Jr., How can I help you?")  #After wishing, the bot will return the stated command.

def intake():
    """This function listens to the user's query"""

    r = sr.Recognizer()  #This is class which helps in to recognize the command given by the user and store in the variable of 'r'.

    with sr.Microphone() as source: #The speech of the user will be taken with the help of microphone.
        print("I am Listening..")
        r.pause_threshold = 1  #Mr.Marson Jr. will wait for 1 sec after the user query phrase to return the value.
        audio = r.listen(source) #This function helps in listening the user query from the 'source'

    try:  
        print("Getting best solution..")
        query = r.recognize_google(audio, language="en-in")  #Developer is assigning to use google to search for user's query whatever is listen through source "Line 41" en-in is ISO code for English India
        print("you said:\n", query)
    
    except Exception as e:
        speak("I'm afraid I could'nt get what you asked for, please repeat your query again.")
        print("I'm afraid I could'nt get what you asked for, please repeat your query again.")
    return query

if __name__ == "__main__":
    greetings()
    intake()



