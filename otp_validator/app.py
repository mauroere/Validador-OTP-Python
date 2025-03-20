from flask import Flask, render_template, request, jsonify
import pyotp
import config
import sms_sender
import whatsapp_sender

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/generate-otp', methods=['POST'])
def generate_otp():
    data = request.get_json()
    secret = data.get('secret', config.DEFAULT_CONFIG['secret'])
    interval = int(data.get('interval', config.DEFAULT_CONFIG['interval']))
    
    totp = pyotp.TOTP(secret, interval=interval)
    otp = totp.now()
    return jsonify({'otp': otp})

@app.route('/send-sms', methods=['POST'])
def send_sms():
    data = request.get_json()
    phone_number = data.get('phone_number')
    otp = data.get('otp')
    
    if not phone_number or not otp:
        return jsonify({'success': False, 'error': 'Missing phone number or OTP'})
    
    message = f"Your OTP is: {otp}"
    success = sms_sender.send_sms(phone_number, message)
    return jsonify({'success': success})

@app.route('/send-whatsapp', methods=['POST'])
def send_whatsapp():
    data = request.get_json()
    phone_number = data.get('phone_number')
    otp = data.get('otp')
    
    if not phone_number or not otp:
        return jsonify({'success': False, 'error': 'Missing phone number or OTP'})
    
    message = f"Your OTP is: {otp}"
    success = whatsapp_sender.send_whatsapp(phone_number, message)
    return jsonify({'success': success})

@app.route('/validate-otp', methods=['POST'])
def validate_otp():
    data = request.get_json()
    secret = data.get('secret', config.DEFAULT_CONFIG['secret'])
    otp = data.get('otp')
    interval = int(data.get('interval', config.DEFAULT_CONFIG['interval']))
    tolerance = int(data.get('tolerance', config.DEFAULT_CONFIG['tolerance']))
    
    if not otp:
        return jsonify({'valid': False, 'error': 'Missing OTP'})
    
    totp = pyotp.TOTP(secret, interval=interval)
    is_valid = totp.verify(otp, tolerance=tolerance)
    return jsonify({'valid': is_valid})

@app.route('/save-config', methods=['POST'])
def save_config():
    try:
        data = request.get_json()
        config.save_config(data)
        return jsonify({'success': True})
    except Exception as e:
        return jsonify({'success': False, 'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)