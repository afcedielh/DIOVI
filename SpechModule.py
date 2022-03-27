import pyttsx3

def text_to_voice(text):
    s = pyttsx3.init()
    data = text
    s.say(data)
    s.runAndWait()
