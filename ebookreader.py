#import pypdf 
from pypdf import PdfReader
from gtts import gTTS
'''Reading a text from a PDF file '''
reader = PdfReader("python_intro.pdf")#Reads the content of the pdf to reader and stores it
text=""
for page in reader.pages:#Reads eacha and every page till last page of PDF
     content = page.extract_text()#Ectracts only text information from the PDF using the extract_text() function
     if content:# Checks whether any information in the pdf file or not 
        text += content#If it found any text in reader it will add to text
#print(text)# we can see the text information in PDF
'''Convet the text to Audio and save'''
txt_to_speach = gTTS(text, lang="en")#Object created for class gtts and passed the parametrs to conver to audio
txt_to_speach.save("Python_intro.mp3")#the audio which is in txt_to_speach is saved to in current dirrectory
print("Audio file saved in current directory as 'Python_intro.mp3'")

