from twilio import TwilioRestException
from twilio import rest

account_sid = ""  # Your Account SID from www.twilio.com/console
auth_token  = ""  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

try:
    message = client.messages.create(body="Hello from Python",
        to="",     # Replace with your phone number
        from_="")  # Replace with your Twilio number
except TwilioRestException as e:
    print(e)

print(message.sid)

