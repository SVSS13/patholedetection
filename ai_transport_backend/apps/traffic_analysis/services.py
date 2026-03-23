def calculate_density(vehicle_count, road_length):
    return vehicle_count / road_length


def classify_density(density):
    if density < 5:
        return "Low"
    elif 5 <= density < 15:
        return "Medium"
    else:
        return "High"