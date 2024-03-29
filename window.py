import os
import tkinter as tk
from folderscraper import folderscraper
from scriptanalytics import scriptanalytics
from classcollecter import classcollector
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
        self.window.tk.call('wm', 'iconbitmap', self.window._w, tk.PhotoImage(f'{os.getcwd()}\Assets\Icon.ico'))
        self.window.geometry(f'{x}x{y}+0+0')
        self.create_inputs()
        self.createRunButton()
        self.createAnalasysDropDown()
        self.createDebugLabel()

    def create_inputs(self):
        self.createEntriesandLabels()
        self.placeEntriesandLabels()

    def createEntriesandLabels(self):
        self.fpLabel = tk.Label(self.window, text="Folder Path")
        self.folderPath = tk.Entry(self.window)
        self.ftLabel = tk.Label(self.window, text="File Type")
        self.fileType =  tk.Entry(self.window)

    def createDebugLabel(self):
        self.debugLabel = tk.Label(self.window, text="Debug Text:")
        self.debugLabel.grid(row=0, column=4)
        self.debugText = tk.Label(self.window, text="", fg="#C00")
        self.debugText.grid(row=1, column=4)

    def setDebugText(self, dbgText):
        self.debugText.config(text = dbgText)

    def placeEntriesandLabels(self):
        self.fpLabel.grid(row=0,column=0)
        self.ftLabel.grid(row=0,column=1)
        self.folderPath.grid(row=1, column=0)
        self.fileType.grid(row=1,column=1)

    def createRunButton(self):
        self.runButton = tk.Button(self.window, text="Analyse", command=self.analyse)
        self.runButton.grid(row=1, column=2)

    def createAnalasysDropDown(self):
        dropOptions = ["Length","Dependancy"]
        self.dropValue = tk.StringVar(self.window)
        self.dropValue.set(dropOptions[0])
        self.dropBar = tk.OptionMenu(self.window, self.dropValue, *dropOptions)
        self.dropBar.grid(row=0,column=3)

    def analyse(self):
        self.setDebugText("Outliers not calculated")
        dropOption = self.dropValue.get()
        if dropOption == "Length":
            self.lengthAnalysis()
        elif dropOption == "Dependancy":
            self.dependancyAnalysis()

    def lengthAnalysis(self):
        scriptCollection = folderscraper(self.folderPath.get(), self.fileType.get())
        scriptCollection.collectAllFiles()
        scriptAnalyzer = scriptanalytics(scriptCollection.fileContents)
        df = pandas.DataFrame(scriptAnalyzer.linesOfCode)
        df.boxplot(column="Scripts", showfliers=False)
        pyplot.show()

    def dependancyAnalysis(self):
        scriptCollection = folderscraper(self.folderPath.get(), self.fileType.get())
        scriptCollection.collectAllFiles()
        collector = classcollector(scriptCollection.fileContents)
        self.setDebugText("Dependancy Not Implemented")
