from src.game import GamePong


def main() -> None:
    game = GamePong(1920, 1080)
    game.run()


if __name__ == "__main__":
    main()
