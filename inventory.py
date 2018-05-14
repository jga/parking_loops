
# I've transformed the parking space inventories into dictionaries with lot_name and space_count keys
PARKING_INVENTORIES = [
    {'lot_name': 'A', 'space_count': 10},
    {'lot_name': 'B', 'space_count': 50},
    {'lot_name': 'C', 'space_count': 10}
]


def add_capacity(parking_inventories):
    # loop through each inventory, add 10% capacity to the existing space count, rount to nearest integer,
    #  and print out the name and new inventory. Then print when function is done
    print('Done.')


add_capacity(PARKING_INVENTORIES)

