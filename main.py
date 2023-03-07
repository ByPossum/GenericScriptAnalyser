from folderscraper import folderscraper
from scriptanalytics import scriptanalytics
import pandas
from matplotlib import pyplot

def main():
    running = True
    scriptCollection = folderscraper(input("Type folder Path "), input("Type folder extention (without the .) "))
    while(running):
        scriptCollection.collectAllFiles()
        scriptAnalyzer = scriptanalytics(scriptCollection.fileContents)
        df = pandas.DataFrame(scriptAnalyzer.linesOfCode)
        df.boxplot(column="Scripts")
        
        pyplot.show()
        running = False

if __name__ == "__main__":
    main()