# OTP Validator

A Python application for generating, sending, and validating One-Time Passwords (OTP) using SMS and WhatsApp.

## Features

- Generate TOTP (Time-based One-Time Password)
- Send OTP via SMS using Twilio
- Send OTP via WhatsApp using Twilio WhatsApp Business API
- Validate OTP with configurable interval and tolerance
- Save and load configuration

## Requirements

- Python 3.x
- Dependencies listed in requirements.txt

## Installation

1. Clone or download this repository
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

1. Open the application
2. Enter your Twilio credentials:
   - Account SID
   - Auth Token
   - Twilio Phone Number
   - WhatsApp Number ID (for WhatsApp functionality)
3. Click "Save Configuration" to store your settings

## Usage

1. Run the application:
   ```bash
   python otp_validator.py
   ```
2. Enter the recipient's phone number
3. Click "Send OTP via SMS" or "Send OTP via WhatsApp"
4. Enter the received OTP
5. Click "Validate OTP" to verify

## Security Notes

- Keep your Twilio credentials secure
- Never share your secret key
- Use strong secret keys for OTP generation