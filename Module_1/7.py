# # 1
# print(sum([x * x for x in range(1, 101)]))
# # Output: 338350

# # 2
# # Answer: 0 8 16 24 32

# # 3
# print(len([x for x in range(1, 21) if x % 2 == 0]))
# # Output: 10

# # 4
# print(len([x for i, x in enumerate([int(y) for y in input().split()]) if i % 2 ==0 and x % 2 == 0]))
# # Output: 3

# 5
print(len([x for x in range(1,1001) if x % 7 == 0 or x % 11 == 0]))
# Output: 220