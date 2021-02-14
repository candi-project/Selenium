from datetime import datetime
from twilio.rest import Client

account_sid = "AC2ae530cc6c5436d28bb2dfa90fc0538e"
auth_token = "cc3242a55e75b7a862064d8cbbaf85cf"
MY_TWILIO_NUMBER = "+12018796450"


def get_verification_code():
    client = Client(account_sid, auth_token)
    received = client.messages.list(
        date_sent=datetime(2021, 2, 14, 0, 0, 0),
        from_='+1(650)215-6993',
        to=MY_TWILIO_NUMBER,
        limit=1
    )

    for message in received:
        text = message.body
        #print(text)
        verification_code = text[0:6]
        print(verification_code)
        return verification_code

co = get_verification_code()
# verification_code = int(re.search(r'\d+', message.body).group())
# str_verification_code = str(verification_code)
# print(verification_code)
