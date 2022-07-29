# this py file contains the listening mechanism of ALICE


import speech_recognition as sr
import pyttsx3

#new libraries for OOP

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)


def talk(text):
    engine.say(text)
    engine.runAndWait()

def take_command(): #split this code into two parts
    command = None
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()
            if 'alice' in command:
                command = command.replace('alice', '')

                return command
    except:
        pass




#def testmic():
    #get the total index number (n) of microphones
    #if mic has no audio, 0++ < n
    #if mic has audio, stop
#    mics = sr.Microphone.list_microphone_names()
#    micAmount = str(len(mics))
#   print(micAmount + ' Audio Sources Available')
#    print("Input Reset")





