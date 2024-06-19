class IOState:
    def __init__(self, input, output):
        self.__input = input
        self.__output = output


    @property
    def input(self):
        return self.__input
    
    @property
    def output(self):
        return self.__output