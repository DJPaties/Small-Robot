import os
from google.cloud import texttospeech
from pydub import AudioSegment
from pydub.playback import play  # Importing the play function
import glob
import time
from concurrent.futures import ThreadPoolExecutor
from serialSender import mouth, talking_scenario

def tts(response_message, lang_code):
    print("TTS")
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'tts.json'
    try:
        client = texttospeech.TextToSpeechClient()
        print("Client created successfully.")
    except Exception as e:
        print("Error:", str(e))
        
    text = '<speak>' + response_message + '</speak>'
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
                input=synthesis_input, voice=voice, audio_config=audio_config,
            )

            filename = 'audio.mp3'
            with open(filename, 'wb') as out:
                out.write(response.audio_content)
                
            audio = AudioSegment.from_file(filename)
            print("MP3 audio length is ", audio.duration_seconds)
            audio.export(filename, format="mp3")
            play(audio)  # Play the loaded audio
            
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

            filename = f"botConnecterarabic.wav"
            with open(filename, "wb") as out:
                out.write(response.audio_content)
                
            audio = AudioSegment.from_file(filename)
            print("WAV audio length is ", audio.duration_seconds)
            audio.export(filename, format="wav")
            play(audio)  # Play the loaded audio
            
    except Exception as e:
        print("Error occurred ", e)

# tts("Bye Bye Mohammad Dghaily", 'ar-LB')
