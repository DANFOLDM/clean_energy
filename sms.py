import africastalking
import os
from africastalking import SMS
from dotenv import load_dotenv


load_dotenv('load.env')


class SMSNotifier:
    def __init__(self):
        self.username = "RayHackathon1"
        self.api_key = os.getenv('API_KEY')
        africastalking.initialize(self.username, self.api_key)
        self.sms = africastalking.SMS()

    def send(self, phone_number, message):
        try:
            response = self.sms.send(message, [phone_number], "20880")
            print(response)
            return True
        except Exception as e:
            print(f'Encountered an error while sending sms: {str(e)}')
            return False


sms_notifier = SMSNotifier()
