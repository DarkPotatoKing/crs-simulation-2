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
        pass
        