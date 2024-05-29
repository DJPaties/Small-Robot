from gtts import gTTS
import os

def text_to_speech(text, filename="output.mp3"):
    # Generate speech from text
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    # Play the audio file
    os.system(f"mpg321 {filename}")

# Example usage
text = "Hello, how are you today?"
text_to_speech(text)
