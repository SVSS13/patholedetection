from django.db import models

class TransportLog(models.Model):
    original_speed = models.FloatField()
    adjusted_speed = models.FloatField()
    traffic_level = models.CharField(max_length=10)
    risk_level = models.CharField(max_length=10)
    eta = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"ETA: {self.eta}, Speed: {self.adjusted_speed}"