import pygame

from src.game_objects.ball import Ball
from src.game_objects.paddle import Paddle


class GamePong:
    def __init__(self, screen_width: int, screen_height: int) -> None:
        # Инициализируем PyGame.
        pygame.init()

        # Инициализируем окно игры.
        self.__screen_width = screen_width
        self.__screen_height = screen_height
        self.__screen = pygame.display.set_mode((self.__screen_width, self.__screen_height))
        self.__screen_bg_color = (0, 0, 0)

        # Инициализируем игровые объекты.
        # Размер мяча -- одна пятидесятая в радиусе по ширине окна.
        self.__ball = Ball(self.__screen_width // 50, self.__screen_width, self.__screen_height, (255, 255, 255))
        # Высота палочки -- 40% от высоты экрана.
        # Ширина палочки -- 2% от ширины экрана.
        self.__paddle_left = Paddle(
            0, int(self.__screen_height * 0.4),
            self.__screen_width // 50, int(self.__screen_height * 0.4),
            (255, 255, 255)
        )
        self.__paddle_right = Paddle(
            0, int(self.__screen_height * 0.4),
            self.__screen_width // 50, int(self.__screen_height * 0.4),
            (255, 255, 255)
        )
        # Двигаем правую палочку к правой стороне.
        self.__paddle_right.set_x(self.__screen_width - self.__paddle_right.get_width())

        # Инициализируем состояние игры.
        self.__is_running = True
        self.__score_left = 0
        self.__score_right = 0

        # Учёт времени с предыдущего кадра.
        self.__fps = 60
        self.__clock = pygame.time.Clock()

    def __del__(self) -> None:
        pygame.quit()

    def run(self) -> None:
        while self.__is_running:
            # Проверяем события кадра.
            self.__check_events()
            # Двигаем игровые объекты.
            self.__move()
            # Проверяем логику игры.
            self.__check_logic()
            # Отрисовываем кадр.
            self.__draw()

    def __check_events(self) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.__is_running = False

    def __move(self) -> None:
        # Получаем время с предыдущего кадра.
        delta_time = self.__clock.tick(self.__fps) / 1000

        # Двигаем игровые объекты.
        self.__ball.move(delta_time)
        self.__paddle_left.move(delta_time, self.__ball.get_y())
        self.__paddle_right.move(delta_time, self.__ball.get_y())

    def __check_logic(self) -> None:
        if self.__ball.check_left_paddle_collision(self.__paddle_left) or\
                self.__ball.check_right_paddle_collision(self.__paddle_right):
            self.__ball.invert_move_x()
            self.__ball.speed_up()

    def __draw(self) -> None:
        self.__screen.fill(self.__screen_bg_color)
        self.__ball.draw(self.__screen)
        self.__paddle_left.draw(self.__screen)
        self.__paddle_right.draw(self.__screen)

        pygame.display.update()
