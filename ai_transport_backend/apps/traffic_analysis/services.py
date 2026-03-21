def calculate_density(vehicle_count, road_length):
    if road_length == 0:
        return 0
    return vehicle_count / road_length


def classify_density(density):
    if density < 5:
        return "Low"
    elif density < 15:
        return "Medium"
    return "High"