import tkinter as tk
from folderscraper import folderscraper
from scriptanalytics import scriptanalytics
import pandas
from matplotlib import pyplot

class window:
    def __init__(self, x, y, title):
        self.createWindow(x, y, title)
        self.running = True
        self.window.protocol("WM_DELETE_WINDOW", self.close)

    def update(self):
        self.window.mainloop()

    def close(self):
        self.window.destroy()
        self.running= False

    def createWindow(self, x, y, title):
        self.window = tk.Tk()
        self.window.title(title)
        self.window.geometry(f'{x}x{y}+0+0')
        self.create_inputs()
        self.createRunButton()

    def create_inputs(self):
        self.createEntriesandLabels()
        self.placeEntriesandLabels()

    def createEntriesandLabels(self):
        self.fpLabel = tk.Label(self.window, text="Folder Path")
        self.folderPath = tk.Entry(self.window)
        self.ftLabel = tk.Label(self.window, text="File Type")
        self.fileType =  tk.Entry(self.window)

    def placeEntriesandLabels(self):
        self.fpLabel.grid(row=0,column=0)
        self.ftLabel.grid(row=0,column=1)
        self.folderPath.grid(row=1, column=0)
        self.fileType.grid(row=1,column=1)

    def createRunButton(self):
        self.runButton = tk.Button(self.window, text="Analyse", command=self.analyse)
        self.runButton.grid(row=1, column=2)

    def createAnalasysDropDown(self):
        dropOptions = ['Length','Dependancy']
        

    def analyse(self):
        scriptCollection = folderscraper(self.folderPath.get(), self.fileType.get())
        scriptCollection.collectAllFiles()
        scriptAnalyzer = scriptanalytics(scriptCollection.fileContents)
        df = pandas.DataFrame(scriptAnalyzer.linesOfCode)
        df.boxplot(column="Scripts")
        pyplot.show()
