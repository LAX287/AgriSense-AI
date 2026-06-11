import pyttsx3

engine = pyttsx3.init()

# Optional: adjust speed
engine.setProperty('rate', 150)

# Optional: increase volume
engine.setProperty('volume', 1.0)

engine.say("Welcome to AgriSense AI")
engine.runAndWait()

print("Voice command executed")