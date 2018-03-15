# coding: utf-8
from PIL import Image

class App:
    def __init__(self):
        self.__compositors = []


    def addCompositor(self, compositor):
        self.__compositors.append(compositor);


    def run(self):
        frame_image = Image.open(self.getBaseFilePath())
        for compositor in self.__compositors:
            compositor.composite(frame_image)
        self.__save(frame_image)


    def getBaseFilePath(self):
        return './image.jpg'


    def getOutputFilePath(self):
        return './tmp/output.jpg'


    def __save(self, frame_image):
        frame_image.save(self.getOutputFilePath())
        frame_image.show()
