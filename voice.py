import speech_recognition as sr
from gtts import gTTS
import os

def stt(languageCode="en-US"):
    lang_code = languageCode
    # Create a recognizer object
    r = sr.Recognizer()

    # Open the microphone for capturing the speech
    with sr.Microphone() as source:
        print("Listening...")   
        
        # Adjust the energy threshold for silence detection
        r.energy_threshold = 4000

        # Listen for speech and convert it to text
        audio = r.listen(source)

        try:
            print("Analyzing")
            text = r.recognize_google(audio, language=lang_code)
            print("You said:", text)

        except sr.UnknownValueError:
            text = 'Not Understand'
            return text

        except sr.RequestError as e:
            text = "Could not request results from Google Speech Recognition service; {0}".format(e)
            print(text)
            return text

        return text.lower()

def text_to_speech(text, filename="output.mp3"):
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    os.system(f"mpg321 {filename}")

if __name__ == "__main__":
    while True:
        spoken_text = stt()
        if spoken_text:
            text_to_speech(spoken_text)
