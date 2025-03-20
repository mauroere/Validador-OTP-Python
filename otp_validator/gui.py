import tkinter as tk
from tkinter import messagebox
import pyotp
import config
import sms_sender
import whatsapp_sender

class OTPValidatorGUI:
    def __init__(self, master):
        self.master = master
        master.title("OTP Validador")

        self.config = config.load_config()

        # Secret Key
        self.secret_label = tk.Label(master, text="Secret Key:")
        self.secret_label.grid(row=0, column=0, sticky="W")
        self.secret_entry = tk.Entry(master, width=40)
        self.secret_entry.grid(row=0, column=1, sticky="EW")
        self.secret_entry.insert(0, self.config["secret"])

        # OTP Input
        self.otp_label = tk.Label(master, text="OTP:")
        self.otp_label.grid(row=1, column=0, sticky="W")
        self.otp_entry = tk.Entry(master, width=10)
        self.otp_entry.grid(row=1, column=1, sticky="W")

        # Interval
        self.interval_label = tk.Label(master, text="Interval (seconds):")
        self.interval_label.grid(row=2, column=0, sticky="W")
        self.interval_entry = tk.Entry(master, width=5)
        self.interval_entry.grid(row=2, column=1, sticky="W")
        self.interval_entry.insert(0, self.config["interval"])

        # Tolerance
        self.tolerance_label = tk.Label(master, text="Tolerance (intervals):")
        self.tolerance_label.grid(row=3, column=0, sticky="W")
        self.tolerance_entry = tk.Entry(master, width=5)
        self.tolerance_entry.grid(row=3, column=1, sticky="W")
        self.tolerance_entry.insert(0, self.config["tolerance"])

        # Phone Number
        self.phone_label = tk.Label(master, text="Phone Number:")
        self.phone_label.grid(row=4, column=0, sticky="W")
        self.phone_entry = tk.Entry(master, width=20)
        self.phone_entry.grid(row=4, column=1, sticky="W")

        # Send OTP via SMS Button
        self.send_sms_button = tk.Button(master, text="Send OTP via SMS", command=self.send_otp_sms)
        self.send_sms_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Send OTP via WhatsApp Button
        self.send_whatsapp_button = tk.Button(master, text="Send OTP via WhatsApp", command=self.send_otp_whatsapp)
        self.send_whatsapp_button.grid(row=6, column=0, columnspan=2, pady=5)

        # Validate Button
        self.validate_button = tk.Button(master, text="Validate OTP", command=self.validate_otp)
        self.validate_button.grid(row=7, column=0, columnspan=2, pady=5)

        # Configuración Twilio (solo si usas Twilio)
        self.twilio_account_sid_label = tk.Label(master, text="Twilio Account SID:")
        self.twilio_account_sid_label.grid(row=8, column=0, sticky="W")
        self.twilio_account_sid_entry = tk.Entry(master, width=40)
        self.twilio_account_sid_entry.grid(row=8, column=1, sticky="EW")
        self.twilio_account_sid_entry.insert(0, self.config["twilio_account_sid"])

        self.twilio_auth_token_label = tk.Label(master, text="Twilio Auth Token:")
        self.twilio_auth_token_label.grid(row=9, column=0, sticky="W")
        self.twilio_auth_token_entry = tk.Entry(master, width=40, show="*")
        self.twilio_auth_token_entry.grid(row=9, column=1, sticky="EW")
        self.twilio_auth_token_entry.insert(0, self.config["twilio_auth_token"])

        self.twilio_phone_number_label = tk.Label(master, text="Twilio Phone Number:")
        self.twilio_phone_number_label.grid(row=10, column=0, sticky="W")
        self.twilio_phone_number_entry = tk.Entry(master, width=20)
        self.twilio_phone_number_entry.grid(row=10, column=1, sticky="W")
        self.twilio_phone_number_entry.insert(0, self.config["twilio_phone_number"])

        # WhatsApp Phone Number ID (si usas Twilio WhatsApp Business)
        self.whatsapp_phone_number_id_label = tk.Label(master, text="WhatsApp Number ID:")
        self.whatsapp_phone_number_id_label.grid(row=11, column=0, sticky="W")
        self.whatsapp_phone_number_id_entry = tk.Entry(master, width=40)
        self.whatsapp_phone_number_id_entry.grid(row=11, column=1, sticky="EW")
        self.whatsapp_phone_number_id_entry.insert(0, self.config["whatsapp_phone_number_id"])

        # Save Configuration
        self.save_config_button = tk.Button(master, text="Save Configuration", command=self.save_config)
        self.save_config_button.grid(row=12, column=0, columnspan=2, pady=5)

    def generate_otp(self):
        secret = self.secret_entry.get()
        interval = int(self.interval_entry.get())
        totp = pyotp.TOTP(secret, interval=interval)
        otp = totp.now()
        return otp

    def send_otp_sms(self):
        phone_number = self.phone_entry.get()
        otp = self.generate_otp()
        message = f"Your OTP is: {otp}"
        if sms_sender.send_sms(phone_number, message):
            messagebox.showinfo("SMS Sent", "OTP sent via SMS!")
        else:
            messagebox.showerror("Error", "Failed to send SMS.")

    def send_otp_whatsapp(self):
        phone_number = self.phone_entry.get()
        otp = self.generate_otp()
        message = f"Your OTP is: {otp}"
        if whatsapp_sender.send_whatsapp(phone_number, message):
            messagebox.showinfo("WhatsApp Sent", "OTP sent via WhatsApp!")
        else:
            messagebox.showerror("Error", "Failed to send WhatsApp message.")

    def validate_otp(self):
        secret = self.secret_entry.get()
        otp = self.otp_entry.get()
        interval = int(self.interval_entry.get())
        tolerance = int(self.tolerance_entry.get())
        totp = pyotp.TOTP(secret, interval=interval)
        is_valid = totp.verify(otp, tolerance=tolerance)
        if is_valid:
            messagebox.showinfo("Validation Result", "OTP is valid!")
        else:
            messagebox.showerror("Validation Result", "OTP is invalid.")

    def save_config(self):
        try:
            secret = self.secret_entry.get()
            interval = int(self.interval_entry.get())
            tolerance = int(self.tolerance_entry.get())
            twilio_account_sid = self.twilio_account_sid_entry.get()
            twilio_auth_token = self.twilio_auth_token_entry.get()
            twilio_phone_number = self.twilio_phone_number_entry.get()
            whatsapp_phone_number_id = self.whatsapp_phone_number_id_entry.get()

            config_data = {
                "secret": secret,
                "interval": interval,
                "tolerance": tolerance,
                "twilio_account_sid": twilio_account_sid,
                "twilio_auth_token": twilio_auth_token,
                "twilio_phone_number": twilio_phone_number,
                "whatsapp_phone_number_id": whatsapp_phone_number_id
            }
            config.save_config(config_data)
            messagebox.showinfo("Configuration Saved", "Configuration saved successfully!")
        except ValueError:
            messagebox.showerror("Error", "Invalid input. Please check your values.")