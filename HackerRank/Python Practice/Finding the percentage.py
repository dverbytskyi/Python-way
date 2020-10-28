# problem statement - https://www.hackerrank.com/challenges/finding-the-percentage/problem

def find_the_percentage(student_marks, query_name):
    # res = (sum(values) / len(values) for keys, values in student_marks.items() if query_name == keys)
    # return res
    res = 0
    for key, value in student_marks.items():
        if query_name == key:
            # print(key, value)
            res = format(sum(value) / len(value), ".2f")

    return res

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()

    result = find_the_percentage(student_marks, query_name)
    print(result)


# dict_1 = {'First' : [1, 2 ,3],
# 'Second' : [4, 5 ,6]}