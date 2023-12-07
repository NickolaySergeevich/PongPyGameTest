from src.base_game_objects.base_game_objects import GameObjectRectangle


class Paddle(GameObjectRectangle):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int]) -> None:
        super().__init__(x, y, width, height, color)

        # Изначальная скорость движения.
        # Скорость движения будет равна 20% высоты.
        self.__speed = self._rect.height // 5

        # Для корректного движения.
        self.__real_y = self._rect.y

    def move(self, delta_time: float, ball_y: int) -> None:
        center_y = self._get_center()[1]

        if abs(center_y - ball_y) < self.__speed * delta_time:
            self.__real_y = ball_y - self._rect.height // 2
        elif center_y > ball_y:
            self.__real_y -= self.__speed * delta_time
        elif center_y < ball_y:
            self.__real_y += self.__speed * delta_time

        self._rect.y = int(self.__real_y)
