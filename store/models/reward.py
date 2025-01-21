# store/models/reward.py
from django.db import models
from .user import CustomUser 
from datetime import datetime

class RewardPayment(models.Model):  # Renamed from Payment to RewardPayment
    user = models.ForeignKey(CustomUser , on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    amount = models.PositiveIntegerField()
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    is_successful = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.user.username} - {self.transaction_id} - {'Success' if self.is_successful else 'Failed'}"