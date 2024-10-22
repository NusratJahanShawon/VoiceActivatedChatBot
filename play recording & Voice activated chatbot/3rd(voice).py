import pygame
import time
import os
import speech_recognition as sr

def play_audio(num):
    audio_path = os.path.join(os.path.dirname(__file__), f"audio{num}.mp3")
    if os.path.exists(audio_path):
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    else:
        print(f"Audio file {audio_path} not found.")

def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio).lower()
        print("You said:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results; {0}".format(e))

def main():
    pygame.mixer.init()
    while True:
        try:
            voice_input = recognize_speech()
            if "play audio 1" in voice_input:
                play_audio(1)
                time.sleep(2)  # Adjust this delay as needed
            elif "play audio 2" in voice_input:
                play_audio(2)
                time.sleep(2)  # Adjust this delay as needed
            else:
                print("Input not recognized. Please try again.")
        except KeyboardInterrupt:
            print("\nExiting.")
            break

if __name__ == "__main__":
    main()
