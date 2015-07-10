class Course:
    """docstring for Course"""
    def __init__(self, subject, section, available_slots, demand, credits, *args):
        self.subject = str(subject)
        self.section = str(section)
        self.available_slots = int(available_slots)
        self.demand = int(demand)
        self.credits = float(credits)
        
        self.conflict_sections = list()

        for x in args:
            self.conflict_sections.append(str(x))

    def __repr__(self):
        return ' '.join([str(self.subject),str(self.section),str(self.available_slots),str(self.demand),str(self.credits),str(self.conflict_sections)])  
        