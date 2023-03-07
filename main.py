from folderscraper import folderscraper
from scriptanalytics import scriptanalytics
import pandas
from matplotlib import pyplot

def main():
    running = True
    fs = folderscraper(input("Type folder Path "), input("Type folder extention (without the .) "))
    while(running):
        fs.collectAllFiles()
        sa = scriptanalytics(fs.fileContents)
        df = pandas.DataFrame(sa.linesOfCode)
        df.boxplot(column="Scripts")
        
        pyplot.show()
        running = False

if __name__ == "__main__":
    main()