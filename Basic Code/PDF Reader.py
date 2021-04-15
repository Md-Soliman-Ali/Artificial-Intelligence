import pyttsx3
import PyPDF2

book = open("AI.pdf","rb")
pdfreader = PyPDF2.PdfFileReader(book)

pcb = pyttsx3.init()
for num in range(0,5):
    page = pdfreader.getPage(num)
    text = page.extractText()
    pcb.say(text)
    pcb.runAndWait()
    