# Abstraksi (Interface)
class MessageService:
    def send_message(self, message):
        pass

# Modul tingkat rendah
class EmailService(MessageService):
    def send_message(self, message):
        print(f"Sending email: {message}")

# Modul tingkat rendah lainnya
class SMSService(MessageService):
    def send_message(self, message):
        print(f"Sending SMS: {message}")

# Modul tingkat tinggi
class Notification:
    def __init__(self, message_service: MessageService):
        self.message_service = message_service  # Bergantung pada abstraksi
    
    def send(self, message):
        self.message_service.send_message(message)

# Menggunakan kelas dengan DIP
email_service = EmailService()
notification_via_email = Notification(email_service)
notification_via_email.send("Hello, this is an email notification!")

# Contoh menggunakan SMS
sms_service = SMSService()
notification_via_sms = Notification(sms_service)
notification_via_sms.send("Hello, this is an SMS notification!")
