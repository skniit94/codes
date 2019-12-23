import traceback

from controller import ParkingController


def main():

    try:
        print ("Enter levels : ")
        levels = int(input())
        print ("Enter rows per level :")
        rows = int(input())

        print ("Enter slots per row :")
        slots = int(input())

        controller = ParkingController()
        controller.initialize_system(slots, rows, levels)

        print("Parking System has been initalized")

        print("Below operations are supported")

        print(ParkingController.operations_code_map)

        print ("Type any number")

        while True:

            query = input()
            controller.query_handler(query)
            print('Success')

    except Exception as e:
        print ('Error')
        print (e)
        print (traceback.format_exc())


if __name__ ==  '__main__':
    main()