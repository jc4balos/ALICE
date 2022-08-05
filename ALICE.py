# This File contains the commands and functions of ALICE




# Functions
import pywhatkit
import datetime
from datetime import date

import Google
import Listener
import sounds
import Applications

# Main Function
def run():
    try:

        textCommand = Listener.take_command()                       # Fetch the returned speech input
        print(textCommand)
        try:
            print("ALICE is listening...")

# Play Youtube
            if 'play' in textCommand:
                sounds.soundListening()
                song = textCommand.replace('play', '')
                Listener.talk('playing ' + song)
                pywhatkit.playonyt(song)
                sounds.soundDone()

# Checking the Date
            elif 'date' in textCommand:
                sounds.soundListening()
                today = date.today()
                todayDate = today.strftime("%B %d, %Y")
                Listener.talk('The Date todat is ' + todayDate)
                sounds.soundDone()

# Checking the Time
            elif 'time' in textCommand:
                sounds.soundListening()
                time = datetime.datetime.now().strftime('%I:%M %p')
                Listener.talk('Current time is ' + time)
                sounds.soundDone()

# Google (Still Buggy)
            elif ('who' in textCommand) or ('what' in textCommand) or ('where' in textCommand) or ('when' in textCommand):
                sounds.soundListening()
                try:
                    searchQuestion = textCommand.replace('what', ' ')
                    info = Google.query(searchQuestion)
                    Listener.talk(info)
                    sounds.soundDone()
                except:
                    Listener.talk("I cannot understand your query.")
                    sounds.soundDone()

# Calculator
            elif 'calculate' in textCommand: # fix this
                equation = textCommand.replace('calculate', '')
                try:
                    answer = Google.calculate(equation)
                    Listener.talk(answer)
                    sounds.soundDone()
                except:
                    Listener.talk("I'm sorry! I cannot calculate that.")
                    sounds.soundDone()
# Application Open/Close
            elif ('open' in textCommand) or ('close' in textCommand):
                sounds.soundListening()
                Applications.open(textCommand)
                sounds.soundDone()

# Shutdown
            elif ('shutdown' in textCommand) or ('power off' in textCommand):
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






