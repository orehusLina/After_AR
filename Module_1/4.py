# Task 1
# Answer: 2 2 2

# Task 2
# Answer: 5

# Task 3
n = int(input())
a = []
x = 0

for i in range(n):
    x = int(input())
    a.append(x)

s = 0
for i in a:
    s += i
k = 5
print(s / k)

# Input: 5 2 3 1 5 10
# Output: 4.2


# Task 4
n = int(input())
m = int(input())
a = []
for i in range(n):
    a.append(int(input()))
print(a[m])

# Input: 10 3 1 10 23 32 18 74 29 73 1 82
# Output: 32


# Task 5
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

s = 0
for i in range(0, n, 2):
    s += a[i]
print(s)

# Input: 6 1 9 2 8 3
# Output: 6