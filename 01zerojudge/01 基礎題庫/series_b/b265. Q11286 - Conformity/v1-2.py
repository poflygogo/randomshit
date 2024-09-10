while True:
    times = int(input())
    if times == 0: break

    student_course = {}
    for _ in range(times):
        course = input().split()
        course.sort()
        course = ''.join(course)
        student_course[course] = student_course.get(course, 0) + 1

    student_course_total = tuple(student_course.values())
    mostpopular = max(student_course_total)
    A = student_course_total.count(mostpopular)

    print(mostpopular * A)
