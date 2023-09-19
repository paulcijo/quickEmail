from tasks import send_email

from emailer import EmailMessage

class App:
	def start(self):
		send_email.delay(recipient = "pl.cijo@gmail.com",
			to = "pl.cijo@gmail.com",
			body = "Hey there",
			subject = "Checking this from my machine")


if __name__ == "__main__":
	App().start()