from course import Course

def main():
    # test if course gets initialized properly

    # no conflict sections
    course1 = Course('Subject 10', 'ABC', 10, 10, 3.0)

    # 1 conflict section
    course2 = Course('Subject 11', 'DEF', 10, 10, 3.0, 'GHI')

    # multiple conflict sections
    course3 = Course('Subject 12', 'JKL', 10, 10, 3.0, 'MNO', 'PQR', 'STU')

    print '\nSubject w/o conflict sections'
    print course1
    print '\nSubject w/ 1 conflict section'
    print course2
    print '\noSubject w/ multiple conflict sections'
    print course3

if __name__ == '__main__':
    main()
