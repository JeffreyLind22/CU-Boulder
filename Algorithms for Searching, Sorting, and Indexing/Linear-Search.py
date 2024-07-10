from typing import List


def main():
    array: List[int | float] = [2, 5, 42, 6, 1]
    number_of_elements: int = len(array)
    key: int = 234
    result: int | float | None = linear_search(array, number_of_elements, key)
    print(result)


def linear_search(a: List[int | float], n: int, x: int | float):
    for i in range(0, n):
        if x == a[i]:
            return i
    return None


if __name__ == '__main__':
    main()
