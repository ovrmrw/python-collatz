def collatz(num, list=[]):
    next = int(num / 2 if num % 2 == 0 else num * 3 + 1)
    list.append(next)
    if (next == 1):
        return list
    else:
        return collatz(next, list)


if __name__ == '__main__':
    num = int(input())
    list = collatz(num)
    print(list)
