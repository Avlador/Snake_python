from __future__ import annotations
import pygame
from .const import *
from .directions import Directions
from .coordinate import Element
class Infrastructure:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode([WIDTH * SCALE, HEIGHT * SCALE])
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font(None, SCALE)
    

    def tt(self) -> bool:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print('Вы вышли из игры')
                return  True
        return False
    
    ## Какие кнопки нажаты
    def pressed_key(self) -> Directions | None:
        key = pygame.key.get_pressed()
        if key[pygame.K_UP]:
            return Directions.UP
        if key[pygame.K_RIGHT]:
            return Directions.RIGHT
        if key[pygame.K_LEFT]:
            return Directions.LEFT
        if key[pygame.K_DOWN]:
            return Directions.DOWN
        return None
    

    def fill_screen(self) -> None:
        self.screen.fill (SCREEN_COLOR)


    def draw_element(self, e:Element, color) -> None:
        pygame.draw.rect(
        self.screen,
        pygame.Color(color),
        (e.x * SCALE, e.y * SCALE, ELEMENT_SIZE, ELEMENT_SIZE),
        0,
        EL_RADIUS
        )


    def draw_score(self, score: int) -> None:
        self.screen.blit(
            self.font.render(f"Score: {score}", True, pygame.Color(SCORE_COLOR)),
            (5,5)
        )


    def draw_game_over(self) -> None:
        message = self.font.render("Проиграл ХА ХА", True, pygame.Color(GAME_OVER_COLOR))
        self.screen.blit(
            message,
            message.get_rect(center = ((WIDTH //2) * SCALE, (HEIGHT// 2) * SCALE)))
        


    def update_and_tick(self) -> None:
        pygame.display.update()
        self.clock.tick(60)

    def quit(self) -> None:
        pygame.quit()
