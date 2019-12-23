from entities.level import Level
from entities.vehicle import Vehicle


class ParkingSystem(object):

    def __init__(self, slots_per_row, rows_per_level, levels):

        self.level_count = levels
        self.rows_per_level = rows_per_level
        self.slots_per_row = slots_per_row
        self.levels = []
        self.vehicle_slot_registry = {}
        self.slot_vehicle_registry = {}
        self.initialize()

    def initialize(self):
        for i in range(self.level_count):
            self.levels.append(Level(i, self.rows_per_level, self.slots_per_row))

    def park(self, number, colour, category):
        print ('park called')

        for level in self.levels:
            for row in level.rows:
                for slot in row.slots:
                    if not slot.occupied:
                        vehicle = Vehicle(number, colour, category)
                        slot.assign_vehicle(vehicle)
                        vehicle.assign_slot(slot)
                        self.update_registry(vehicle, slot)
                        print (str(slot))
                        return
        print('No Empty Slot')

    def update_registry(self, vehicle, slot, unpark=False):
        if not unpark:
            self.vehicle_slot_registry[vehicle.number] = slot
            self.slot_vehicle_registry[slot.id] = vehicle
        else:
            if self.vehicle_slot_registry.get(vehicle.number):
                del self.vehicle_slot_registry[vehicle.number]
            if self.slot_vehicle_registry.get(slot.id):
                del self.slot_vehicle_registry[slot.id]

    def unpark(self, number):

        slot = None
        if self.vehicle_slot_registry.get(number):
            slot = self.vehicle_slot_registry.get(number)

        if not slot:
            print ('No Such Vehicle Present')
            return

        vehicle = self.slot_vehicle_registry[slot.id]

        self.update_registry(vehicle, slot, unpark=True)

        slot.unassign_vehicle()

        vehicle.unassign_slot()

    def isparked(self, number):
        slot = None
        if self.vehicle_slot_registry.get(number):
            slot = self.vehicle_slot_registry.get(number)

        if not slot:
            print ('No Such Vehicle Present')
            return

        print (str(slot))

    def get_vehicles_with_colour(self, colour):
        print ('get_vehicles_with_colour called')
        vehicles = []
        for vehicle in self.slot_vehicle_registry.values():
            if vehicle.colour == colour:
                vehicles.append(str(vehicle))

        print (vehicles, len(vehicles))


    def get_vehicles_with_type(self, category):
        print ('get_vehicles_with_type called')

        vehicles = []
        for vehicle in self.slot_vehicle_registry.values():
            if vehicle.category == category:
                vehicles.append(str(vehicle))

        print (vehicles, len(vehicles))

    def get_current_status(self):
        print ('get_current_status called')

        total_slots = self.level_count*self.rows_per_level*self.slots_per_row

        occupied_slots = len(self.slot_vehicle_registry.keys())
        empty_slots = total_slots - occupied_slots

        print (f'Total slots {total_slots} Occupied slots {occupied_slots} Empty slots {empty_slots}')





