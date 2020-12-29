import os, sys
import imageio
from PIL import Image
import fire
import PySimpleGUI as sg

#GUI
sg.ChangeLookAndFeel('Dark Blue 3')
form = sg.FlexForm('GIF-ifier', default_element_size=(40, 1))
column1 = [[sg.Text('Column 1', background_color='#d3dfda', justification='center', size=(10,1))],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 1')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 2')],
           [sg.Spin(values=('Spin Box 1', '2', '3'), initial_value='Spin Box 3')]]
layout = [
    [sg.Text('Images to GIF maker', size=(30, 1), font=("Helvetica", 25))],
    [sg.Text('Choose a folder of jobs you want made into a gif', size=(35, 1))],
    [sg.InputText(' '), sg.FolderBrowse()],
    [sg.Submit(), sg.Cancel()]
     ]

button, values = form.Layout(layout).Read()

#store the directory as a string
print(values["Browse"])

if values["Browse"]:
    #sg.Popup("Creating Gif...") <- If you want a popup
    print("Starting...")
else:
    print("Canceled.")
    exit()

form.close()

images = []

# Progress Bar Script
def printProgressBar (iteration, total, prefix = '', suffix = '', decimals = 1, length = 100, fill = '█', printEnd = "\r"):
    percent = ("{0:." + str(decimals) + "f}").format(100 * (iteration / float(total)))
    filledLength = int(length * iteration // total)
    bar = fill * filledLength + '-' * (length - filledLength)
    print(f'\r{prefix} |{bar}| {percent}% {suffix}', end = printEnd)
    # Print New Line on Complete
    if iteration == total: 
        print()


path_to_folder = values["Browse"]
files = len(os.listdir(path_to_folder))
items = list(range(0, files))
l = len(items)

# Initial call to print 0% progress
printProgressBar(0, l, prefix = 'Making GIF:', suffix = 'Complete', length = 50)
xx = 0

for imgFile in os.listdir(path_to_folder):
    if imgFile.endswith(('jpg', 'png')) and imgFile.startswith("S"):
        imgFilePath = path_to_folder + '/' + imgFile
        images.append(imgFilePath)
        #print(imgFile) <- current image
        im = Image.open(imgFilePath)
        imResize = im.resize((1200,675), Image.ANTIALIAS)
        imResize.save(imgFilePath, quality=10)
        xx += 1
        printProgressBar(xx, l, prefix = 'Optimizing Images:', suffix = 'Complete', length = 50)


pictures = len(os.listdir(path_to_folder))
number = 0
printProgressBar(0, l, prefix = 'Making GIF:', suffix = 'Complete', length = 50)
with imageio.get_writer(path_to_folder + "/Final_" + path_to_folder.split("/")[-1] + '.gif', mode='I', fps=24) as writer:
    for filename in images:
        number += 1
        printProgressBar(number, l, prefix = 'Converting to GIF:', suffix = 'Complete', length = 50)
        image = imageio.imread(filename)
        writer.append_data(image)

print("\nGIF is ready! It can be found in the same folder as your images.")