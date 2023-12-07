import pygame


class GameObject:
    def __init__(self, color: tuple[int, int, int]) -> None:
        self._color = color

        self._speed = int()

    def move(self, delta_time: float) -> None:
        pass

    def draw(self, screen: pygame.Surface) -> None:
        pass


class GameObjectCircle(GameObject):
    def __init__(self, x: int, y: int, radius: int, color: tuple[int, int, int]) -> None:
        super().__init__(color)

        self._x = x
        self._y = y
        self._radius = radius

    def get_y(self) -> int:
        return self._y

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.circle(screen, self._color, (self._x, self._y), self._radius)


class GameObjectRectangle(GameObject):
    def __init__(self, x: int, y: int, width: int, height: int, color: tuple[int, int, int]) -> None:
        super().__init__(color)

        self._rect = pygame.Rect(x, y, width, height)

    def _get_center(self) -> tuple[int, int]:
        return self._rect.center

    def set_x(self, x: int) -> None:
        self._rect.x = x

    def get_x(self) -> int:
        return self._rect.x

    def get_y(self) -> int:
        return self._rect.y

    def get_width(self) -> int:
        return self._rect.width

    def get_height(self) -> int:
        return self._rect.height

    def draw(self, screen: pygame.Surface) -> None:
        pygame.draw.rect(screen, self._color, self._rect)
