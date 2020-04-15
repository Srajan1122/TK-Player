from decouple import config
from twilio.rest import Client as TwilioClient
account_sid = config('account_sid')
auth_token = config('auth_token')
twilio_phone = config("twilio_phone")
client = TwilioClient(account_sid, auth_token)

user_phone_number = "+919145253235"
client.messages.create(
                     body="Your verification code is "+'123456',
                     from_=twilio_phone,
                     to=user_phone_number
                 )