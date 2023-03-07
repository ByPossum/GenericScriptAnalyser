class scriptanalytics:
    def __init__(self, scripts):
        self.scripts = scripts
        self.linesOfCode = {"Scripts" : self.countLinesOfCode()}

    def countLinesOfCode(self):
        lines = []
        for script in self.scripts:
            lines.append(script.count('\n'))
        return lines