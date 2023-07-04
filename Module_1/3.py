# Task 1
# Answer: (x % 2 != 0) or (x % 10 != 5)


# Task 2
# Answer: i 10


# Task 3
k = int(input())
n = int(input())
s = 0
k += (k % 2 == 0)
while (k <= n):
    s += k
    k += 2
print(s)

# Input: 12345 56789
# Output: 768182441


# Task 4 
n = int(input())
fact = 1
for i in range(2, n+1):
    fact *= i
print(fact)

# Input: 10
# Output: 3628800