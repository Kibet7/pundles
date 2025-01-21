import random
from django.shortcuts import render
from django.http import JsonResponse
from store.models.payment import Payment
from store.models.reward import RewardPayment
from store.mpesa import initiate_mpesa_payment  # Function to handle M-Pesa
from django.contrib.auth.decorators import login_required

@login_required
def lucky_box(request):
    if request.method == 'POST':
        phone_number = request.POST.get('phone_number')
        box_choice = request.POST.get('box_choice')

        if box_choice not in ['1', '2', '3']:
            return JsonResponse({'error': 'Invalid box choice'}, status=400)

        payment_response = initiate_mpesa_payment(phone_number, amount=42)
        if payment_response.get("ResponseCode") == "0":
            reward = get_weighted_reward()
            return JsonResponse({'message': f'Payment successful! Your reward is: {reward}.'})
        else:
            return JsonResponse({'error': 'Payment initiation failed. Try again.'}, status=400)
    return render(request, 'store/lucky_box.html')

def get_weighted_reward():
    """Select a reward based on weighted probabilities."""
    rewards = [
        ("Ksh.10", 70),
        ("Ksh.50", 20),
        ("Ksh.200", 9),
        ("Ksh.1000", 1)
    ]
    population, weights = zip(*rewards)
    return random.choices(population, weights, k=1)[0]
