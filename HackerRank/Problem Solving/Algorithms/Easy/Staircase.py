
def staircase(n):
    # for line in range(1, n+1):
    #     print(str('#'*line).rjust(n))
        # for stair in range(line):
        #     print("#"*stair)
        #
    for item in range(1, n+1):
        print(" " * (n-item) + "#" * item)

if __name__ == '__main__':
    n = int(input())
    staircase(n)
