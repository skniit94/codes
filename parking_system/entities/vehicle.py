


class Vehicle(object):

    def __init__(self, number, colour, category='CAR'):

        self.number = number
        self.colour = colour
        self.category = category
        self.slot = None
        self.isparked = False

    def __repr__(self):
        return f'{self.number} {self.colour} {self.category}'

    def assign_slot(self, slot):
        self.slot = slot
        self.isparked = True

    def unassign_slot(self):
        self.slot = None
        self.isparked = False