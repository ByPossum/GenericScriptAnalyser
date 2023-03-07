
class filehandler:
    def __init__(self, fileName):
        fs = open(fileName)
        self.file = fs.read()
        fs.close()

    def getFileContents(self):
        return self.file
