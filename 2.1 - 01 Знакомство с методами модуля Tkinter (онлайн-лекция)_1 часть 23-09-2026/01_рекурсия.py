# def num2(n: int) -> None:
#     if n > 1:
#         num2(n -1)
#     print(n)
#
# def num1(n: int) -> None:
#     if n > 1:
#         num2(n -1)
#     print(n)

def num(x, n: int) -> None:
    if n > x:
        num(x, n -1)
    print(n)


num(4, 15)

print("-" * 5)


def factorial(n: int) -> int:
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial(5))