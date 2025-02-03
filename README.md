# ImprovedPythonNotepad
This is a simple notepad that will be updated as much as possible.
This project was something I worked on for my Computer Science class after we learned about APIs. We were given the freedom to choose a project, and I decided to create a tool that combines several interesting features like voice recognition, text-to-speech, and file management, all within a simple graphical interface. My goal was to practice using APIs and strengthen my Python skills by building something practical and interactive.

Here's how the code works:

Graphical User Interface (GUI):
I used the tkinter library to create a window where users can interact with the app. The window includes a text area where users can type or see text, and several buttons to perform actions like saving or opening files, dictating text, or having the text read aloud.

Voice Recognition:
One of the main features of the app is the ability to convert speech into text. I used the speech_recognition library to capture the user's voice through a microphone. The program listens for speech and converts it into text, which is then inserted into the text area. If the program hears "Ok Google," it recognizes this as a command to search the web or open websites. For example, if you say "Open Wikipedia," it opens the Wikipedia website.

Text-to-Speech:
The app can also read the text aloud. I used the pyttsx3 library to make this possible. When you click the "Read" button, the app reads all the text entered in the text area. This feature is helpful for people who may want to listen to the text instead of reading it.

File Handling:
The app allows you to open and save text files. Using Tkinter's file dialog, you can choose to save your work as a .txt file or open an existing text file. This makes the app more functional, letting you store your notes or other text-based documents.

Buttons for Interaction:
I created four buttons that trigger the main actions of the app:

Save: Saves the current text to a file.

Open: Opens an existing text file and displays its content in the text area.

Dictate: Starts the voice recognition process, allowing the user to speak and have it converted into text or issue a command like opening a website.

Read: Makes the app read the text aloud.
