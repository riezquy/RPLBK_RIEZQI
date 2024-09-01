# Modul tingkat rendah
class EmailService:
    def send_email(self, message):
        print(f"Sending email: {message}")

# Modul tingkat tinggi
class Notification:
    def __init__(self):
        self.email_service = EmailService()  # Ketergantungan langsung pada EmailService
    
    def send(self, message):
        self.email_service.send_email(message)

# Menggunakan kelas tanpa DIP
notification = Notification()
notification.send("Hello, this is a notification!")
