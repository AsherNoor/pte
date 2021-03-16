"""
----------------------------
| PTE (PDF Text Extractor) |
----------------------------
By: [bini-tek]\\
Email: binitek.baltimore@gmail.com
Discord: Home of bini-tek (https://discord.gg/4GqDrH)




----------------
Version 001.
July\23\2020.
----------------




---------------
| EXPLANATION |
---------------
PTE simply reads a PDF file, extracts the text, and inputs it in a text file.
In this version, it is able to print out ASCII (English) letters.
It recognizes UNICODE, but it does not print it out correctly.
This is a work in progress.




----------------
| CONTRIBUTORS |
----------------
@Phaseit, Inc : for the PyPDF2 tool.
@ryn0f1sh: coder.
@50DD : coder.


"""


import sys
from os import system, name
from subprocess import call
from PyPDF2 import PdfFileReader, PdfFileWriter
from time import sleep
import codecs

'''------------------
DEFINING MY FUNCTIONS
---------------------'''

# The Intro function
#-------------------
def intro():
    print("\n---------------------"
          "\nP.T.E."
          "\nPDF Text Extractor."
          "\nBy: [bini-tek]\\\\"
          "\nVersion: 001"
          "\n---------------------\n")
    sleep(2)
    extractor() # calling the extractor function.


''' THE TEXT EXTRACTOR STARTS HERE '''
# Define the extractor() function
#--------------------------------
def extractor():
    print("\n----------"
          "\nIMPORTANT "
          "\n----------"
          "\nPlease make sure that P.T.E. & and your PDF file(s) are in the same file/folder location."
          "\n-----------------------------------------------------------------------------------------\n")
    sleep(3)

    '''--------------------- 
    The User Input Section 
    ----------------------'''
    # User Input : Name of the PDF file.
    ui_PDFFileName = str(input("Enter the PDF file name without the '.pdf': "))

    # User Input : Name of the TXT file.
    ui_TextFileName = str(input("Enter the output TEXT file name without the '.txt.': "))



    '''-------------------------------- 
    The PDF info extraction Section 
    --------------------------------'''
    # Opening the PDF file
    PDFfile = open(ui_PDFFileName+".pdf", "rb")
    # Reading the PDF file
    pdfread = PdfFileReader(PDFfile, strict=False)

    # Get the number of pages of this file.
    num_of_pages = pdfread.numPages
    print("\nOne moment, reading", ui_PDFFileName)
    sleep(2)
    print("\nThe page count is: ", num_of_pages)
    sleep(3)



    '''------------------------------------------ 
    The TEXT file creation & appending section 
    ------------------------------------------'''
    # A While loop to extract the whole file.
    i = 0
    while i < num_of_pages:
        pageinfo = pdfread.getPage(i)
        txt = pageinfo.extractText()

        #Encode the txt to utf-8 (converts bytes to string)
        encoded = txt.encode("utf-8")

        # Write to a text file & close text file
        text_file = open(ui_TextFileName + ".txt", "a")
        text_file.write("Page: "+str(i+1)+"\n"+str(encoded)+"\n"*2)
        text_file.close()
        i += 1


    '''-----------------------------------------------
    The Final message that the process is complete 
    ------------------------------------------------'''
    print("\nCreating your output text file, please wait.")
    sleep(2)
    print("\nYour output text file has been created.")

    ''' END OF EXTRACTOR FUNCTION '''


# The Main While Function
#------------------------
def main_while_function():

    while True:
        while_answer = str(input("\nHave another file? [y/n]: ").lower().strip())
        if while_answer == "y":
            #Calling the extractor function.
            extractor()
            continue
        #elif while_answer == "n":
        #    print("You typed [n], looping\n")
        else:
            print("\nExiting PTE, please wait. \n\n"
                  "\n-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-"
                  "\nBrought to you by: [bini-tek]\\\\"
                  "\nEmail: binitek.baltimore@gmail.com"
                  "\nDiscord: Home of bini-tek (https://discord.gg/4GqDrH)"
                  "\n-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-\\-")
            sleep(2)
            print("\n\nThank You for using P.T.E.")
            sleep(1)
            print(input("Press any key to exit."))
            exit()




'''------------------
CALLING THE FUNCTIONS
----------------------'''
#Calling the Functions
intro()
main_while_function()









"""
-------------------
| The Scratch Pad |
-------------------
Slices of codes that was not used.
----------------------------------

#This is only to display it on the screen.
print("The while extract \n", encoded).




"""