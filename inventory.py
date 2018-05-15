
# I've transformed the parking space inventories into dictionaries with lot_name and space_count keys
PARKING_INVENTORIES = [
    {'lot_name': 'A', 'space_count': 10},
    {'lot_name': 'B', 'space_count': 50},
    {'lot_name': 'C', 'space_count': 10}
]


def add_capacity(parking_inventories):
    for count in PARKING_INVENTORIES:
        print(count['lot_name'],'', str(count['space_count'] * 10 / 100 + count['space_count']))
    print('Done.')


add_capacity(PARKING_INVENTORIES)


