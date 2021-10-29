from twilio.rest import Client 

class Messaging:
    @classmethod
    def send_sms(cls, data):
        with open ("./flask_app/static/files/twilio.key", "r") as key:
            twilio_key=(key.read()).strip()
        with open ("./flask_app/static/files/twilio.sid", "r") as messaging_sid:
            twilio_sid=(messaging_sid.read()).strip()
        account_sid = twilio_sid
        auth_token = twilio_key
        client = Client(account_sid, auth_token)

        print('***  1000A  ***', twilio_sid, twilio_key, data['phone'])
        message = client.messages.create(
            to=data['phone'],
            from_="+13206264345",
            body=data['message']
        )
        print('message created')
        return(message.sid)