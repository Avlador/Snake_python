from .snake import Snake
from .coordinate import Element
from random import randrange
from .const import *
def random() -> Element:
    return Element(randrange(0, WIDTH), randrange(0, HEIGHT))
##! Генерация яблока
def gen_apple(snake: Snake):
    candidate = None
    while candidate is None:
        candidate = random()
        if snake.is_el(candidate):
            candidate = None
    return candidate


##! Ищим центр поля для начальной позиции
def center_position() -> Element:
    return Element(WIDTH //2, HEIGHT//2)

##? Проверка что элемент внутри поля
def pp(e:Element) -> bool:
    return 0 <= e.x < WIDTH and 0 <= e.y < HEIGHT



def good_head(head:Element, snake:Snake) -> bool:
    return pp(head) and not snake.is_el(head) ## голова внутри поля и не на змейке
