import re

class classcollector:
    def __init__(self, scripts):
        self.scripts = scripts
        self.identifierExpression = "class |enum |interface "
        self.buildDependables()
        self.findDependancies()

    def buildDependables(self):
        self.dependables = dict()
        for script in self.scripts:
            search = re.search(self.identifierExpression, script)
            if(search):
                start = search.regs[0][1]
                end = self.findEndOfDependancyName(script, start)
                self.dependables[script[start:end]] = []
    
    def findEndOfDependancyName(self, currentScript, start):
        end = len(currentScript)
        for i in range(start, end):
            if(currentScript[i] == "(" or currentScript[i] == "{" or currentScript[i] == '\n' or currentScript[i] == ":"):
                return i

    def findDependancies(self):
        for scriptName in self.dependables.keys():
            print(f"{scriptName} depends on:")
            for script in self.scripts:
                search = re.search(scriptName, script)
                if(search):
                    currentScript = re.search(self.identifierExpression, script)
                    if(currentScript):
                        dependancyName = script[currentScript.regs[0][1]:self.findEndOfDependancyName(script, currentScript.regs[0][1])]
                        if(scriptName != dependancyName):
                            self.dependables[scriptName].append(dependancyName)
                            print(dependancyName)
