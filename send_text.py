from twilio.rest import TwilioRestClient

account_sid = "ACbfb329a7ef60c450b297d35fc90c61b5" # Your Account SID from www.twilio.com/console
auth_token  = "867f55f9f0931edbc656af1815d9db2b"  # Your Auth Token from www.twilio.com/console

client = TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="I am going to become a code reviewer",
    to="+447572986245",    # Replace with your phone number
    from_="+441233801264") # Replace with your Twilio number

print(message.sid)