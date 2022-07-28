#Functions
import pywhatkit
import datetime
import wikipedia
from datetime import date

import Listener
import sounds


def run(): #insert via priotiy command keyword
    try:
        if 'alice' in Listener.take_command():
            global textCommand
    except TypeError:
        pass
    finally:
        try:
            textCommand = Listener.take_command().replace('alice', ' ')
            print("ALICE is listening...")
            print(textCommand)
            if 'play' in textCommand:
                playSong()
            elif 'time' in textCommand:
                checkTime()
            elif 'what' in textCommand:
                wikiPedia()
            elif 'shutdown' in textCommand:
                shutDown()
            else:
                Listener.talk("I'm sorry. Can you repeat that?") #fix engaging when alice is not called
        except AttributeError:
            pass



def initialize():
    Listener.talk("Initializing ALICE ...")

def greetings():
    sounds.soundListening()
    today = date.today()
    todayDate = today.strftime("%B %d, %Y")
    hour = datetime.datetime.now().hour
    time = datetime.datetime.now().strftime('%I:%M %p')


    if hour < 12:
        Listener.talk("Good Morning JC")
        Listener.talk('Today is ' + todayDate + '. and its ' + time)

    elif hour < 18:
        Listener.talk("Good Afternoon JC" )
        Listener.talk("Today is " + todayDate + ". and its " + time)
    else:
        Listener.talk("Good Evening JC")
        Listener.talk("Today is " + todayDate + ". and its " + time)
    sounds.soundDone()



def shutDown():
    sounds.soundListening()
    Listener.talk('Initiating Shutdown Sequence')
    print("Initiating Shutdown Sequence...")
    sounds.soundShutdown()
    quit()

def playSong():
    sounds.soundListening()
    song = textCommand.replace('play', '')
    Listener.talk('playing ' + song)
    pywhatkit.playonyt(song)
    sounds.soundDone()



def checkTime():
    sounds.soundListening()
    time = datetime.datetime.now().strftime('%I:%M %p')
    Listener.talk('Current time is ' + time)
    sounds.soundDone()


def wikiPedia():
    sounds.soundListening()
    try:
        whatQuestion = textCommand.replace('what', '')
        info = wikipedia.summary(whatQuestion, 1)
        print(info)
        Listener.talk(info)
        sounds.soundDone()

    except:
        Listener.talk("This is not available on wikipedia")
        sounds.soundDone()




