from gtts import gTTS
import os
import time
from mutagen.mp3 import MP3

def text_to_speech(text, lang='en', slow=False, filename="output.mp3"):
    try:
        # Create an instance of gTTS
        speech = gTTS(text=text, lang=lang, slow=slow)
        # Save the speech to an MP3 file
        speech.save(filename)
        print(f"Speech saved to {filename}")
        return filename
    except Exception as e:
        print(f"An error occurred: {e}")
        return None

def play_and_delete(filename):
    try:
        # Play the MP3 file using mpg321
        os.system(f"mpg321 {filename}")
        
        # Wait for the duration of the audio file before deleting
        audio = MP3(filename)
        time.sleep(audio.info.length + 1)  # Adding a little buffer
        
        # Remove the MP3 file after playing
        os.remove(filename)
        print(f"Deleted the file {filename}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    while True:
        text = input("Enter the text you want to convert to speech (or type 'exit' to quit): ")
        if text.lower() == 'exit':
            print("Exiting the program.")
            break
        filename = text_to_speech(text)
        if filename:
            play_and_delete(filename)
