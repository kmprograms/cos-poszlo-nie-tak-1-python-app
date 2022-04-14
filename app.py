from typing import List

def add_numbers(numbers: List[int]) -> int:
    """

    :param numbers:
    :return:
    """
    return sum(numbers)

def main() -> None:
    print(add_numbers([1, 2, 3]))

if __name__ == '__main__':
    main()