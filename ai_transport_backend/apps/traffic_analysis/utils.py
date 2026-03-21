def validate_input(vehicle_count, road_length):
    if vehicle_count < 0 or road_length <= 0:
        return False
    return True