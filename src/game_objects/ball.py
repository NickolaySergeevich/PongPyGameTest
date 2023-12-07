import random
import pygame
from src.game_objects.paddle import Paddle
from src.base_game_objects.base_game_objects import GameObjectCircle


class Ball(GameObjectCircle):
    def __init__(self, radius: int, screen_width: int, screen_height: int, color: tuple[int, int, int]) -> None:
        super().__init__(screen_width // 2, screen_height // 2, radius, color)

        # Движение
        # Вектор движения.
        if random.randint(0, 1):  # 50% на 50%, что двигаться будет либо вправо, либо влево.
            self.__move_vector = pygame.Vector2(1, random.uniform(-1, 1))  # При этом движение по вертикали рандомное.
        else:
            self.__move_vector = pygame.Vector2(-1, random.uniform(-1, 1))
        self.__move_vector = self.__move_vector.normalize()  # Нормализация длины вектора.
        # Повешение скорости.
        self.__speed_up = random.randint(5, 50)
        # Изначальная скорость движения.
        self._speed = 100

    def invert_move_x(self) -> None:
        self.__move_vector.x *= -1

    def speed_up(self) -> None:
        self._speed += self.__speed_up

    def move(self, delta_time: float) -> None:
        self._x += self.__move_vector.x * self._speed * delta_time
        self._y += self.__move_vector.y * self._speed * delta_time

    def check_left_paddle_collision(self, paddle: Paddle) -> bool:
        return self._x - self._radius <= paddle.get_x() + paddle.get_width() and\
            self._y >= paddle.get_y() and self._y <= paddle.get_y() + paddle.get_height()

    def check_right_paddle_collision(self, paddle: Paddle) -> bool:
        return self._x + self._radius >= paddle.get_x() and\
            self._y >= paddle.get_y() and self._y <= paddle.get_y() + paddle.get_height()
