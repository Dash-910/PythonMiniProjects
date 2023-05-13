# install pyttsx3 library and intitalize text to speech engine 
#  using 'pyttsx3.init()'
import pyttsx3

if __name__ =='__main__':
    print("Welcome to RoboSpeaker 1.0 Created by Dash")
    engine = pyttsx3.init()

    while True:
        x=input("Enter what you want me to speak: ")
        if x=="q":
            goodbye = "bye bye friend"
            engine.say(goodbye)
            engine.runAndWait()
            break
        # To queue the text for speech systhsis
        engine.say(x)
        # To process the speech and wait for it to complete 
        # Before accepting next input
        engine.runAndWait()
  

