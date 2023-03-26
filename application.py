from window import window

class application:
    def __init__(self):
        self.running = True
        self.window = window(800, 900, 'Generic Script Analyser')
    
    def step(self):
        self.check_quit()


    def check_quit(self):
        if self.window.running != False:
            self.window.update()
        else:
            quit()

    def quit(self):
        self.running = False
        self.window.close()
