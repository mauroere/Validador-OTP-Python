from twilio.rest import Client
import config

def send_sms(to_number, message):
    cfg = config.load_config()
    account_sid = cfg["twilio_account_sid"]
    auth_token = cfg["twilio_auth_token"]
    twilio_number = cfg["twilio_phone_number"]

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            to=to_number,
            from_=twilio_number,
            body=message
        )
        print(f"SMS sent with SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Error sending SMS: {e}")
        return False