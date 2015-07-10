from preenlistment_module import PreenlistmentModule as PM
import sys

def main():
    filename = ''
    num_runs = 0

    try:
        filename = sys.argv[1]

        with open(filename,'r') as f:
            pass
    except IndexError:
        print 'No input! Please pass the .csv file as an argument.'
        return
    except IOError:
        print 'Cannot read input file.'
        return

    try:
        num_runs = int(sys.argv[2])
    except Exception, e:
        num_runs = 1
    
    pm = PM()
    pm.load(filename)
    pm.batchrun(num_runs)


if __name__ == '__main__':
    main()