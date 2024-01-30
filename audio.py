import os
import glob
import time
import wave
from pydub import AudioSegment
from pydub.playback import play
from playsound import playsound
from google.cloud import texttospeech
from mutagen.mp3 import MP3
import speech_recognition as sr

def tts(response_message, lang_code):
    os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "text.json"
    try:
        client = texttospeech.TextToSpeechClient()
        print("Client created successfully.")
    except Exception as e:
        print("Error:", str(e))
    
    text = "<speak>" + "" + response_message + "" + "</speak>"
    synthesis_input = texttospeech.SynthesisInput(ssml=text)

    try:
        if lang_code == "en-US":
            voice = texttospeech.VoiceSelectionParams(
                language_code=lang_code,
                ssml_gender=texttospeech.SsmlVoiceGender.MALE,
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.MP3,
            )
            response = client.synthesize_speech(
                input=synthesis_input,
                voice=voice,
                audio_config=audio_config,
            )

            filename = "audio.mp3"
            with open(filename, "wb") as out:
                out.write(response.audio_content)
            
            # Use playsound to play the audio
            playsound(filename)

        else:
            name = "ar-XA-Standard-B"
            text_input = texttospeech.SynthesisInput(text=response_message)
            voice_params = texttospeech.VoiceSelectionParams(
                language_code="ar-XA", name=name
            )
            audio_config = texttospeech.AudioConfig(
                audio_encoding=texttospeech.AudioEncoding.LINEAR16
            )

            response = client.synthesize_speech(
                input=text_input,
                voice=voice_params,
                audio_config=audio_config,
            )

            filename = f"{name}.wav"
            print(filename)
            with open(filename, "wb") as out:
                out.write(response.audio_content)
                print(f'Generated speech saved to "{filename}"')
            with wave.open(filename) as mywav:
                duration_seconds = mywav.getnframes() / mywav.getframerate()
                print(f"Length of the WAV file: {duration_seconds:.1f} s")

            # Use playsound to play the audio
            playsound(filename)

    except Exception as e:
        print("Error occurred ", e)

# Example usage



def stt(lang_code):
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
            text = r.recognize_google(audio, language=lang_code)
            print("You said:", text)
            return text

        except sr.UnknownValueError:
            # TODO: Implement the sleep function or other logic here
            print("Could not understand audio. No speech detected.")
            return None

        except sr.RequestError as e:
            error_message = f"Could not request results from Google Speech Recognition service; {e}"
            print(error_message)
            return error_message


if __name__ == "__main__":
    while 1:
        response =stt("en")
        if "how are you" in response:
            tts("I am good how are you","en-US")
        elif "bye" in response:
            tts("Good bye see you later", "en-US")
        else:
            tts(response, "en-US")