import argparse

from src.simulation import run_simulation


def main(argv: list[str] | None = None) -> int:
    """
    Запускает CLI симуляции библиотеки
    :param argv: Аргументы командной строки
    :return: Код завершения
    """
    parser = argparse.ArgumentParser(
        prog="python -m src.main",
        description="Запуск симуляции библиотеки",
    )
    parser.add_argument("--steps", type=int, default=20, help="Количество шагов")
    parser.add_argument(
        "--seed", type=int, default=None, help="Сид для генератора случайных событий"
    )

    args = parser.parse_args(argv)

    run_simulation(steps=args.steps, seed=args.seed)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
