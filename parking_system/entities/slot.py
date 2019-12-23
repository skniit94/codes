

class Slot(object):

    def __init__(self, level, row, position):

        self.level = level
        self.row = row
        self.position = position
        self.id = f'{level}#{row}#{position}'
        self.occupied = False
        self.vehicle = None

    def __repr__(self):
        return f'level = {self.level} row = {self.row} slot = {self.position}'

    def assign_vehicle(self, vehicle):
        self.occupied = True
        self.vehicle = vehicle

    def unassign_vehicle(self):
        self.occupied = False
        self.vehicle = None