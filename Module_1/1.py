def main():
    task_1()
    task_2()
    task_3()
    task_4()
    task_5()
    task_6()


def task_1():
    a = input()
    b = input()
    c = input()
    print(a + b + c)


def task_2():
    a = int(input())
    b = int(input())
    res = 2 ** 8 * a ** 8 - 2 ** 4 * a ** 4 + 2 ** 2 * a ** 2 - 2 * b + 1 / 2 * b ** 0.5 + (a * b ** (b + a)) / 2
    print(res)
    # Input: 2 9
    # Output: 65378.5


def task_3():
    a = input()
    b = input()
    print(a + b, end="!")
    # Input: 2 3
    # Output: 23!


def task_4():
    a = int(input())
    b = int(input())
    c = int(input())
    print('(', end='')
    print(a, b, sep=' + ', end=' - ')
    print(c, ') % 10', sep='', end=' = ')
    print((a + b - c) % 10)
    # Input: 123 456 789
    # Output: (123 + 456 - 789) % 10 = 0


def task_5():
    x = int(input())
    print(x + 1, x - 1, sep='')
    # Input: 24
    # Output: 2523


def task_6():
    print("Centimeters: ")
    x = int(input())
    print("Kilometers: ", x // 100000)
    # Input: 123456789
    # Output: 1234


if __name__ == "__main__":
    main()
