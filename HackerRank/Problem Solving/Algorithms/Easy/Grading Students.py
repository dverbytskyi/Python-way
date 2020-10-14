
def gradingStudents(grades):
    res = []
    for grade in grades:
        if grade >= 38:
            mod5 = grade % 5
            if mod5 >= 3:
                grade = grade + (5 - mod5)

        print(grade)
        # if grade >= 38:
        #     if grade % 5 == 3:
        #         grade += 2
        #         # print(grade)
        #         res.append(grade)
        #     elif grade % 5 == 4:
        #         grade += 1
        #         # print(grade)
        #         res.append(grade)
        #     else:
        #         # print(grade)
        #         res.append(grade)
        # else:
        #     # print(grade)
        #     res.append(grade)

    # print(res)
    return res

if __name__ == '__main__':

    grades_count = int(input().strip())
    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)