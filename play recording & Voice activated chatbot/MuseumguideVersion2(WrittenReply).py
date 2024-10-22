import time
import os
import speech_recognition as sr
import pyttsx3

def recognize_speech(recognizer, microphone):
    with microphone as source:
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
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()

    print("Listening for 'Hello'...")
    hello_text = recognize_speech(recognizer, microphone)

    while True:
        if hello_text and "hello" in hello_text:
            break
        else:
            print("Didn't hear 'Hello'. Please say 'Hello' to start.")
            hello_text = recognize_speech(recognizer, microphone)

    while True:
        try:
            print("Listening...")
            engine.say("Welcome! How can I assist you today?")
            engine.say("You can ask about general information, exhibit specifics, historical context, interactive features, practical information, or anything else you'd like to know.")
            print("Welcome! How can I assist you today?")
            print("You can ask about general information, exhibit specifics, historical context, interactive features, practical information, or anything else you'd like to know.")
            engine.runAndWait()
            time.sleep(2)
            print("Listening...")
            voice_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
            if voice_input is not None:
                if "general information" in voice_input:
                    while True:
                        engine.say("Sure, what would you like to know? ")
                        engine.say("You can ask about opening hours, directions to specific exhibits or rooms, availability of guided tours, ticket prices, or information about special exhibitions.")                 
                        print("You can ask about opening hours, directions to specific exhibits or rooms, availability of guided tours, ticket prices, or information about special exhibitions.")
                        engine.runAndWait()
                        time.sleep(2)
                        print("Listening...")
                        general_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
                        if general_input is not None:  # Check if general_input is not None
                            if "opening hours" in general_input:
                                print("The opening hours are from 9 am to 5 pm, Monday through Saturday, and from 10 am to 4 pm on Sundays.")
                                engine.say("The opening hours are from 9 am to 5 pm, Monday through Saturday, and from 10 am to 4 pm on Sundays.")
                                print("Listening...")
                                engine.runAndWait()
                                time.sleep(2)
                                engine.say("Is there anything else you would like to know?")
                                print("Is there anything else you would like to know?")
                                engine.runAndWait()
                                time.sleep(1)
                                anything_else_input = recognize_speech(recognizer, microphone).lower()  # Pass recognizer and microphone here
                                if anything_else_input and "yes" in anything_else_input:
                                    print("Listening for 'Hello'...")
                                    hello_text = recognize_speech(recognizer, microphone)
                                    while True:
                                        if hello_text and "hello" in hello_text:
                                            break
                                        else:
                                            print("Didn't hear 'Hello'. Please say 'Hello' to start.")
                                            hello_text = recognize_speech(recognizer, microphone)
                                    continue  # Restart the loop to the beginning
                                elif anything_else_input and "no" in anything_else_input:
                                    engine.say("Okay, let me know if you need anything else.")
                                    engine.runAndWait()
                                    break
                            elif "guided tour" in general_input:
                                engine.say("Yes, guided tours are available. They usually run every hour starting from 10 am to 4 pm.")
                                
                                engine.runAndWait()
                                time.sleep(2)
                                print("Listening...")

                                # Ask if the user wants to know anything else
                                engine.say("Is there anything else you would like to know?")
                                engine.runAndWait()
                                time.sleep(2)

                                anything_else_input = recognize_speech(recognizer, microphone).lower()  # Pass recognizer and microphone here
                                if anything_else_input and "yes" in anything_else_input:
                                    print("Listening for 'Hello'...")
                                    hello_text = recognize_speech(recognizer, microphone)
                                    while True:
                                        if hello_text and "hello" in hello_text:
                                            break
                                        else:
                                            print("Didn't hear 'Hello'. Please say 'Hello' to start.")
                                            hello_text = recognize_speech(recognizer, microphone)
                                    continue  # Restart the loop to the beginning
                                elif anything_else_input and "no" in anything_else_input:
                                    engine.say("Okay, let me know if you need anything else.")
                                    engine.runAndWait()
                                    # Proceed with other commands
                            # Add more elif conditions for other general information options
                            else:
                                engine.say("Sorry, I didn't understand. Please try again.")
                                engine.runAndWait()
                                break
                        else:
                            engine.say("Sorry, I didn't understand. Please try again.")
                            engine.runAndWait()
                            break

                    # Add more elif conditions for other general information options

                elif "exhibit specific" in voice_input:
                    engine.say("What specific information are you looking for about exhibits or artworks? You can ask about a particular exhibit or artwork, works by specific artists, famous pieces, significance of artifacts, or for recommendations.")
                    engine.runAndWait()
                    time.sleep(2)
                    exhibit_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
                    if "famous pieces" in exhibit_input:
                        engine.say("Some of the famous pieces include 'Mona Lisa' by Leonardo da Vinci and 'Starry Night' by Vincent van Gogh.")
                        engine.runAndWait()
                    # Add more elif conditions for other exhibit specific queries

                elif "historical information" in voice_input:
                    engine.say("What historical information would you like to know? You can ask about the history of the museum/place, historical context of exhibits/artworks, past events in the area, or information about the architecture of the building.")
                    engine.runAndWait()
                    time.sleep(2)
                    historical_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
                    if "history of this place" in historical_input:
                        engine.say("This museum was established in 1920 and has since become a landmark for showcasing art and history.")
                        engine.runAndWait()

                    # Ask if the user wants to know anything else
                    engine.say("Is there anything else you would like to know?")
                    engine.runAndWait()
                    time.sleep(2)
                    anything_else_input = recognize_speech(recognizer, microphone).lower()  # Pass recognizer and microphone here
                    if anything_else_input and "yes" in anything_else_input:
                        print("Listening for 'Hello'...")
                        hello_text = recognize_speech(recognizer, microphone)
                        while True:
                            if hello_text and "hello" in hello_text:
                                break
                            else:
                                print("Didn't hear 'Hello'. Please say 'Hello' to start.")
                                hello_text = recognize_speech(recognizer, microphone)
                        continue  # Restart the loop to the beginning
                    elif anything_else_input and "no" in anything_else_input:
                        engine.say("Okay, let me know if you need anything else.")
                        engine.runAndWait()
                        # Proceed with other commands
                    else:
                        engine.say("Sorry, I didn't understand your response.")
                        engine.runAndWait()

                    # Add more elif conditions for other historical information queries

                elif "interactive features" in voice_input:
                    engine.say("Are you interested in interactive exhibits or activities? I can provide information about hands-on experiences, photography policies, gift shops, or any other interactive features.")
                    engine.runAndWait()
                    time.sleep(2)
                    interactive_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
                    if "gift shop" in interactive_input:
                        engine.say("Yes, there is a gift shop located near the entrance where you can purchase souvenirs.")
                        engine.runAndWait()
                    # Add more elif conditions for other interactive features queries

                elif "practical information" in voice_input:
                    engine.say("What practical information do you need? You can inquire about restrooms, café or restaurant facilities, wheelchair access, parking facilities, or any other practical matters.")
                    engine.runAndWait()
                    time.sleep(2)
                    practical_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
                    if "restrooms" in practical_input:
                        engine.say("Restrooms are located on each floor of the museum for your convenience.")
                        engine.runAndWait()
                    # Add more elif conditions for other practical information queries

                elif "additional assistance" in voice_input:
                    engine.say("Do you need any additional assistance? I can provide maps, information about audio guides, online ticket booking, or details about coat check or locker facilities.")
                    engine.runAndWait()
                    time.sleep(2)
                    assistance_input = recognize_speech(recognizer, microphone)  # Pass recognizer and microphone here
                    if "maps" in assistance_input:
                        engine.say("Maps of the museum are available at the information desk near the entrance.")
                        engine.runAndWait()
                    # Add more elif conditions for other additional assistance queries

                elif "stop" in voice_input:
                    engine.say("Exiting the program.")
                    engine.runAndWait()
                    print("\nExiting the program.")
                    break
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
