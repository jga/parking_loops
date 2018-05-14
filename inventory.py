
PARKING_SPACE_COUNTS = [10, 50, 30]


def add_capacity(parking_space_counts):
    # changing name from non-descript ints to specific descriptor
    for parking_space_count in PARKING_SPACE_COUNTS:
        print(parking_space_count + 1)
    # Moved back into the function because instructions were to note the *function" was done, not the module
    print('Done.')


add_capacity(PARKING_SPACE_COUNTS)

