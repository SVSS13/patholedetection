def calculate_risk(width, depth, speed):
    if speed == 0:
        return 0
    return (width * depth) / speed


def adjust_speed_and_eta(distance, traffic_level, speed, width, depth, route_distance):

    # Risk calculation
    risk = calculate_risk(width, depth, speed)

    # Speed adjustment
    if distance > 40:
        new_speed = speed - 5
    elif 20 <= distance <= 40:
        new_speed = speed - 15
    else:
        new_speed = speed - 25

    # Traffic effect
    if traffic_level == "High":
        new_speed -= 10

    # ETA
    time = route_distance / max(new_speed, 1)

    return {
        "adjusted_speed": new_speed,
        "risk": risk,
        "eta": round(time, 2)
    }


def calculate_eta(distance, speed):
    if speed == 0:
        return float('inf')
    return distance / speed