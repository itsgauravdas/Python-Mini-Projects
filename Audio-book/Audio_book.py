#Importing Google Text to Speech library
from gtts import gTTS
#Importing PDF reader PyPDF2
import PyPDF2
import  os

os.chdir(os.getcwd())
#open the file
try:
    pdf_file = open('name1.pdf','rb')
except FileNotFoundError:
    print("File not found")

#Create PDF reader object
pdf_reader = PyPDF2.PdfReader('NAME.pdf')
count = len(pdf_reader.pages) #count number of pages in pdf
teXt_list = []
print(count)
#Extracting the text data from each page of the pdf
for i in range(count):
    try:
        page = pdf_reader.getPage(i)
        print(page.extract_text())
        text_list.append(page.extractText())
    except :
        print("Page does not exist")


#converting the multiline text to single line text
textString = "".join(teXt_list)
print(textString)

# set language to english
language = 'en'

#call gtts
try:
    myAudio = gTTS(text=textString,lang=language,slow=False)
    # save the file
    myAudio.save("audio.mp3")
except Exception as e:
    print(e)






