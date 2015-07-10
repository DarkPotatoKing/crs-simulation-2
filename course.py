class Course:
    """docstring for Course"""
    
    def __init__(self, *args):
        args = [str(x).strip() for x in args]
        self.subject = str(args[0])
        self.section = str(args[1])
        self.available_slots = int(args[2])
        self.demand = int(args[3])
        self.credits = float(args[4])
        
        self.conflict_sections = list()

        for x in args[5:]:
            self.conflict_sections.append(str(x))

    def __repr__(self):
        return ' '.join([str(self.subject),str(self.section),str(self.available_slots),str(self.demand),str(self.credits),str(self.conflict_sections)])  
