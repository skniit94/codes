from entities.slot import Slot


class Row(object):

    def __init__(self, level, row_no, slots):
        self.level = level
        self.row_no = row_no
        self.slot_count = slots
        self.slots = []
        self.initialize()

    def initialize(self):
        for i in range(self.slot_count):
            self.slots.append(Slot(self.level, self.row_no, i))

