# 코드업 python 기초 100제 답안 (32~64)

#32
a = int(input())
print(-a)

#33
a = ord(input())
print(chr(a + 1))

#34
a, b = map(int, input().split())
print(a - b)

#35
a, b = map(float, input().split())
print(a * b)

#36
a, b = input().split()
print(a * int(b))

#37
a = int(input())
b = input()
print(b * a)

#38
a, b = map(int, input().split())
print(a ** b)

#39
a, b = map(float, input().split())
print(a ** b)

#40
a, b = map(int, input().split())
print(a // b)

#41
a, b = map(int, input().split())
print(a % b)

#42
a = float(input())
print(format(a, ".2f"))

#43
a, b = map(float, input().split())
c = a / b
print(format(c, ".3f"))

#44
a, b = map(int, input().split())
print(a + b)
print(a - b)
print(a * b)
print(a // b)
print(a % b)
print(format(a / b, ".2f"))

#45
a, b, c = map(int, input().split())
s = a + b + c
av = s / 3
print(s, format(av, ".2f"))

#46
a = input()
print(a << 1)

#47
a, b = map(int, input().split())
print(a << b)

#48
a, b = map(int, input().split())
print(a < b)

#49
a, b = map(int, input().split())
print(a == b)

#50
a, b = map(int, input().split())
print(a <= b)

#51
a, b = map(int, input().split())
print(a != b)

#52
a = int(input())
print(bool(a))

#53
a = bool(int(input()))
print(not(a))

#54
a, b = map(int, input().split())
print(bool(a) and bool(b))

#55
a, b = map(int, input().split())
print(bool(a) or bool(b))

#56
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print(a != b or b != a)

#57
a, b = map(int, input().split())
print(bool(a == b))

#58
a, b = map(int, input().split())
a = bool(a)
b = bool(b)
print(bool(not(a or b)))

#59
a = int(input())
print(~a)

#60
a, b = map(int, input().split())
print(a & b)

#61
a, b = map(int, input().split())
print(a | b)

#62
a, b = map(int, input().split())
print(a ^ b)

#63
a, b = map(int, input().split())
print(a if a > b else b)

#64
a, b, c = map(int, input().split())
print(min(a, b, c))