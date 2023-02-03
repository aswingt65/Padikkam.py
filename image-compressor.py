import PIL
from PIL import Image
from tkinter.filedialog import *

file_path = askopenfilename()
Image = PIL.Image.open(file_path)
height, width = Image.size
Img = Image.resize((height,width), PIL.Image.ANTIALIAS)

Img.save(file_path+ "-compressed.jpg")