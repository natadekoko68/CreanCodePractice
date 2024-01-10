class Circle:
    __PI = 3.14

    def __init__(self, r):
        self.__r = r

    def length(self):
        return self.__r * 2 * Circle.__PI

    def __area(self):
        return self.__r**2 * Circle.__PI

circle = Circle(5)
print(circle._Circle__PI)
print(circle._Circle__r)
print(circle._Circle__area())