from mailjet_rest import Client

from data.config import API_KEY as api_key
from data.config import API_SECRET as api_secret

from data.config import (
    SENDER_GMAIL, SENDER_NAME,
    RECIPIENT_GMAIL, RECIPIENT_NAME
)


class SendMail:
    def __init__(self, api_key, api_secret):
        self.api_key = api_key
        self.api_secret = api_secret
    
    def send_mail(self, subject, text_part):
        mailjet = Client(auth=(self.api_key, self.api_secret), version='v3.1')

        data = {
        'Messages': [
            {
            "From": {
                "Email": SENDER_GMAIL,
                "Name": SENDER_NAME
            },
            "To": [
                {
                "Email": RECIPIENT_GMAIL,
                "Name": RECIPIENT_NAME
                }
            ],
            "Subject": subject,
            "TextPart": text_part,
            "HTMLPart": text_part,
            "CustomID": "AppGettingStartedTest"
            }
        ]
        }

        result = mailjet.send.create(data=data)
        return result
        