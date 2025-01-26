import speech_recognition as sr


def speech_to_text() -> None:
    recognizer = sr.Recognizer()

    with sr.Microphone() as mic:
        print("Listening...")
        audio = recognizer.listen(mic)

    try:
        text = recognizer.recognize_google(audio)
        print(text)
    except sr.UnknownValueError:
        print("Sorry, couldn't get that...")
    except sr.RequestError as e:
        print(f"Could not request results from Google speech recognition service {e}")


def main() -> None:
    speech_to_text()


if __name__ == "__main__":
    main()
