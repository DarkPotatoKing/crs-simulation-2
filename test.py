from course import Course
from preenlistment_module import PreenlistmentModule as PM

def main():
    # test if course gets initialized properly

    # no conflict sections
    course1 = Course('Subject 10', 'ABC', 10, 10, 3.0)

    # 1 conflict section
    course2 = Course('Subject 11', 'DEF', 10, 10, 3.0, 'GHI')

    # multiple conflict sections
    course3 = Course('Subject 12', 'JKL', 10, 10, 3.0, 'MNO', 'PQR', 'STU')

    # initializing Course with whitespaces in args
    course4 = Course('     Subject 13    ', '   ABC    ', 10, 10, 3.0, '  LOL   ')

    print '\nSubject w/o conflict sections'
    print course1
    print '\nSubject w/ 1 conflict section'
    print course2
    print '\nSubject w/ multiple conflict sections'
    print course3
    print '\ninitializing Course with whitespaces in args'
    print course4

    # test if class is added to a desired classes succesfully
    print '\ntest if class is added to a desired classes succesfully'
    pm = PM()
    pm.add_class(*['Subject 13','VWX', 10, 10, 3.0, 'YZA', 'BCD', 'EFG'])
    print pm

    # test if preenlistment module loads .csv file successfully
    print '\ntest if preenlistment module loads .csv file successfully'
    pm.load('sample.csv')
    print pm

if __name__ == '__main__':
    main()
