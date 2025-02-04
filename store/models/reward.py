from django.db import models
from .user import CustomUser
from .payment import Payment  # Link to Payment model
from datetime import datetime

class RewardPayment(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    phone_number = models.CharField(max_length=15)
    amount = models.PositiveIntegerField()  # Amount of reward or prize
    transaction_id = models.CharField(max_length=100, unique=True, null=True, blank=True)
    is_successful = models.BooleanField(default=False)
    reward = models.CharField(max_length=50, null=True, blank=True)  # Reward details
    payment = models.OneToOneField(Payment, on_delete=models.CASCADE, related_name="payment", null=True, blank=True)  # Make it nullable
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.transaction_id} - {'Success' if self.is_successful else 'Failed'}"
