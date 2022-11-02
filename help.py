from rembg.bg import remove

import tkinter
from tkinter import filedialog
from rembg import remove
from tkinter import filedialog
root = tkinter.Tk()
root.withdraw()

input_path = filedialog.askopenfilename()


output_path = 'output.png'

with open(input_path, 'rb') as i:
    with open(output_path, 'wb') as o:
        input = i.read()
        output = remove(input)
        o.write(output)