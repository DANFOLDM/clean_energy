import africastalking

class SMS:
    def __init__(self):
    # Set your app credentials
      self.username = "RayHackathon1"
      self.api_key = "atsk_f912cbd6d3e25a8277b0f5b0052db6484777ffbe01aa2fa010690c1202debcf4e8479960"

        # Initialize the SDK
      africastalking.initialize(self.username, self.api_key)

        # Get the SMS service
      self.sms = africastalking.SMS

    def send(self):
            # Set the numbers you want to send to in international format
            recipients = ["+254715067724"]

            # Set your message
            message = "Hey ,Sr Eng Ray welcome to Candit-Pesa, your betting genius, your OTP is **** ";

            # Set your shortCode or senderId
            sender = "20880"
            try:
        # Thats it, hit send and we'll take care of the rest.
                response = self.sms.send(message, recipients, sender)
                print (response)
            except Exception as e:
                print ('Encountered an error while sending: %s' % str(e))


if __name__ == '__main__':
    SMS().send()
