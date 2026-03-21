from rest_framework.decorators import api_view
from rest_framework.response import Response
from .scheduling import calculate_risk, adjust_speed_and_eta, calculate_eta
from .utils import classify_risk
from .models import TransportLog

@api_view(['POST'])
def smart_transport_control(request):
    distance = request.data.get('distance', 30)
    traffic_level = request.data.get('traffic_level', "Medium")
    speed = request.data.get('speed', 40)
    width = request.data.get('width', 1)
    depth = request.data.get('depth', 1)
    route_distance = request.data.get('route_distance', 10)

    # Risk calculation
    risk = calculate_risk(width, depth, speed)
    risk_level = classify_risk(risk)

    # Speed adjustment
    new_speed = adjust_speed(distance, traffic_level, risk_level, speed)

    # ETA calculation
    eta = calculate_eta(route_distance, new_speed)

    # Save log
    TransportLog.objects.create(
        original_speed=speed,
        adjusted_speed=new_speed,
        traffic_level=traffic_level,
        risk_level=risk_level,
        eta=eta
    )

    return Response({
        "distance_to_pothole": distance,
        "traffic_level": traffic_level,
        "risk_level": risk_level,
        "original_speed": speed,
        "adjusted_speed": new_speed,
        "eta": eta
    })