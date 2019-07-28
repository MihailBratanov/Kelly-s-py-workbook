#Url we shall be scraping from

base_url="https://www.lexico.com/en/definition/"

#imports of libraries we will use

from tkinter import *
import requests
import re
from bs4 import BeautifulSoup




#This is a function to remove the html tags from the definition
def cleanup(definition):
    regex = "<.*?>"
    final_definition = re.sub(regex, '', str(definition))
    return final_definition

#main function to lookup definition,creates the window and after typing the word the button press
#sends it over to the createdefinition function where magic happens
def lookup():
    defLookUpgui = Toplevel(root)
    defLookUpgui.title("Look it up!")
    actual_word = StringVar()

    wordBox = Entry(defLookUpgui, text='Insert word', textvariable=actual_word).pack()
#here is where magic happens,soup is created and then filtered down to a definition.
    def createdefinition():

        definition_name = actual_word.get()
        #print(type(definition_name))
        page = requests.get(base_url + definition_name)
        soup = BeautifulSoup(page.content, 'html.parser')
        definition_line = soup.find('span', {"class": "ind"})
#creates the window where definitions are displayed
        new = cleanup(definition_line)
        if new != " ":
            definition_gui = Toplevel()
            definition_gui.title("Definition:")
            definitionText = Label(definition_gui, text=new, height=20)
            definitionText.pack()

    searchButton = Button(defLookUpgui, text="Look up", command=createdefinition)
    searchButton.pack()
#root of the application, the base of all bases, the beginning
root = Tk()
root.title("Kelly's workbook")
label1 = Label(root, text="Welcome to Kelly's workbook")
label1.pack()
lookup_button = Button(root, text="Search definitions", command=lookup)


lookup_button.pack()
#the loop of life
root.mainloop()