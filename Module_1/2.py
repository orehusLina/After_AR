# Task 1
x = int(input())
y = int(input())
if x >= 5 and y < 25:
    print('True')
else:
    print('False')
# Input: 10 13
# Output: True


# Task 2
s1 = input()
s2 = input()
print(s1 == s2)
# Input:
# 8b66bBT67-NVbds8_23dlsa-02EcxjKseQ
# 8b66bBT67-NVbds8_23dIsa-02EcxjKseQ

# Output: False


# Task 3
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if a < b * a < c * a < d:
    print(a)
elif b < c * b < d:
    print(b)
elif c < d:
    print(c)
else:
    print(d)
# Input: 12, 10, 5, 21
# Output: 5


# Task 4
a = int(input())
b = int(input())
c = int(input())
d = int(input())
print(max(a, b, c, d))
# Input: 21 1 30 12
# Output: 30


# Task 5
a = int(input())
b = int(input())
c = int(input())
z = (a <= (b + c)) and (b <= (a + c)) and (c <= (a + b))
print(z == 1)
# Input: 13 19 15
# Output: True


# Task 6
a = int(input())
b = int(input())
c = int(input())
z = (a < (b + c)) and (b < (a + c)) and (c < (a + b))
if z == 0:
    print("Вырожденный")
else:
    if (a == b) and (b == c):
        print("Равносторонний")
    elif (a == b) or (b == c) or (a == c):
        print("Равнобедренный")
    else:
        print("Разносторонний")
# Input: 10 13 23
# Output: Вырожденный


# Task 7
a = int(input())
b = int(input())
c = int(input())
d = int(input())
if (a <= c) and (b >= c):
    print(b - c + 1)
elif (a >= c) and (d >= a):
    print(b - d + 1)
else:
    print(0)
# Input: 3 13 7 17
# Output: 7
