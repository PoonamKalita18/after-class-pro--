class Shapes:
    def __init__(self):
        self.__rectangle = 100
    def area(self):
        print('selling price is : {}'.format(self.__rectangle))
    def setArea(self,Price):
        self.__rectangle = Price
c = Shapes()
c.area()
c.___rectangle = 300
c.area()
c.setArea(300)
c.area()
