

PARKING_INVENTORIES = [
    {'lot_name': 'A', 'space_count': 10},
    {'lot_name': 'B', 'space_count': 50},
    {'lot_name': 'C', 'space_count': 10}
]


def add_capacity(inventories):
    # Changed the name to inventory to more clearly reflect what each element in the list represents
    for inventory in inventories:
        # Cleaned up your math to make it simpler. Let's talk it over if it's unclear why this is
        # a mathematical equivalent to your work
        updated_space_count = int(inventory['space_count'] * 1.1)
        # Using the format method of a string to create a mini-template
        output_message = 'Lot {0} spaces: {1}'.format(inventory['lot_name'], updated_space_count)
        print(output_message)
    # Moved the final print. Only want one print of "Done". The entire function completes only once per call. If it's in the loop scope,
    # it prints every iteration, creating 3 "Done." messages.
    print('Done.')


add_capacity(PARKING_INVENTORIES)
