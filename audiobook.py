import pyttsx3
import PyPDF2

# Import the pdf text file.
book = open('resources/sample.pdf', 'rb')

# Create the pdf-reader
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
# Print the total pages of the pdf-file; we need it, when we want to read in a range.
print(pages)

# Initialize the text-to-speech engine
speaker = pyttsx3.init()
page = pdfReader.getPage(1) # Will start from the second page

# Extract all the text from the specifies page(s)
txt = page.extractText()
# Make the engine ready to speak out the texts loud
speaker.say(txt)
# The speaker will start speaking out the text of the pdf file
speaker.runAndWait()
