# # 코드업 python 기초 100제 답안 (77~98)

# #77
# from typing_extensions import ParamSpec


# n = int(input())
# s = 0 
# for i in range(1, n+1):
#     if i % 2 == 0:
#         s += i
# print(s)

# #78
# while True:
#     a = input()
#     print(a)
#     if a == "q":
#         break

# #79
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s += i
#     if n <= s:
#         print(i)
#         break

# #80
# a, b = map(int, input().split())
# for x in range(1, a+1):
#     for y in range(1, b+1):
#         print(x, y)

# #81
# n = int(input(), 16)
# for i in range(1, 16):
#     print('%X*%X=%X' %(n, i, n*i))

# #82
# n = int(input())
# for i in range(1, n+1):    
#     if (i % 10 == 3 or i % 10 == 6 or i % 10 == 9):
#         print("X", end=" ")
#         continue
#     print(i, end=" ")

# #83
# r, g, b = map(int, input().split())
# c = 0
# for i in range(0, r):
#     for j in range(0, g):
#         for k in range(0, b):
#             print(i, j, k)
#             c += 1
# print(c)

# #84
# h, b, c, s = map(int, input().split())
# m = (h * b * c * s) / 8 / 1024 / 1024
# print("%.1f MB" %m)

# #85
# h, b, c = map(int, input().split())
# m = (h * b * c) / 8 / 1024 / 1024
# print("%.2f MB" %m)

# #86
# n = int(input())
# s = 0
# for i in range(1, n+1):
#     s += i
#     if n <= s:
#         # print(s)
#         break

# #87
# n = int(input())
# for i in range(1, n + 1):
#     if i % 3 == 0:
#         continue
#     print(i, end=" ")

# #88
# a, d, c = map(int, input().split())
# total = a
# for i in range(1, c):
#     total = total + d
# print(total)

# #89
# a, r, n = map(int, input().split())
# total = a 
# for i in range(1, n):
#     total = total * r
# print(total)

# #90
# a, m, d, n = map(int, input().split())
# total = a
# for i in range(1, n):
#     total = total * m + d
# print(total)

# #91
# a, b, c = map(int, input().split())
# d = 1
# while d % a != 0 or d % b != 0 or d % c != 0:
#     d = d + 1
# print(d)

# #92
# n = int(input())
# a = list(map(int, input().split()))
# d = []
# for i in range(24):
#     d.append(0)
# for i in range(n):
#     d[a[i]] += 1
# for i in range(1,24):
#     print(d[i], end=" ")

# #93
# n = int(input())
# a = list(map(int, input().split()))
# for i in range(n-1, -1, -1):
#     print(a[i], end=" ")

# #94
# n = int(input())
# a = list(map(int, input().split()))
# k = a[0]
# for i in range(n):
#     if(k > a[i]):
#         k = a[i]
# print(k)

# 95
# d = []
# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     d[x][y] = 1
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end=" ")
#     print()

# #96
# d = []
# for i in range(20):
#     d.append([])
#     for j in range(20):
#         d[i].append(0)
# for i in range(19):
#     a = input().split()
#     for j in range(19):
#         d[i+1][j+1] = int(a[j])
# n = int(input())
# for i in range(n):
#     x, y = map(int, input().split())
#     for j in range(1, 20):
#         if d[x][j] == 0:
#             d[x][j] = 1
#         else:
#             d[x][j] = 0
#         if d[j][y] == 0:
#             d[j][y] = 1
#         else:
#             d[j][y] = 0
# for i in range(1, 20):
#     for j in range(1, 20):
#         print(d[i][j], end=" ")
#     print()

#97
t = []
h, w = map(int, input().split())
for i in range(h+1):
    t.append([])
    for j in range(w+1):
        t[i].append(0)
n = int(input())
for i in range(n):
    l, d, x, y = map(int, input().split())
    if d == 0:
        for j in range(l):
            t[x][y+j] = 1
    else:
        for j in range(l):
            t[x+j][y] = 1



for i in range(1, h+1):
    for j in range(1, w+1):
        print(t[i][j], end=" ")
