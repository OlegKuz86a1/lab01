"""CLI-утилита для приветствия пользователя с поддержкой формального стиля."""

# Импортируем typer для создания CLI с автогенерацией справки и валидацией типов аргументов
import typer

def main(
    name: str,
    lastname: str = typer.Option("", help="Фамилия пользователя."),
    formal: bool = typer.Option(False, "--formal", "-f", help="Использовать формальное приветствие."),
) -> None:
    """
    Выводит приветствие на основе переданных аргументов.

    :param name: Имя пользователя (обязательный позиционный аргумент)
    :param lastname: Фамилия пользователя (опционально)
    :param formal: Флаг переключения на формальный стиль
    """
    if formal:
        print(f"Добрый день, {name} {lastname}!")
    else:
        print(f"Привет, {name}!")

if __name__ == "__main__":
    typer.run(main)
