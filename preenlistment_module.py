from __future__ import division
from course import Course
import random

class PreenlistmentModule:
    """docstring for PreenlistmentModule"""
    desired_classes = list()

    def load(self, filename):
        self.desired_classes = list()
        with open(filename, 'r') as f:
            classes = [x.strip() for x in f.readlines()]
            for x in classes:
                args = x.split(',')
                # print args
                self.add_class(*args)

    def batchrun(self, num_runs = 1):
        total_run_units = 0.0
        total_num_times_granted = dict()

        # create a dictionary of number of times a subject is granted
        # set everything to zero at the start
        for x in self.desired_classes:
            total_num_times_granted[x] = 0

        for run_num in xrange(num_runs):
            granted_classes = list()
            units = 0
            print '\nRun #%s' % str(run_num+1)
            print 'Granted classes:\n'

            # iterate through desired classes
            for x in self.desired_classes:
                # randomize slot
                if PreenlistmentModule.class_granted(x):
                    # if granted, check for conflict
                    conflict = False
                    for y in granted_classes:
                        conflict = PreenlistmentModule.has_conflict(x,y)
                        # break if there is conflict
                        if conflict:
                            break

                    # check if adding subeject results to overload
                    if units + x.credits > 20.0:
                        conflict = True

                    # add class only if no conflict
                    if not conflict:
                        granted_classes.append(x)
                        units += x.credits
                        total_num_times_granted[x] += 1

            # print granted classes
            for x in granted_classes:
                print '{}\t{}\t({})'.format(x.subject, x.section, x.credits)
            print 'Total units: {}'.format(units)
            total_run_units += units

        # print runs summary
        print '\n\nRuns Summary ({} runs)'.format(num_runs)
        print 'Average units:\t{}'.format(total_run_units/num_runs)
        print 'Subject\tSection\t[Times Granted/Num runs]'
        # print stats of each subject
        for x in self.desired_classes:
            print '{}\t{}\t({}/{})\t{:.0%}'.format(x.subject,x.section,total_num_times_granted[x],num_runs,total_num_times_granted[x]/num_runs)
        print '\n'
        self.print_cumulative_stats(total_num_times_granted, num_runs)

    @staticmethod
    def print_cumulative_stats(total_num_times_granted, num_runs):
        subjects = [x.subject for x in total_num_times_granted]
        subjects = sorted(list(set(subjects)))
        cumulative_stats = dict()

        for x in subjects:
            cumulative_stats[x] = 0

        for x in total_num_times_granted:
            name = x.subject
            cumulative_stats[name] += total_num_times_granted[x]

        print 'Cumulative Stats'
        print 'Subject\t\t[Times Granted/Num runs]'
        # print stats of each subject
        for x in cumulative_stats:
            print '{}\t\t({}/{})\t{:.0%}'.format(x, cumulative_stats[x], num_runs, cumulative_stats[x] / num_runs)
        print '\n'

    def add_class(self, *args):
        self.desired_classes.append(Course(*args))

    def __repr__(self):
        return str(self.desired_classes)

    @staticmethod
    def class_granted(course):
        random.seed()
        return random.random() < course.available_slots / course.demand

    @staticmethod
    def is_same_subject(course1, course2):
        return course1.subject == course2.subject

    @staticmethod
    def is_overlapping_schedule(course1, course2):
        # check if they are the same section
        if course1.section == course2.section:
            return True

        # check overlapping schedules using conflict_sections attribute
        # iterate through conflict_sections
        for x in course1.conflict_sections:
            # check if x has a substring in course2's section
            if course2.section.find(x) != -1:
                return True

        # if the none of the above conditions are satisfied, return False
        return False

    @staticmethod
    def has_conflict(course1, course2):
        # check if they are the same subject or overlapping schedule
        return PreenlistmentModule.is_same_subject(course1, course2) or PreenlistmentModule.is_overlapping_schedule(course1, course2)

