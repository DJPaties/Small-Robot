import speech_recognition as sr
from gtts import gTTS
import os

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something:")
        audio = recognizer.listen(source)
    try:
        text = recognizer.recognize_google(audio)
        print(f"You said: {text}")
        return text
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
        return None
    except sr.RequestError as e:
        print(f"Could not request results; {e}")
        return None

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"mpg321 {filename}")

if __name__ == "__main__":
    spoken_text = recognize_speech()
    if spoken_text:
        text_to_speech(spoken_text)
