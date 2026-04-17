from .infrastructure_pygame import Infrastructure
from .snake import Snake
from .apple import *
from .const import *

class Game:
    def __init__(self, infrastructure: Infrastructure) ->None:
        self.infrastructure = infrastructure
        head = center_position()
        self.snake = Snake(head)
        self.apple = gen_apple(self.snake)
        self.tick_counter = 0
        self.snake_speed = SPEED_SNAKE
        self.is_running = True
        self.is_game_over = False
        self.score = 0


    def process_events(self) -> None:
        if self.infrastructure.tt():
            self.is_running = False
        new_dir = self.infrastructure.pressed_key()
        if new_dir is not None:
           self.snake.set_dir(new_dir) 

    def update_state(self) ->None:
        if self.is_game_over:
            return
        self.tick_counter += 1
        if self.tick_counter % self.snake_speed == 0:
            head = self.snake.get_new_head()
            if not good_head(head, self.snake):
                self.is_game_over = True
                return    
            self.snake.eneque(head)
            
            if head == self.apple:
                self.score += 1
                self.apple = gen_apple(self.snake)
            else:
                self.snake.dequeue()
        # else:
        #     self.is_game_over = True

    def render(self) -> None:
        self.infrastructure.fill_screen()
        for e in self.snake.body:
            self.infrastructure.draw_element(e, SNAKE_COLOR)
        self.infrastructure.draw_element(self.apple, APPLE_COLOR)
        self.infrastructure.draw_score(self.score)
        if self.is_game_over:
            self.infrastructure.draw_game_over()

        self.infrastructure.update_and_tick()

    def loop(self):
        while self.is_running:
            self.process_events()
            self.update_state()
            self.render()
        self.infrastructure.quit()