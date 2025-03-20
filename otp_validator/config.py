import json
import os

CONFIG_FILE = "config.json"
DEFAULT_CONFIG = {
    "secret": "ThisIsASecretKey",
    "interval": 30,
    "tolerance": 1,
    "twilio_account_sid": "",
    "twilio_auth_token": "",
    "twilio_phone_number": "",
    "whatsapp_phone_number_id": ""
}

def load_config():
    if os.path.exists(CONFIG_FILE):
        with open(CONFIG_FILE, "r") as f:
            return json.load(f)
    else:
        return DEFAULT_CONFIG

def save_config(config):
    with open(CONFIG_FILE, "w") as f:
        json.dump(config, f, indent=4)