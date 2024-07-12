from typing import List


def main():
    array: List[int | float] = [2, 1, 73, 6, 25]
    length_of_array: int = len(array)
    result = selection_sort(array, length_of_array)
    print(result)


def selection_sort(A: List[int | float], n: int) -> List[int | float]:
    for i in range(0, n):
        minimum: int | float = A[i]
        minimum_arg: int = i
        j = i + 1
        while j < n:
            if minimum > A[j]:
                minimum = A[j]
                minimum_arg = j
            j += 1
        A[minimum_arg] = A[i]
        A[i] = minimum
    return A


if __name__ == '__main__':
    main()
