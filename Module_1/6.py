# # 1
# n = int(input())
# m = int(input())
# a = []
# a.append(n)
# a.append(m)
# for i in a:
#     print(i)
# print("Сумма:", sum(a))
# # Input: 12 34
# # Output: 12 34 46

# # 2
# a = []
# for i in input().split():
#     a.append(i)
# print(a[0], a[len(a) - 1])
# # Input: Программирование после школы
# # Outout: Программирование школы

# # 3
# a = []
# for i in input().split():
#     a.append(i)
# maxim = -1e9
# res = ""
# for i in a:
#     if len(i) > maxim:
#         maxim = len(i)
#         res = i
# print(res)
# # Input: Вот Вотяков нетипичный учитель
# # Output: нетипичный

# # 4
# n = int(input())
# a = []
# for i in range(1, n + 1):
#     if i % 3 == 0 or i % 5 == 0:
#         a.append(i)
# print(sum(a))
# # Input: 1000
# # Output: 234168

# 5
a = []
for i in input().split():
    a.append(i)
maxim = -1e9
res = ""
for i in a:
    if a.count(i) > maxim:
        maxim = a.count(i)
        res = i
print(i)
# Input: cat cat dog cat dog dog cat cat dog dog cat
# Output: cat