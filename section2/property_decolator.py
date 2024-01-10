class Rectangle:
    def __init__(self, width: int, height: int):
        self._width = width
        self._height = height

    @property
    def width(self) -> int:
        return self._width

    @width.setter
    def width(self, value: int) -> None:
        if value < 0:
            raise ValueError("幅は0以上")
        self._width = value

    @property
    def height(self) -> int:
        return self._height


    def change_value(self, width, height) -> None:
        self._width = width
        self._height = height


rectangle = Rectangle(5, 3)
print(rectangle.width)

rectangle.width = 8
print(rectangle.width)

# rectangle.width = -2
# print(rectangle.width)

rectangle._width = 7
print(rectangle.width)

# だめ
rectangle._width = -2
print(rectangle.width)

rectangle.change_value(1, 2)
print(rectangle.width)
