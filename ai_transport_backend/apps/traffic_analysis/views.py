from rest_framework.decorators import api_view
from rest_framework.response import Response
from .services import calculate_density, classify_density
from .utils import validate_input
from .models import TrafficRecord
from apps.transport_management.scheduling import adjust_speed_and_eta


@api_view(['GET', 'POST'])
def analyze_traffic(request):

    # ✅ Allow GET (for testing)
    if request.method == 'GET':
        return Response({
            "message": "Send POST request with vehicle_count and road_length"
        })

    print("DATA RECEIVED:", request.data)

    try:
        vehicle_count = int(request.data.get('vehicle_count', 0))
        road_length = float(request.data.get('road_length', 1))
        speed = float(request.data.get('speed', 50))
        distance = float(request.data.get('distance', 30))
    except:
        return Response({"error": "Invalid input format"}, status=400)

    if not validate_input(vehicle_count, road_length):
        return Response({"error": "Invalid values"}, status=400)

    # 🚦 Traffic Logic
    density = calculate_density(vehicle_count, road_length)
    traffic_level = classify_density(density)

    # 🚀 Transport Logic Integration
    transport_result = adjust_speed_and_eta(
        distance=distance,
        traffic_level=traffic_level,
        speed=speed,
        width=2,
        depth=1,
        route_distance=10
    )

    # 💾 Save to DB
    TrafficRecord.objects.create(
        vehicle_count=vehicle_count,
        road_length=road_length,
        density=density,
        traffic_level=traffic_level
    )

    return Response({
        "traffic": {
            "vehicle_count": vehicle_count,
            "road_length": road_length,
            "density": density,
            "traffic_level": traffic_level
        },
        "transport": transport_result
    })