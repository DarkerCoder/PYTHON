import pyttsx3  # type: ignore

engine = pyttsx3.init()
name = input("Enter your msg for speak : ")
engine.say(name)
engine.runAndWait()
