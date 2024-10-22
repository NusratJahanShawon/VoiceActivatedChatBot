import time
import os
import speech_recognition as sr
import pyttsx3

def recognize_speech(recognizer, microphone):
    with microphone as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)

    try:
        recognized_text = recognizer.recognize_google(audio, language="bn-BD").lower()
        print("আপনি বলেছেন:", recognized_text)
        return recognized_text
    except sr.UnknownValueError:
        print("কথা বুঝতে অক্ষম.")
        return None
    except sr.RequestError as e:
        print("অনুরোধে ত্রুটি; {0}".format(e))
        return None

def main():
    recognizer = sr.Recognizer()
    microphone = sr.Microphone()
    engine = pyttsx3.init()

    print("শুনছি 'হ্যালো'...")
    hello_text = recognize_speech(recognizer, microphone)

    while True:
        if hello_text and "হ্যালো" in hello_text:
            break
        else:
            print("'হ্যালো' শোনা গেল না। দয়া করে শুরু করতে 'হ্যালো' বলুন।")
            hello_text = recognize_speech(recognizer, microphone)

    while True:
        try:
            print("শুনছি...")
            engine.say("স্বাগতম! আজ আমি আপনাকে কীভাবে সাহায্য করতে পারি?")
            engine.say("আপনি সাধারণ তথ্য, প্রদর্শনী বিশেষত্ব, ঐতিহাসিক প্রসঙ্গ, ইন্টারঅ্যাক্টিভ বৈশিষ্ট্য, প্রায়শই তথ্য, বা আরো কিছু জানতে পারেন।")
            print("স্বাগতম! আজ আমি আপনাকে কীভাবে সাহায্য করতে পারি?")
            print("আপনি সাধারণ তথ্য, প্রদর্শনী বিশেষত্ব, ঐতিহাসিক প্রসঙ্গ, ইন্টারঅ্যাক্টিভ বৈশিষ্ট্য, প্রায়শই তথ্য, বা আরো কিছু জানতে পারেন।")
            engine.runAndWait()
            time.sleep(2)
            print("শুনছি...")
            voice_input = recognize_speech(recognizer, microphone)
            if voice_input is not None:
                if "সাধারণ তথ্য" in voice_input:
                    while True:
                        engine.say("আপনি কী জানতে চান?")
                        engine.say("আপনি বিকালের সময়, নির্দেশানগুলি, নির্দেশিকা প্রদর্শনী বা কক্ষগুলি, গাইডেড ট্যুরের উপলব্ধতা, টিকিটের মূল্য, বা বিশেষ প্রদর্শনী সম্পর্কে তথ্য জিজ্ঞাসা করতে পারেন।")
                        print("আপনি বিকালের সময়, নির্দেশানগুলি, নির্দেশিকা প্রদর্শনী বা কক্ষগুলি, গাইডেড ট্যুরের উপলব্ধতা, টিকিটের মূল্য, বা বিশেষ প্রদর্শনী সম্পর্কে তথ্য জিজ্ঞাসা করতে পারেন।")
                        engine.runAndWait()
                        time.sleep(2)
                        print("শুনছি...")
                        general_input = recognize_speech(recognizer, microphone)
                        if general_input is not None:
                            if "বিকালের সময়" in general_input:
                                engine.say("বিকালের সময় সোমবার থেকে শনিবার সকাল 9 টা থেকে রাত 5 টা, এবং রবিবার সকাল 10 টা থেকে রাত 4 টা।")
                                print("বিকালের সময় সোমবার থেকে শনিবার সকাল 9 টা থেকে রাত 5 টা, এবং রবিবার সকাল 10 টা থেকে রাত 4 টা।")
                                engine.runAndWait()
                                time.sleep(2)
                                engine.say("আরো কিছু জানতে আছে?")
                                print("আরো কিছু জানতে আছে?")
                                engine.runAndWait()
                                time.sleep(2)
                                anything_else_input = recognize_speech(recognizer, microphone)
                                if anything_else_input and "হ্যাঁ" in anything_else_input:
                                    print("'হ্যালো' শোনা যাচ্ছে...")
                                    hello_text = recognize_speech(recognizer, microphone)
                                    while True:
                                        if hello_text and "হ্যালো" in hello_text:
                                            break
                                        else:
                                            print("'হ্যালো' শোনা গেল না। দয়া করে শুরু করতে 'হ্যালো' বলুন।")
                                            hello_text = recognize_speech(recognizer, microphone)
                                    continue
                                elif anything_else_input and "না" in anything_else_input:
                                    engine.say("ঠিক আছে, যদি আরো কিছু দরকার হয়, অবশ্যই বলুন।")
                                    engine.runAndWait()
                                    break
                            elif "গাইডেড ট্যুর" in general_input:
                                engine.say("হ্যাঁ, গাইডেড ট্যুর উপলব্ধ। এটা সাধারণত প্রতি ঘণ্টায় 10 টা থেকে 4 টার মধ্যে চলে।")
                                engine.runAndWait()
                                time.sleep(2)
                                engine.say("আরো কিছু জানতে আছে?")
                                engine.runAndWait()
                                time.sleep(2)
                                anything_else_input = recognize_speech(recognizer, microphone)
                                if anything_else_input and "হ্যাঁ" in anything_else_input:
                                    print("'হ্যালো' শোনা যাচ্ছে...")
                                    hello_text = recognize_speech(recognizer, microphone)
                                    while True:
                                        if hello_text and "হ্যালো" in hello_text:
                                            break
                                        else:
                                            print("'হ্যালো' শোনা গেল না। দয়া করে শুরু করতে 'হ্যালো' বলুন।")
                                            hello_text = recognize_speech(recognizer, microphone)
                                    continue
                                elif anything_else_input and "না" in anything_else_input:
                                    engine.say("ঠিক আছে, যদি আরো কিছু দরকার হয়, অবশ্যই বলুন।")
                                    engine.runAndWait()
                                    break
                            else:
                                engine.say("দুঃখিত, আমি বুঝিনি। অনুগ্রহ করে আবার চেষ্টা করুন।")
                                engine.runAndWait()
                                break
                        else:
                            engine.say("দুঃখিত, আমি বুঝিনি। অনুগ্রহ করে আবার চেষ্টা করুন।")
                            engine.runAndWait()
                            break

                elif "প্রদর্শনী বিশেষত্ব" in voice_input:
                    engine.say("আপনি কী প্রদর্শনী বা কার্যকলাপ সম্পর্কে জানতে চান? আপনি একটি নির্দিষ্ট প্রদর্শনী বা কার্যকলাপ, নির্দিষ্ট কর্মীর কাজ, বিখ্যাত কার্যকলাপ, কৃত্রিম প্রাচীনতা, বা প্রসারণ জন্য অনুশিক্ষণ প্রশ্ন করতে পারেন।")
                    engine.runAndWait()
                    time.sleep(2)
                    exhibit_input = recognize_speech(recognizer, microphone)
                    if "বিখ্যাত কার্যকলাপ" in exhibit_input:
                        engine.say("কিছু বিখ্যাত কার্যকলাপ হল 'মোনা লিসা' এবং 'ভান রাত' দ্বারা লিওনার্ডো দা ভিঞ্সি এবং ভিনসেন্ট ভ্যান গগ।")
                        engine.runAndWait()

                elif "ঐতিহাসিক তথ্য" in voice_input:
                    engine.say("আপনি কী ঐতিহাসিক তথ্য জানতে চান? আপনি মিউজিয়াম / জায়গার ইতিহাস, প্রদর্শনী / শিল্পকলার ঐতিহাসিক প্রসঙ্গ, এলাকার পূর্ববর্তী ঘটনা, বা ভবনের স্থাপত্য সম্পর্কে তথ্য জিজ্ঞাসা করতে পারেন।")
                    engine.runAndWait()
                    time.sleep(2)
                    historical_input = recognize_speech(recognizer, microphone)
                    if "এই জায়গার ইতিহাস" in historical_input:
                        engine.say("এই জায়গার মিউজিয়াম প্রতিষ্ঠিত হয় ১৯২০ সালে এবং তারপর প্রসিদ্ধি অর্জন করে।")
                        engine.runAndWait()

                elif "ইন্টারঅ্যাক্টিভ বৈশিষ্ট্য" in voice_input:
                    engine.say("আপনি কি ইন্টারঅ্যাক্টিভ প্রদর্শনী বা কার্যকলাপে আগ্রহী? আমি হাতের অভিজ্ঞতা, ছবি নীতি, গিফ্ট শপ, বা অন্য কোনও ইন্টারঅ্যাক্টিভ বৈশিষ্ট্য সম্পর্কে তথ্য প্রদান করতে পারি।")
                    engine.runAndWait()
                    time.sleep(2)
                    interactive_input = recognize_speech(recognizer, microphone)
                    if "গিফ্ট শপ" in interactive_input:
                        engine.say("হ্যাঁ, এখানে আপনি সুভাষিত কিনতে পারেন।")
                        engine.runAndWait()

                elif "প্রায়শই তথ্য" in voice_input:
                    engine.say("আপনি কী প্রায়শই তথ্য জানতে চান? আপনি শৌচাগার, ক্যাফে বা রেস্তোরাঁ সুবিধা, চক্রান্ত অ্যাক্সেস, পার্কিং সুবিধা, বা অন্য কোনও প্রায়শই বিষয় বিনামূল্যে পরিচিত করতে পারেন।")
                    engine.runAndWait()
                    time.sleep(2)
                    practical_input = recognize_speech(recognizer, microphone)
                    if "শৌচাগার" in practical_input:
                        engine.say("মিউজিয়ামের প্রতিটি তলায় শৌচাগার আছে।")
                        engine.runAndWait()

                elif "অতিরিক্ত সাহায্য" in voice_input:
                    engine.say("আপনি কি কোনও অতিরিক্ত সাহায্য চান? আমি মানচিত্র, অডিও গাইড, অনলাইন টিকিট বুকিং, বা কোট চেক বা লকার সুবিধা সম্পর্কে বিস্তারিত তথ্য প্রদান করতে পারি।")
                    engine.runAndWait()
                    time.sleep(2)
                    assistance_input = recognize_speech(recognizer, microphone)
                    if "মানচিত্র" in assistance_input:
                        engine.say("মিউজিয়ামের মানচিত্র প্রবেশদ্বারের কাছাকাছি উপলব্ধ।")
                        engine.runAndWait()

                elif "থামুন" in voice_input:
                    engine.say("প্রোগ্রাম থেকে বের হচ্ছি।")
                    engine.runAndWait()
                    print("\nপ্রোগ্রাম থেকে বের হচ্ছি।")
                    break
                else:
                    engine.say("দুঃখিত, আমি বুঝিনি। অনুগ্রহ করে আবার চেষ্টা করুন।")
                    engine.runAndWait()
            else:
                print("কথা বুঝতে অক্ষম.")
        except KeyboardInterrupt:
            engine.say("প্রোগ্রাম থেকে বের হচ্ছি।")
            engine.runAndWait()
            print("\nপ্রোগ্রাম থেকে বের হচ্ছি।")
            break

if __name__ == "__main__":
    main()
