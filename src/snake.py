from collections import deque
from .coordinate import Element
from .directions import Directions
##! Наша змейка текущий вектор движения
class Snake:
    def __init__(self, head: Element) -> None:
        self.body = deque() ##? deque - это как бы метод который позволяет сделать очередь
                                 ##? элементов (а элементы это части нашей змеки)
                                 ##? если голова змеи идет в низ то в перед добавится эелемент а в конце змейки этот элемент удалится
        self.body.appendleft(head)
        self.directions = Directions.RIGHT
    ##! Функция для изменения направления при нажатии на стрелки и запрещая разворот на 180 
    def set_dir(self, new_dir: Directions) -> None:
        if new_dir == Directions.UP and self.directions != Directions.DOWN:
            self.directions = new_dir
        elif new_dir == Directions.DOWN and self.directions != Directions.UP:
            self.directions = new_dir
        elif new_dir == Directions.LEFT and self.directions != Directions.RIGHT:
            self.directions = new_dir
        elif new_dir == Directions.RIGHT and self.directions != Directions.LEFT:
            self.directions = new_dir

    ## Функции съедания яблочка и передвижения
    def eneque(self, head:Element) -> None:
        self.body.appendleft(head)
    ## Голова
    def dequeue(self) -> None:
        if len(self.body) > 1: # Удаляем хвост только если в змейке больше 1 сегмента
            self.body.pop()

    ##! Проверка передвижения если в верх то +1 элемент выше
    def get_new_head(self) -> Element:
        head = self.body[0] ## Текущая голова
        if self.directions == Directions.UP:
            return Element(head.x, head.y - 1)
        if self.directions == Directions.RIGHT:
            return Element(head.x + 1, head.y)
        if self.directions == Directions.DOWN:
            return Element(head.x, head.y + 1)
        if self.directions == Directions.LEFT:
            return Element(head.x -1, head.y)
        

    ##! Функция проверки что элемент находится на змейке
    def is_el(self, e: Element) -> bool:
        try:
            self.body.index(e)
            return True
        except ValueError:
            return False
