# -*- coding: utf-8 -*-®

# 数组
from functools import reduce

classmates = ['Michael', 'Bob', 'Tracy']
print("class:" + classmates[-3] + "\nlenght:" + str(len(classmates)))

# 单二维数组
t = ('a', 'b', ['A', 'B'])
t[2][0] = 'X'
t[2][1] = 'Y'
print("t:" + str(t))

# 二维数组
L = [
    ['Apple', 'Google', 'Microsoft'],
    ['Java', 'Python', 'Ruby', 'PHP'],
    ['Adam', 'Bart', 'Lisa']
]
print("L:" + L[0][1])

print(list(range(5)))

d = {'Michael': 95, 'Bob': 75, 'Tracy': 85}
print(d['Michael'])
print('Thomas' in d)

L = []
n = 1
while n <= 99:
    L.append(n)
    n = n + 2
print(L)


# 切片
def trim(s):
    while s[:1] == ' ':
        s = s[1:]
    while s[-1:] == ' ':
        s = s[:-1]
    return s


if trim('hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello') != 'hello':
    print('测试失败!')
elif trim('  hello  ') != 'hello':
    print('测试失败!')
elif trim('  hello  world  ') != 'hello  world':
    print('测试失败!')
elif trim('') != '':
    print('测试失败!')
elif trim('    ') != '':
    print('测试失败!')
else:
    print('测试成功!')

# 迭代
d = {'a': 1, 'b': 2, 'c': 3}
for key, value in d.items():
    print(value)

# 最后一个小问题，如果要对list实现类似Java那样的下标循环怎么办？Python内置的enumerate函数可以把一个list变成索引-元素对，这样就可以在for循环中同时迭代索引和元素本身：
for i, value in enumerate(['A', 'B', 'C']):
    print(i, value)


# 测试
def findMinAndMax(L):
    count = len(L)
    if count == 0: return None, None

    start = 0
    while start < count:
        index = start
        while index < count:
            if L[start] > L[index]:
                min = L[index]
                L[index] = L[start]
                L[start] = min
            index = index + 1
        start = start + 1

    return L[:1][0], L[-1:][0]


print(list(findMinAndMax([7, 3, 1, 9, 5])))

if findMinAndMax([]) != (None, None):
    print('测试失败!')
elif findMinAndMax([7]) != (7, 7):
    print('测试失败!')
elif findMinAndMax([7, 1]) != (1, 7):
    print('测试失败!')
elif findMinAndMax([7, 3, 1, 9, 5]) != (1, 9):
    print('测试失败!')
else:
    print('测试成功!')


# 高阶行数:map
def f(x): return x * x


r = map(f, range(5))
print(list(r))
print(list(map(str, range(10))))

# reduce
print(reduce(lambda x, y: x + y, [1, 3, 5, 7, 9]))

DIGITS = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9}


def str2int(s):
    return reduce(lambda x, y: x * 10 + y, map(lambda char: DIGITS[char], s))


print(str2int('13579'))

# filter
print(list(filter(lambda n: n % 2 == 1, [1, 2, 4, 5, 6, 9, 10, 15])))


def is_palindrome(n):
    if str(n)[:1] == str(n)[-1:]:
        return True


output = filter(is_palindrome, range(1, 1000))
print('1~1000:', list(output))

if list(filter(is_palindrome, range(1, 200))) == [1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 22, 33, 44, 55, 66, 77, 88, 99, 101,
                                                  111, 121, 131, 141, 151, 161, 171, 181, 191]:
    print('测试成功!')
else:
    print('测试失败!')


# 生成器
def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        yield b
        a, b = b, a + b
        n = n + 1
    return 'done'


f = fib(6)
print(f)


# 练习题
def triangles(max):
    n, index = 0, 1
    curt = [index]
    while n < max + 1:
        t = []
        for i in range(n + 1):
            if i == 0:
                t.append(index)
            elif i < len(curt):
                t.append(curt[i] + curt[i - 1])
            else:
                t.append(index)
        curt = t
        print(t)
        n = n + 1
    return 'done'


triangles(6)


def triangles1():
    L = [1]
    while True:
        yield L[:]
        L.append(0)
        L = [L[i] + L[i - 1] for i in range(len(L))]


p = triangles1()
for i in range(7):
    print(next(p))

L = [1]
print(L[:])
L.append(0)

