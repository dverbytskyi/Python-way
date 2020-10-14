if __name__ == '__main__':
    # students = list()
    # for _ in range(int(input())):
    #     name = input()
    #     score = float(input())
    #     students.append([name, score])
    #
    # scores = [student[1] for student in students]
    # scores = set(scores)
    # scores = list(scores)
    # scores.remove(min(scores))
    # second_lowest = min(scores)
    #
    # student_names = list()
    #
    # for student in students:
    #     if student[1] == second_lowest:
    #         student_names.append(student[0])
    #
    # for name in student_names:
    #     print(name)

    n = int(input())
    marksheet = [[input(), float(input())] for _ in range(n)]
    second_highest = sorted(list(set([marks for name, marks in marksheet])))[1]
    print('\n'.join([a for a, b in sorted(marksheet) if b == second_highest]))
