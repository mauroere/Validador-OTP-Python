const express = require('express');
const { authenticator } = require('otplib');
const twilio = require('twilio');
const path = require('path');

const app = express();
const port = 3000;

app.use(express.json());
app.use(express.static('public'));

// Load configuration
const config = {
  secret: process.env.OTP_SECRET || 'ThisIsASecretKey',
  interval: 30,
  tolerance: 1,
  twilioAccountSid: process.env.TWILIO_ACCOUNT_SID || '',
  twilioAuthToken: process.env.TWILIO_AUTH_TOKEN || '',
  twilioPhoneNumber: process.env.TWILIO_PHONE_NUMBER || '',
  whatsappNumberId: process.env.WHATSAPP_NUMBER_ID || ''
};

app.get('/', (req, res) => {
  res.sendFile(path.join(__dirname, 'public', 'index.html'));
});

app.post('/generate-otp', (req, res) => {
  const { secret = config.secret } = req.body;
  authenticator.options = { step: config.interval };
  const otp = authenticator.generate(secret);
  res.json({ otp });
});

app.post('/validate-otp', (req, res) => {
  const { secret = config.secret, otp } = req.body;
  authenticator.options = { step: config.interval };
  const isValid = authenticator.verify({ token: otp, secret });
  res.json({ valid: isValid });
});

app.post('/send-sms', (req, res) => {
  const { phoneNumber, otp } = req.body;
  
  if (!config.twilioAccountSid || !config.twilioAuthToken) {
    return res.json({ success: false, error: 'Twilio credentials not configured' });
  }

  const client = twilio(config.twilioAccountSid, config.twilioAuthToken);
  
  client.messages.create({
    body: `Your OTP is: ${otp}`,
    to: phoneNumber,
    from: config.twilioPhoneNumber
  })
  .then(() => res.json({ success: true }))
  .catch(error => res.json({ success: false, error: error.message }));
});

app.post('/send-whatsapp', (req, res) => {
  const { phoneNumber, otp } = req.body;
  
  if (!config.twilioAccountSid || !config.twilioAuthToken) {
    return res.json({ success: false, error: 'Twilio credentials not configured' });
  }

  const client = twilio(config.twilioAccountSid, config.twilioAuthToken);
  
  client.messages.create({
    body: `Your OTP is: ${otp}`,
    to: `whatsapp:${phoneNumber}`,
    from: `whatsapp:${config.whatsappNumberId}`
  })
  .then(() => res.json({ success: true }))
  .catch(error => res.json({ success: false, error: error.message }));
});

app.listen(port, () => {
  console.log(`OTP Validador esta ejecutandose en http://localhost:${port}`);
});