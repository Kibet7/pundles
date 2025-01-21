import requests
import base64
from datetime import datetime
from django.conf import settings

def generate_mpesa_token():
    """Generate M-Pesa API access token."""
    url = "https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials"
    consumer_key = settings.MPESA_CONSUMER_KEY
    consumer_secret = settings.MPESA_CONSUMER_SECRET
    response = requests.get(url, auth=(consumer_key, consumer_secret))
    
    if response.status_code == 200:
        return response.json().get('access_token')
    else:
        raise Exception(f"Failed to generate token: {response.text}")

def generate_timestamp():
    """Generate current timestamp for M-Pesa request."""
    return datetime.now().strftime("%Y%m%d%H%M%S")

def generate_password(shortcode, passkey):
    """Generate password using shortcode, passkey, and timestamp."""
    timestamp = generate_timestamp()
    password_str = f"{shortcode}{passkey}{timestamp}"
    return base64.b64encode(password_str.encode()).decode()

def initiate_mpesa_payment(phone_number, amount, callback_url):
    """Initiate M-Pesa STK push payment."""
    token = generate_mpesa_token()
    if not token:
        return {"error": "Failed to generate token"}

    url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
    headers = {"Authorization": f"Bearer {token}"}
    payload = {
        "BusinessShortCode": settings.BUSINESS_SHORTCODE,
        "Password": generate_password(settings.BUSINESS_SHORTCODE, settings.MPESA_PASSKEY),
        "Timestamp": generate_timestamp(),
        "TransactionType": "CustomerPayBillOnline",
        "Amount": amount,
        "PartyA": phone_number,
        "PartyB": settings.BUSINESS_SHORTCODE,
        "PhoneNumber": phone_number,
        "CallBackURL": callback_url,
        "AccountReference": "Lucky Box",
        "TransactionDesc": "Payment for lucky box"
    }

    response = requests.post(url, json=payload, headers=headers)
    return response.json()
