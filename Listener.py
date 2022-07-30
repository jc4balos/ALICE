# this py file contains the listening mechanism of ALICE


import speech_recognition as sr
import pyttsx3



# Initializing PyAudio (Audio Input)
listener = sr.Recognizer()                      # Creating Recognizer Instance
engine = pyttsx3.init()                         # Initializing TTS

#Voice Properties
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
rate = engine.getProperty('rate')
engine.setProperty('rate', rate-25)

#Engaging Text to Speech
def talk(text):
    engine.say(text)
    engine.runAndWait()

# Speech to Text Translator
def take_command():
    command = None
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)             # Listen To Speech
            command = listener.recognize_google(voice)  # Use google Web Speech API
            command = command.lower()                   # Changing Speechs Recognizer input into lowercase
            if 'alice' in command:                      # Checks if "Alice" has been said
                command = command.replace('alice', '')

                return command                          #Returns Speech input
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





