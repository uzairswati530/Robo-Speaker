import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1 Created by M UZair")
    while True:
        x = input("Enter what do you want me to speak (or type 'q' to quit): ")
        if x.lower() == "q":
            # Use PowerShell's text-to-speech for the "bye bye" message
            os.system("powershell -Command \"Add-Type -AssemblyName System.Speech; "
                      "$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; "
                      "$speak.Speak('bye bye')\"")
            break
        # Using PowerShell's text-to-speech feature for user input
        command = f"powershell -Command \"Add-Type -AssemblyName System.Speech; " \
                  f"$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; " \
                  f"$speak.Speak('{x}')\""
        os.system(command)
