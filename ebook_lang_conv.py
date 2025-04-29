# from googletrans import Translator
# from gtts import gTTS
# srcfile=open("my_intro.txt",mode='r')
# text=srcfile.read()
# translator = Translator()
# translated = translator.translate(text, src='en', dest='te')
# telugu_text_conv = translated.text

# print(f"\nTranslated to telugu language: {telugu_text_conv}")

# speech = gTTS(text=telugu_text_conv, lang='te')
# speech.save("Introduction_telugu.mp3")
# srcfile.close()
# print("\n Translation and Audio saved successfully as 'Introduction_telugu.mp3'.")




'''------------Read file translate fro eng to tel and create audion-------------'''
import asyncio
from googletrans import Translator
from gtts import gTTS
import edge_tts
import os

srcfile=open("my_intro.txt",mode='r')
text=srcfile.read()
translator = Translator()
translated = translator.translate(text, src='en', dest='te')
telugu_text_conv = translated.text

VOICE = "te-IN-MohanNeural"  # Telugu Male Voice
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
OUTPUT_FILE = os.path.join(BASE_DIR, "Introduction_telugu1.mp3")
#OUTPUT_FILE = r"C:\pdfreader\Introduction_telugu.mp3"
async def save_audio():
    communicate = edge_tts.Communicate(text=telugu_text_conv, voice=VOICE)
    await communicate.save(OUTPUT_FILE)
print("Audio created successfully!",OUTPUT_FILE)