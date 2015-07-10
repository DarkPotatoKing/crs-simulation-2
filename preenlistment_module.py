from course import Course

class PreenlistmentModule:
    """docstring for PreenlistmentModule"""
    desired_classes = list()

    def load(self, filename):
        pass

    def batchrun(self, num_runs = 1):
        pass

    def add_class(self, *args):
        self.desired_classes.append(Course(*args))

    def __repr__(self):
        return str(self.desired_classes)

    @staticmethod
    def has_conflict(course1, course2):
        pass
        