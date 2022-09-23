!python detect.py --weights runs/train/exp2/weights/best.pt --img 640 --conf 0.25 --source data/images/phoi6.jpg
from importlib.resources import open_binary
from tkinter.ttk import  Frame, Button, Style
from PIL import Image, ImageTk
import os
from tkinter import filedialog, Tk, Label, RAISED, BOTH, RIGHT

def openBrowser():
    file = filedialog.askopenfilename()
    #dir = filedialog.askdirectory()
    global filepath 
    filepath = os.path.abspath(file)
    #print(str(filepath))
    img = Image.open(filepath)
    imgg = ImageTk.PhotoImage(img)
    label1 = Label(image=imgg)
    label1.image = imgg
    label1.grid(x=20, y=20)
   

class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.initUI()
    #def clickOK():
!python detect.py --weights runs/train/exp2/weights/best.pt --img 640 --conf 0.25 --source data/images/phoi6.jpg
    


    def initUI(self):
        self.parent.title("Nhan dien cam xuc khuon mat")
        self.style = Style()
        self.style.theme_use("default")
        frame = Frame(self, relief=RAISED, borderwidth=1)
        frame.pack(fill=BOTH, expand=True)
        self.pack(fill = BOTH, expand = 1)

        closeButton = Button(self, text="Close", command= self.quit)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        okButton = Button(self, text="OK")
        okButton.pack(side=RIGHT, padx=5, pady = 5)

        okBrowser = Button(self, text="Browser", command = openBrowser)
        okBrowser.pack(side=RIGHT, padx=5, pady=5)

        
        
    

  
 
root = Tk()
root.geometry("1200x800+100+100")
app = Example(root)
root.mainloop()