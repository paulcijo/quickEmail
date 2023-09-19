from dotenv import load_dotenv
from emailer import EmailMessage, Emailer

class App:

	def start(self):
		load_dotenv()


	def send_email(self, to: str ="", recipient_email: str = "", subject: str = "", message: str = ""):
		email = EmailMessage(fromVal=recipient_email, to=to, body=message, subject = subject)
		emailer = Emailer(email)
		emailer.send_email()


if __name__ == '__main__':
	app = App()

	app.start()
	app.send_email(to="pl.cijo@gmail.com", recipient_email="pl.cijo@gmail.com", 
		subject = "From CIJO", message="Hello from the script")