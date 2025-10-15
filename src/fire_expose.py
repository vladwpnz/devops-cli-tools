# src/fire_expose.py
import fire
import utils

def main():
    """
    Fire-CLI для швидкого доступу до існуючих функцій.

    Приклади:
      python src/fire_expose.py greet Alice
      python src/fire_expose.py goodbye Bob

    Допомога:
      python src/fire_expose.py --help
      python src/fire_expose.py greet --help
    """
    # можна віддати цілий модуль — Fire зробить з нього дерево команд
    fire.Fire({
        "greet": utils.greet,
        "goodbye": utils.goodbye,
    })

if __name__ == "__main__":
    main()