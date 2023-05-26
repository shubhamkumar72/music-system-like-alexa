import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime 
import wikipedia 
import pyjokes
listener =sr.Recognizer()
engine =pyttsx3.init()
voices=engine.getProperty('voices')
engine.setProperty('voice',voices[1].id)
engine.setProperty('rate',150 )

def talk(text):
    engine.say(text)
    engine.runAndWait()
def take_command():
    try:
        with sr.Microphone() as source:
            print("now you can speake......... i'm  listening......")
            engine.say("now you can speake......... i'm  listening......")
            engine.runAndWait()
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alexa' in command:
                command = command.replace('alexa','')
                print(command)
    except:
        pass
    return command
def run_alexa():
    command = take_command()
    print(command)
    if 'play' in command:
        song = command.replace('play','')
        talk('playing'+song)
        pywhatkit.playonyt(song)
    elif 'time now' in command:
        time = datetime.datetime.now().strftime("%H:%M:%S")
        talk('current time is   '+ time )
    elif "who is " in command:
        person = command.replace( "who is ",'')
        
        info = wikipedia.summary(person,4)
        print("info")
        talk(info)
    elif "what is " in command:
       
        person = command.replace( "what is ",'')
        info = wikipedia.summary(person,4)
        print("info")
        talk(info)
    elif "ritik fathers name  " in command:
       talk(" mondal ko pata hai.. ")
        
    elif 'party' in command:
        talk("sorry , abhi mood nhi hai     firr kabhi  ")
    elif 'are you single' in command:
        talk(" NO I am in relationship with Anupam ")
    elif 'joke' in command:
        talk(pyjokes.get_joke())
    else:
        talk("please repeat i'm not able to understand ")   
while True:
    run_alexa()


