from typing import List


def main():
    A: List[int] = [1, 0, 0, 1, 1]
    B: List[int] = [0, 1, 1, 1, 0]
    n: int = len(A)
    C: List[int] = add_binary_integers(A, B, n)
    print(C)


def add_binary_integers(A: List[int], B: List[int], n: int) -> List[int]:
    a: int = 0
    b: int = 0
    for i in range(0, n):
        a += A[i] * 2 ** i
        b += B[i] * 2 ** i
    c: int = a + b
    C: List[int] = []
    for i in range(n, -1, -1):
        if 2 ** i <= c:
            C.insert(0, 1)
            c -= 2 ** i
        else:
            C.insert(0, 0)
    return C


if __name__ == '__main__':
    main()
