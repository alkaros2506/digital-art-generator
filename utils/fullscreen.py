import sys
from time import sleep

import tkinter
from PIL import Image, ImageTk


def showPIL(pilImage):
    root = tkinter.Tk()
    w, h = root.winfo_screenwidth(), root.winfo_screenheight()
    root.overrideredirect(1)
    root.geometry("%dx%d+0+0" % (w, h))
    root.focus_set()
    root.bind("<Escape>", lambda e: (e.widget.withdraw(), e.widget.quit()))
    canvas = tkinter.Canvas(root, width=w, height=h)
    canvas.pack()
    canvas.configure(background="black")
    imgWidth, imgHeight = pilImage.size
    if imgWidth > w or imgHeight > h:
        ratio = min(w / imgWidth, h / imgHeight)
        imgWidth = int(imgWidth * ratio)
        imgHeight = int(imgHeight * ratio)
        pilImage = pilImage.resize((imgWidth, imgHeight))
    image = ImageTk.PhotoImage(pilImage)
    imagesprite = canvas.create_image(w / 2, h / 2, image=image)
    # root.mainloop()
    sleep(5)


if __name__ == "__main__":
    pilImage = Image.open(
        "/Users/alkis/Desktop/Screenshot 2023-07-03 at 9.24.14 AM.png"
    )
    showPIL(pilImage)
