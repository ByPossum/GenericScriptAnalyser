class scriptanalytics:
    def __init__(self, scripts):
        self.scripts = scripts
        self.linesOfCode = {"Scripts" : self.countLinesOfCode()}

    def countLinesOfCode(self):
        lines = []
        for script in self.scripts:
            script = self.removeBracingAndWhiteSpace(script)
            lines.append(script.count('\n'))
        return lines
    
    def removeBracingAndWhiteSpace(self, script):
        actualCode = ""
        for line in script.split('\n'):
            if self.checkLineIsNotEmpty(line):
                actualCode+=line+'\n'
        print(actualCode)
        return actualCode

    def checkLineIsNotEmpty(self, line):
        if len(line.strip()) <= 0:
            return False
        elif '{' in line or '}' and len(line.strip()) == 1:
            return False
        return True
    