while True:
    times = int(input())
    if times == 0: break
    
    student_course = {}
    for _ in range(times):
        course = tuple(sorted(input().split()))
        if course in student_course:
            student_course[course] += 1

        else:
            student_course[course] = 1

    student_course_total = tuple(student_course.values())
    mostpopular = max(student_course_total)
    A = student_course_total.count(mostpopular)

    print(mostpopular * A)
