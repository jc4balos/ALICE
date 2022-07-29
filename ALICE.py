# This File contains the commands and functions of ALICE




# Functions
import pywhatkit
import datetime
from datetime import date

import Google
import Listener
import sounds

def run(): #insert via priotiy command keyword
    try:

        textCommand = Listener.take_command()
        print(textCommand)
        try:
            print("ALICE is listening...")

            if 'play' in textCommand:
                sounds.soundListening()
                song = textCommand.replace('play', '')
                Listener.talk('playing ' + song)
                pywhatkit.playonyt(song)
                sounds.soundDone()

            elif 'date' in textCommand:
                sounds.soundListening()
                today = date.today()
                todayDate = today.strftime("%B %d, %Y")
                Listener.talk('The Date todat is ' + todayDate)
                sounds.soundDone()

            elif 'time' in textCommand:
                sounds.soundListening()
                time = datetime.datetime.now().strftime('%I:%M %p')
                Listener.talk('Current time is ' + time)
                sounds.soundDone()

            elif 'what' in textCommand:
                sounds.soundListening()
                try:
                    whatQuestion = textCommand.replace('what', ' ')
                    info = Google.query(whatQuestion)
                    Listener.talk(info)
                    sounds.soundDone()
                except:
                    Listener.talk("I cannot understand your query.")
                    sounds.soundDone()

            elif 'calculate' in textCommand: # fix this
                equation = textCommand.replace('calculate', '')
                try:
                    answer = Google.calculate(equation)
                    Listener.talk(answer)
                    sounds.soundDone()
                except:
                    Listener.talk("I'm sorry! I cannot calculate that.")
                    sounds.soundDone()

            elif 'shutdown' in textCommand:
                sounds.soundListening()
                Listener.talk('Initiating Shutdown Sequence')
                print("Initiating Shutdown Sequence...")
                sounds.soundShutdown()
                quit()

            else:
                Listener.talk("I'm sorry. Can you repeat that?")  # fix engaging when alice is not called

        except AttributeError:
            pass

    except TypeError:
        pass

def initialize():
    sounds.soundListening()
    Listener.talk("Initializing ALICE ...")

def greetings():
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






