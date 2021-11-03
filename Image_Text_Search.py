from  tkinter import *
from tkinter import filedialog
import os
import pytesseract as tess
from PIL import Image
tess.pytesseract.tesseract_cmd = r'C:/Users/Legion/AppData/Local/Programs/Tesseract-OCR/tesseract.exe'


root = Tk()
pathy = filedialog.askdirectory()
path = pathy+'/'
root.destroy()


def pictureout():
    print("Found at {}".format(files))
    print('Please Wait while we show you the picture')
    img.show(path,'{}'.format(files))
    


a = input("Enter what you want to search: ")
flag = False
try:
    for files in os.listdir(path):
        fp = path+files
        img = Image.open(fp)
        text = tess.image_to_string(img)
        if a in text.split():
            flag = True
            pictureout()
        elif a.upper() in text.split():
            flag = True
            pictureout()
        elif a.lower() in text.split():
            flag = True
            pictureout()
        elif a.title() in text.split():
            flag = True
            pictureout()

    else:
        if flag == False:
                print("{} was not found".format(a))
except:
    print("Small Error")
    exit()                