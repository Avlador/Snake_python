# import pygame

# pygame.init()

# ##? Создание игрового окна
# screen = pygame.display.set_mode([640, 480]) 
# ##? Тики объектов 
# clock = pygame.time.Clock()

# ##! Цикл на запуск игры
# is_runing = True
# while is_runing:
#     ##! Цикл на обработу действия а точнее на выход из игры нажав на крестик
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             print('Вы вышли из игры')
#             is_runing = False
#     pygame.display.update()
#     clock.tick(60) ##? Кадры в сек


# pygame.quit()


from src.game import Game
from src.infrastructure_pygame import Infrastructure

if __name__ == "__main__":
    game = Game(Infrastructure())
    game.loop()
