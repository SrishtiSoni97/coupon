import os
# from twilio.rest import Client

def send_whatsapp_otp(phone_number, otp):
    """
    Sends OTP via WhatsApp using Twilio or similar service.
    Mocked for development.
    """
    print(f"========================================")
    print(f"SENDING WHATSAPP OTP TO {phone_number}: {otp}")
    print(f"========================================")
    
    # Real implementation would be:
    # client = Client(os.environ['TWILIO_ACCOUNT_SID'], os.environ['TWILIO_AUTH_TOKEN'])
    # message = client.messages.create(
    #     body=f"Your verification code is {otp}",
    #     from_=f"whatsapp:{os.environ['TWILIO_WHATSAPP_NUMBER']}",
    #     to=f"whatsapp:{phone_number}"
    # )
    return True
