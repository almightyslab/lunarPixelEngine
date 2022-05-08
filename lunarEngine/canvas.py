class Canvas():
    filleduni = "██"
    unfilleduni = "⠀⠀"
    def __init__(self, size):
        self.size = size
        self.rangesize = size*size
    def writepixels(self, pixeldict: dict):
        for i in range(self.rangesize):
            i = i+1
            pixelis = pixeldict[i]
            if pixelis == True:
                print(self.filleduni, end='', flush=True)
            else:
                print(self.unfilleduni, end='', flush=True)
            if i%self.size==0:
                print("")

    def flushpixels(self):
        print("")
                