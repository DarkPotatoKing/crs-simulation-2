from course import Course

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
        pass

    def add_class(self, *args):
        self.desired_classes.append(Course(*args))

    def __repr__(self):
        return str(self.desired_classes)

    @staticmethod
    def has_conflict(course1, course2):
        # check if they are the same subject or overlapping schedule
        return is_same_subject(course1, course2) or is_overlapping_schedule(course1, course2)

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
