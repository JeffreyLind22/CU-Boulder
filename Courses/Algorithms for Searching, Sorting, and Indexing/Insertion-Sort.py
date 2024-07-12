from typing import List


def main():
    A: List[int | float] = [2, 1, 21, 67, 14, 189, 30, 30]
    n: int = len(A)
    increasing_result: List[float | int] = increasing_insertion_sort(A, n)
    print(f"Increasing Insertion Sort Result = {increasing_result}")

    A: List[int | float] = [2, 1, 21, 67, 14, 189, 30, 30]
    n: int = len(A)
    decreasing_result: List[float | int] = decreasing_insertion_sort(A, n)
    print(f"Decreasing Insertion Sort Result = {decreasing_result}")


def increasing_insertion_sort(array: List, n: int) -> List[float | int]:
    for i in range(1, n):
        key: int | float = array[i]
        j: int = i - 1
        while j >= 0 and array[j] > key:
            array[j + 1]: int | float = array[j]
            j -= 1
        array[j + 1]: int | float = key
    return array


def decreasing_insertion_sort(array: List, n: int) -> List[float | int]:
    for i in range(1, n):
        key: int | float = array[i]
        j: int = i - 1
        while j >= 0 and key > array[j]:
            array[j + 1]: int | float = array[j]
            j -= 1
        array[j + 1]: int | float = key
    return array


if __name__ == "__main__":
    main()
