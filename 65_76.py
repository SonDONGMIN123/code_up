# 코드업 python 기초 100제 답안 (65~76)

#65
a, b, c = map(int, input().split())
if a % 2 == 0:
    print(a)
if b % 2 == 0:
    print(b)
if c % 2 == 0:
    print(c)

#66
a, b, c = map(int, input().split())
if a % 2 == 0:
    print("even")
else:
    print("odd")
if b % 2 == 0:
    print("even")
else:
    print("odd")
if c % 2 == 0:
    print("even")
else:
    print("odd")

#67
a = int(input())
if a < 0:
    if a % 2 == 0:
        print("A")
    else:
        print("B")
else:
    if a % 2 == 0:
        print("C")
    else:
        print("D")

#68
a = int(input())
if 90 <= a <= 100:
    print("A")
elif 70 <= a:
    print("B")
elif 40 <= a:
    print("C")
else:
    print("D")

#69
a = input()
if a == "A":
    print("best!!!")
elif a == "B":
    print("good!!")
elif a == "C":
    print("run!")
elif a == "D":
    print("slowly~")
else:
    print("what?")

#70
a = int(input())
if a // 3 == 1:
    print("spring")
elif a // 3 == 2:
    print("summer")
elif a // 3 == 3:
    print("fall")
else:
    print("winter")

#71
a = int(input())
while a != 0:
    print(a)
    a = int(input())

#72
a = int(input())
while a >= 0:
    print(a)
    a -= 1

#73
a = int(input())
while a > 0:
    a -= 1
    print(a)
    
#74
a = ord(input())
b = ord("a")
while b <= a:
    print(chr(b), end=" ")
    b += 1

#75
a = int(input())
b = 0
while b <= a:
    print(b)
    b += 1

#76
a = int(input())
for b in range(0, a+1):
    print(b)