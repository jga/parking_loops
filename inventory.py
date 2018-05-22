

PARKING_INVENTORIES = [
    {'lot_name': 'A', 'space_count': 10},
    {'lot_name': 'B', 'space_count': 50},
    {'lot_name': 'C', 'space_count': 10}
]


def sum_inventory(inventories):
    return sum([inventory['space_count'] for inventory in inventories])


def add_capacity(inventories):
    # original_sum = sum of dict space_count
    # Changed the name to inventory to more clearly reflect what each element in the list represents
    original_sum = sum_inventory(inventories)
    new_sum = 0
    for inventory in inventories:
        updated_space_count = int(inventory['space_count'] * 1.1)
        new_sum += updated_space_count
        # Using the format method of a string to create a mini-template
        output_message = 'Lot {0} spaces: {1}'.format(inventory['lot_name'], updated_space_count)
        print(output_message)
    # Print original_sum + output_message
    print('Original Count {0} New Count {1}'.format(original_sum, new_sum))
    print('Done.')


add_capacity(PARKING_INVENTORIES)
