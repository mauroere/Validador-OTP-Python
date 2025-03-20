from twilio.rest import Client
import config

def send_whatsapp(to_number, message):
    cfg = config.load_config()
    account_sid = cfg["twilio_account_sid"]
    auth_token = cfg["twilio_auth_token"]
    whatsapp_number_id = cfg["whatsapp_phone_number_id"]

    client = Client(account_sid, auth_token)

    try:
        message = client.messages.create(
            to=f"whatsapp:{to_number}",
            from_=f"whatsapp:{whatsapp_number_id}",
            body=message
        )
        print(f"WhatsApp message sent with SID: {message.sid}")
        return True
    except Exception as e:
        print(f"Error sending WhatsApp message: {e}")
        return False