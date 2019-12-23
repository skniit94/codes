from entities.parking_system import ParkingSystem


class ParkingController(object):

    operations_code_map = {
        "1": "Park a vehicle",
        "2": "Unpark a vehicle",
        "3": "isparked",
        "4": "get vehicles with a colour",
        "5": "get vehicles with a type",
        "6": "Parking System current status",
    }

    operations_req_param_map = {
        "1": ['Vehicle Number', 'Vehicle Colour', 'Vehicle Type'],
        "2": ['Vehicle Number'],
        "3": ['Vehicle Number'],
        "4": ["Vehicle Colour"],
        "5": ["Vehicle Type"],
        "6": []
    }

    def __init__(self):
        pass

    def initialize_system(self, slots_per_row, rows_per_level, levels):
        self.target = ParkingSystem(slots_per_row, rows_per_level, levels)

    def park(self):
        self.target.park(*self.param_list)

    def unpark(self):
        self.target.unpark(*self.param_list)

    def isparked(self):
        self.target.isparked(*self.param_list)

    def get_vehicles_with_colour(self):
        self.target.get_vehicles_with_colour(*self.param_list)

    def get_vehicles_with_type(self):
        self.target.get_vehicles_with_type(*self.param_list)

    def get_current_status(self):
        self.target.get_current_status()


    def gather_req_info(self, query):

        req_params = ParkingController.operations_req_param_map.get(query)
        param_list = []
        if req_params:
            for param in req_params:
                print (f'Enter {param} :')
                param_list.append(input())
        return param_list


    def query_handler(self, query):
        self.param_list = self.gather_req_info(query)

        if query == '1':
            self.park()
        if query == '2':
            self.unpark()
        if query == '3':
            self.isparked()
        if query == '4':
            self.get_vehicles_with_colour()
        if query == '5':
            self.get_vehicles_with_type()
        if query == '6':
            self.get_current_status()



