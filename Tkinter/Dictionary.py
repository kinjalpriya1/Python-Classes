from tkinter import *
import requests

URL = "https://api.dictionaryapi.dev/api/v2/entries/en/"

window = Tk()

window.geometry("400x600")
window.title("K Dictionary")
window.config(bg = "#133463")

headerFrame = Frame(window, bg = "#0D2242")
headerFrame.pack(side = TOP, fill = X)

footerFrame = Frame(window, bg = "#0D2242")
footerFrame.pack(side = BOTTOM, fill = X)

inputFrame = Frame(window, bg = "#1E4377")
inputFrame.pack(side = TOP, fill = BOTH)

infoFrame = Frame(window, bg = "#1E4377")
infoFrame.pack(side = TOP, fill = BOTH, expand = True)

titleLabel = Label(headerFrame, text = "K DICTIONARY", font = ("Arial", 22), bg = "#0D2242", fg = "White")
titleLabel.pack(pady = 20)

footerLabel = Label(footerFrame, text = "By Kinjal Priyadarshini", font = ("Arial", 16), bg = "#0D2242", fg = "White")
footerLabel.pack(pady = 10) 

input = Entry(inputFrame, text = "Word", font = ("Arial", 16), bg = "#A7A8AA", fg = "White", justify = "center")
input.pack(pady = (35, 10)) 



typeLabel = Label(infoFrame, text="", bg = "#1E4377", fg = "White")
typeLabel.pack(pady = (20, 10))

defLabel = Label(infoFrame, text="", bg = "#1E4377", fg = "White")
defLabel.pack(pady = (20, 10))

exampleLabel = Label(infoFrame, text="", bg = "#1E4377", fg = "White")
exampleLabel.pack(pady = (20, 10))

soundLabel = Label(infoFrame, text="", bg = "#1E4377", fg = "White")
soundLabel.pack(pady = (20, 10))



def findWordInfo():
    word = input.get().strip().lower()
    parameters = {
        "q": word, 
        
    }
    response = requests.get("https://api.dictionaryapi.dev/api/v2/entries/en/{word}")
    data = response.json()
    print(data)

    defLabel.config(text = f"Definition: {data[0]["meanings"][0]["definitions"][0]["definition"]}")

 


#http: supports get, post, put, delete

submit = Button(inputFrame, text = "Submit", font = ("Arial", 16), bg = "#0D2242", fg = "White", command = findWordInfo)
submit.pack(pady = 10) 



window.mainloop() 