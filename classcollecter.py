import re

class classcollector:
    def __init__(self, scripts):
        self.scripts = scripts
        self.identifierExpression = "class |enum |interface "
        self.buildDependables()
        self.findDependancies()
        self.debugDependables()

    def buildDependables(self):
        self.scriptNames = dict()
        for script in self.scripts:
            search = re.search(self.identifierExpression, script)
            if(search):
                start = search.regs[0][1]
                end = self.findEndOfDependancyName(script, start)
                self.scriptNames[script[start:end]] = script
    
    def findEndOfDependancyName(self, currentScript, start):
        end = len(currentScript)
        for i in range(start, end):
            if(currentScript[i] == "(" or currentScript[i] == "{" or currentScript[i] == '\n' or currentScript[i] == ":"):
                return i

    def findDependancies(self):
        self.dependancies = dict()
        for currentScript in self.scriptNames.keys():
            self.dependancies[currentScript] = []
            for otherScript in self.scriptNames.keys():
                if(otherScript != currentScript):
                    match = re.search(otherScript, self.scriptNames[currentScript])
                    if(match):
                        self.dependancies[currentScript].append(otherScript)

    def debugDependables(self):
        for currentClass in self.scriptNames.keys():
            print(f"{currentClass} depends on:")
            for currentDependants in self.dependancies[currentClass]:
                print(currentDependants)
