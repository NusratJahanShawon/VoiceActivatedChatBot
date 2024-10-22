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
        print(f"অডিও ফাইল {audio_path} পাওয়া যায়নি।")


def recognize_speech():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("শুনছি...")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language="bn-BD").lower()
        print("আপনি বলেছেন:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("শব্দ বোঝা যায়নি।")
        return None  # Return None if speech cannot be understood
    except sr.RequestError as e:
        print("ফলাফল অনুরোধ করা যায়নি; {0}".format(e))
        return None  # Return None if there's an error in the request


def main():
    pygame.mixer.init()
    while True:
        try:
            voice_input = recognize_speech()
            if voice_input is not None:
                if "অবসর" in voice_input:
                    # Respond to the leisure command
                    play_audio(1)  # For example, play some relaxing music
                    time.sleep(2)  # Adjust this delay as needed
                elif "অডিও এক চালু করো" in voice_input:
                    play_audio(1)
                    time.sleep(2)  # Adjust this delay as needed
                elif "অডিও দুই চালু করো" in voice_input:
                    play_audio(2)
                    time.sleep(2)  # Adjust this delay as needed
                else:
                    print("প্রবেশ বুঝা যায়নি। আবার চেষ্টা করুন।")
        except KeyboardInterrupt:
            print("\nপ্রস্থান করছি।")
            break


if __name__ == "__main__":
    main()
