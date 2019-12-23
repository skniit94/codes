from entities.row import Row


class Level(object):

    def __init__(self, height, rows, slots_per_row):
        self.height = height
        self.row_count = rows
        self.slots_per_row = slots_per_row
        self.rows = []
        self.initialize()

    def initialize(self):
        for i in range(self.row_count):
            self.rows.append(Row(self.height, i, self.slots_per_row))