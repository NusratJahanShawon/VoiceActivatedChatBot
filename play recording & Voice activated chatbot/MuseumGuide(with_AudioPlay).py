import pygame
import time
import os
import speech_recognition as sr
import pyttsx3

def play_audio(num):
    audio_path = os.path.join(os.path.dirname(__file__), f"audio{num}.mp3")
    if os.path.exists(audio_path):
        print(f"Playing audio: {audio_path}")
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
        recognized_text = recognizer.recognize_google(audio, language="en-US").lower()
        print("You said:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("Unable to understand speech.")
        return None
    except sr.RequestError as e:
        print("Error in request; {0}".format(e))
        return None

def main():
    pygame.mixer.init()
    engine = pyttsx3.init()

    while True:
        try:
            engine.say("Welcome! How can I assist you today? You can ask about general information, exhibit specifics, historical context, interactive features, practical information, or anything else you'd like to know.")
            engine.runAndWait()
            voice_input = recognize_speech()
            if voice_input is not None:
                if "general information" in voice_input:
                    engine.say("What would you like to know about? You can ask about opening hours, directions, ticket prices, guided tours, or special exhibitions.")
                    engine.runAndWait()
                    time.sleep(2)
                    general_input = recognize_speech()
                    if "opening hours" in general_input:
                        play_audio(1)  # Adjust to appropriate audio file number
                        time.sleep(2) 
                        engine.say("The opening hours are...")
                        engine.runAndWait()
                    # Add more elif conditions for other general information options

                # Add similar if-elif blocks for exhibit specifics, historical context, interactive features, practical information, and additional assistance

                elif "stop" in voice_input:
                    pygame.mixer.music.stop()
                    engine.say("Audio stopped.")
                    engine.runAndWait()
                else:
                    engine.say("Sorry, I didn't understand. Please try again.")
                    engine.runAndWait()
            else:
                print("Unable to understand speech.")
        except KeyboardInterrupt:
            engine.say("Exiting the program.")
            engine.runAndWait()
            print("\nExiting the program.")
            break

if __name__ == "__main__":
    main()
