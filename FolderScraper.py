from os import listdir, walk
from os.path import isfile, join, isdir
from filehandler import filehandler

class folderscraper:
    def __init__(self, parentfolder):
        self.fileContents = []
        self.parentfolder = parentfolder

    def getFiles(self):
        return self.fileContents
    
    def addFile(self, fileName):
        self.fileContents.append(filehandler(fileName).getFileContents().strip())

    def getAllCSFiles(self, folderName : str):
        allFiles = [f for f in listdir(folderName) if isfile(join(folderName, f))]
        csFiles = [f for f in allFiles if f[-3:] == ".cs"]
        for filename in csFiles:
            fn = folderName.replace("C:/Users/ImHiP/Documents/GitHub/ArmOfSatan/Assets/Scripts/", "")
            print(f"{fn}/{filename}")
            self.addFile(f"{folderName}/{filename}")

    def getAllFolders(self):
        return [x[0] for x in walk(self.parentfolder)]

    def addFilesFromNestedFolders(self):
        for folder in self.getAllFolders():
            self.getAllCSFiles(folder.__str__().replace("\\", '/'))

    def collectAllFiles(self):
        #self.getAllCSFiles(self.parentfolder)
        self.addFilesFromNestedFolders()
        