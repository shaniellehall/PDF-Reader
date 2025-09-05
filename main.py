import pyttsx3
from PyPDF2 import PdfReader
from tkinter.filedialog import askopenfilename

# Select PDF file
book = askopenfilename()
reader = PdfReader(book)
pages = len(reader.pages)

# Initialize TTS engine once
player = pyttsx3.init()

# Get available voices
voices = player.getProperty("voices")

# Show available voices
print("Available voices:")
for index, voice in enumerate(voices):
    print(f"{index}: {voice.name} ({voice.id})")

# Let user pick a voice
choice = int(input("Enter the number of the voice you want: "))
if 0 <= choice < len(voices):
    player.setProperty("voice", voices[choice].id)
else:
    print("Invalid choice, using default voice.")

# Optional: adjust rate & volume
player.setProperty("rate", 150)   # speed (words per minute)
player.setProperty("volume", 1.0) # volume (0.0 to 1.0)

# Read the PDF
for i in range(pages):
    page = reader.pages[i]
    text = page.extract_text()
    if text:
        player.say(text)

player.runAndWait()
