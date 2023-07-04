# # 1
# n = int(input())
# for i in range (n + 1):
#     if i % 3 == 0 and i % 6 != 0:
#         print(i)
# # Input: 20
# # Output: 3 9 15


# # 2
# n = int(input())
# for i in range (10, n + 1):
#     if i % 10 % 2 == 0:
#         print(i)
# # Input: 17
# # Output: 10 12 14 16

# # 3
# n = int(input())
# counter_chet = 0
# counter_nechet = 0
# if (n % 2 == 0):
#     for i in range (2, n + 1, 2):
#         counter_chet += 1
#     print(counter_chet)
# else:
#     for i in range (1, n + 1, 2):
#         counter_nechet += i
#     print(counter_nechet)
# # Input 1: 100
# # Output 1: 50
# # Input 2: 99
# # Outout 2: 2500

# # 4
# n = int(input())
# if (n % 3 == 0):
#     m = int(input())
#     counter = 0
#     for i in range(m, n + 1, m):
#         counter += 1
#     print(counter)
# else:
#     for i in range(1, n + 1):
#         print(n**i)
# # Input 1: 8
# # Output 1: 8 64 512 4096 32768 262144 2097152 16777216
# # Input 2: 99 7
# # Output2: 14

# 5
a = int(input())
b = int(input())
n = int(input())
counter = 0
for i in range(n):
    x = int(input())
    if (x > 10 and ((a*a + b*b) == x * x)):
        if (x % 3 == 0 or x % 4 == 0):
            counter += 1
print(counter)
# Input: 12 16 10 20 12 11 1 19 7 10 21 22 18
# Output: 1