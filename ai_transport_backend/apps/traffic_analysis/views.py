from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import calculate_density, classify_density
from .utils import validate_input
from .models import TrafficRecord
from apps.transport_management.scheduling import adjust_speed_and_eta

@api_view(['POST'])
def analyze_traffic(request):

    print("DATA RECEIVED:", request.data)

    vehicle_count = int(request.data.get('vehicle_count', 0))
    road_length = int(request.data.get('road_length', 1))

    if not validate_input(vehicle_count, road_length):
        return Response({"error": "Invalid input"}, status=400)

    # 🚦 Traffic Logic
    density = calculate_density(vehicle_count, road_length)
    traffic_level = classify_density(density)

    # 🚀 CALL TRANSPORT MODULE AUTOMATICALLY
    transport_result = adjust_speed_and_eta(
        distance=30,              # dummy for now (later from pothole module)
        traffic_level=traffic_level,
        speed=50,                 # current speed
        width=2,
        depth=1,
        route_distance=10
    )

    # 💾 Save Traffic
    TrafficRecord.objects.create(
        vehicle_count=vehicle_count,
        road_length=road_length,
        density=density,
        traffic_level=traffic_level
    )

    # 🔥 COMBINED RESPONSE
    return Response({
        "traffic": {
            "vehicle_count": vehicle_count,
            "road_length": road_length,
            "density": density,
            "traffic_level": traffic_level
        },
        "transport": transport_result
    })