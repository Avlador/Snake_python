##Координаты для перемещения
class Element: 
    def __init__(self, x:int, y:int) -> None:
        self.x = x
        self.y = y


    def __eq__(self, value) -> bool:
        return self.x == value.x and self.y == value.y