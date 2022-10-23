from creds import twilio_sid, twilio_auth_token, twilio_verify_sid
from twilio.rest import Client

client = Client(twilio_sid, twilio_auth_token)
verify = client.verify.services(twilio_verify_sid)

def send_verification(number):
    verify.verifications.create(to=number, channel='sms')

def check_verification(phone_number, new_code):
    return verify.verification_checks.create(to=phone_number, code=new_code).status
