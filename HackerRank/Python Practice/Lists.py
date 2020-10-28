# problem statement - https://www.hackerrank.com/challenges/python-lists/problem

if __name__ == '__main__':
    N = int(input())
    arr = list()
    for _ in range(N):
        command, *values = input().split()
        if command == "insert":
            arr.insert(int(values[0]), int(values[1]))
        elif command == "print":
            print(arr)
        elif command == "remove":
            arr.remove(int(values[0]))
        elif command == "append":
            arr.append(int(values[0]))
        elif command == "sort":
            arr.sort()
        elif command == "pop":
            arr.pop()
        elif command == "reverse":
            arr.reverse()

    # print(command)
    # print(values)
