import pygame
import time
import os

def play_audio(num):
    audio_path = os.path.join(os.path.dirname(__file__), f"audio{num}.mp3")
    if os.path.exists(audio_path):
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    else:
        print(f"Audio file {audio_path} not found.")

def main():
    pygame.mixer.init()
    while True:
        try:
            num = int(input("Enter a number (1 or 2 to play audio, any other number to exit): "))
            if num == 1 or num == 2:
                play_audio(num)
                time.sleep(2)  # Adjust this delay as needed
            else:
                print("Exiting.")
                break
        except ValueError:
            print("Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()







