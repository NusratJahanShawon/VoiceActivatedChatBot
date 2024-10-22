import pygame
import time
import os
import speech_recognition as sr
from gtts import gTTS


def play_audio(num):
    audio_path = os.path.join(os.path.dirname(__file__), f"audio{num}.mp3")
    if os.path.exists(audio_path):
        print(f"Playing audio: {audio_path}")
        pygame.mixer.init()
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy():
            pygame.time.Clock().tick(10)
    else:
        print(f"Audio file {audio_path} not found.")


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language="bn-BD").lower() # Recognize Bangla speech
        print("You said:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("Unable to understand speech.")
        return None
    except sr.RequestError as e:
        print("Error in request; {0}".format(e))
        return None


import tempfile

def speak_text(text):
    tts = gTTS(text=text, lang='bn')
    with tempfile.NamedTemporaryFile(suffix='.mp3', delete=False) as temp_file:
        audio_path = temp_file.name
        tts.save(audio_path)
        play_audio('')  # Play the audio file



def main():
    pygame.init()

    while True:
        try:
            speak_text("কোন অডিও চালাতে চান? অডিও এক চালাতে 'অডিও এক চালাও' বলুন এবং অডিও দুই চালাতে 'অডিও দুই চালাও' বলুন।")
            voice_input = recognize_speech()
            if voice_input is not None:  
                if "অডিও এক চালাও" in voice_input:
                    play_audio(1)
                    time.sleep(2) 
                    speak_text("অডিও এক চলছে।")
                elif "অডিও দুই চালাও" in voice_input:
                    play_audio(2)
                    time.sleep(2) 
                    speak_text("অডিও দুই চলছে।")
                elif "বন্ধ" in voice_input:
                    pygame.mixer.music.stop()
                    speak_text("অডিও বন্ধ হয়েছে।")
                else:
                    speak_text("দুঃখিত, আমি বুঝতে পারলাম না। অনুগ্রহ করে আবার চেষ্টা করুন।")
            else:
                print("Unable to understand speech.")
        except KeyboardInterrupt:
            speak_text("প্রোগ্রাম থেকে বাহির হচ্ছে।")
            print("\nপ্রোগ্রাম থেকে বাহির হচ্ছে।")
            break


if __name__ == "__main__":
    main()
