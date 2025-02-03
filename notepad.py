import tkinter as tk
from tkinter import filedialog
import speech_recognition as sr
import pyttsx3
import webbrowser
import time
import urllib.parse

# Initialization of the text-to-speech engine
engine = pyttsx3.init()

# Creating the main window
root = tk.Tk()
root.title("Improved notepad")
root.geometry("600x400")

# Text area where the user can enter or view text
text_area = tk.Text(root, wrap='word', height=20, width=80)
text_area.pack(padx=10, pady=10)

# Save text function
def save_file():
    file = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, 'w') as f:
            f.write(text_area.get("1.0", "end-1c"))

# Function to open an existing file
def open_file():
    file = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if file:
        with open(file, 'r') as f:
            content = f.read()
            text_area.delete('1.0', 'end')
            text_area.insert('1.0', content)

# Function to activate voice recognition and convert voice into text or open Google
def voice_to_text_or_google():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        
        try:
            text = recognizer.recognize_google(audio, language="en-US")
            
            if "ok google" in text.lower():
                time.sleep(0.25)
                audio = recognizer.listen(source)

                command = recognizer.recognize_google(audio, language="en-US").lower()

                if "open" in command:
                    site_name = command.replace("open", "").strip()
                    if "wikipedia" in site_name or "wikipédia" in site_name:
                        webbrowser.open("https://www.wikipedia.org")
                    else:
                        webbrowser.open(f"https://www.{site_name}.com")

                elif "find" in command:
                    query = command.replace("find", "").strip()
                    if query:
                        query = urllib.parse.quote_plus(query)
                        webbrowser.open(f"https://www.google.com/search?q={query}")

            else:
                text_area.insert(tk.END, text + " ")

        except sr.UnknownValueError:
            print("Retry")
        except sr.RequestError:
            print("Connection error with voice recognition services.")

# Function for reading text aloud
def read_text():
    text = text_area.get("1.0", "end-1c")
    engine.say(text)
    engine.runAndWait()

# Create buttons for the graphical interface
save_button = tk.Button(root, text="Save", command=save_file)
save_button.pack(side=tk.LEFT, padx=10)

open_button = tk.Button(root, text="Open", command=open_file)
open_button.pack(side=tk.LEFT, padx=10)

# Button to start voice dictation or Google command
voice_button = tk.Button(root, text="Dictate", command=voice_to_text_or_google)
voice_button.pack(side=tk.LEFT, padx=10)

read_button = tk.Button(root, text="Read", command=read_text)
read_button.pack(side=tk.LEFT, padx=10)

# Launch the Tkinter application
root.mainloop()
