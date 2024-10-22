import cv2
import numpy as np
import pygame
import os

# Function to play audio based on number
def play_audio(num):
    audio_path = os.path.join(os.path.dirname(__file__), f"audio{num}.mp3")
    if os.path.exists(audio_path):
        pygame.mixer.music.load(audio_path)
        pygame.mixer.music.play()
    else:
        print(f"Audio file {audio_path} not found.")

# Initialize Pygame mixer
pygame.mixer.init()

# Load the reference image
reference_image = cv2.imread('1.png', cv2.IMREAD_GRAYSCALE)

# Preprocess the reference image (optional)
# Perform any necessary preprocessing steps here

# Initialize camera
cap = cv2.VideoCapture(0)

# Get reference image dimensions
h, w = reference_image.shape

while True:
    # Capture frame-by-frame
    ret, frame = cap.read()

    # Convert frame to grayscale
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Resize reference image to match frame size
    reference_image_resized = cv2.resize(reference_image, (gray.shape[1], gray.shape[0]))

    # Perform template matching
    result = cv2.matchTemplate(gray, reference_image_resized, cv2.TM_CCOEFF_NORMED)

    # Define a threshold for matching
    threshold = 0.8

    # Find matches above the threshold
    loc = np.where(result >= threshold)

    # Draw bounding boxes around the matches
    for pt in zip(*loc[::-1]):
        cv2.rectangle(frame, pt, (pt[0] + w, pt[1] + h), (0, 255, 0), 2)

        # Play audio corresponding to the matched number
        play_audio(1)  # Change this according to your reference image

    # Display the captured frame
    cv2.imshow('Frame', frame)

    # Check for 'q' key press to exit the loop
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all OpenCV windows
cap.release()
cv2.destroyAllWindows()

