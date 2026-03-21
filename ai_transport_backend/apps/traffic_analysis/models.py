from django.db import models

class TrafficRecord(models.Model):
    vehicle_count = models.IntegerField()
    road_length = models.FloatField()
    density = models.FloatField()
    traffic_level = models.CharField(max_length=10)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.traffic_level} traffic ({self.density})"