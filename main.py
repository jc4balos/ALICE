import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
from playsound import playsound





from datetime import date
listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()


def take_command():

    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alice' in command:
                playsound('./sounds/listening.mp3')
                command = command.replace('alice', '')
                print('ALICE is listening...')
    except:
        pass
    return command #Fix Unbound Local Error

                        #UnboundLocalError: local variable 'command' referenced before assignment

def run_alice():
    try:
        command = take_command()
        print(command)
    except:
        print('An Error Occured')
    else:
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        elif 'what' in command:
            try:
                person = command.replace('what', '')
                info = wikipedia.summary(person, 1)
                print(info)
                talk(info)
            except:
                talk("This is not available on wikipedia")
            finally:
                run_alice()
        elif 'date' in command:
            talk('sorry, I have a headache')
        elif 'facebook' in command:
            talk('I cant open facebook. Please fix this issue.')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'initiate shutdown sequence' in command:
            talk('Goodbye JC! Have a great day!')
            playsound('./sounds/shutdown.mp3')
            quit()
        else:
            talk('Please say the command again.')
    playsound('./sounds/done.mp3')

def greetings():
    today = date.today()
    todayDate = today.strftime("%B %d, %Y")
    hour = datetime.datetime.now().hour
    currentTime = time = datetime.datetime.now().strftime('%I:%M %p')


    if hour < 12:
        talk("Good Morning JC")
        talk('Today is ' + todayDate + '. and its ' + currentTime)

    elif hour < 18:
        talk("Good Afternoon JC" )
        talk("Today is " + todayDate + ". and its " + currentTime)
    else:
        talk("Good Evening JC")
        talk("Today is " + todayDate + ". and its " + currentTime)



def initialize():
    talk("Initializing ALICE ...")

def testmic():
    #get the total index number (n) of microphones
    #if mic has no audio, 0++ < n
    #if mic has audio, stop
    mics = sr.Microphone.list_microphone_names()
    micAmount = str(len(mics))
    print(micAmount + ' Audio Sources Available')



#initialize()
#greetings()

while True:
    testmic()
    run_alice()


