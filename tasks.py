from emailer import EmailMessage, Emailer

from celery_main import app

@app.task(bind = True)
def send_email(self, recipient: str, to: str, body: str, subject: str):
	emailMessage = EmailMessage(fromVal = recipient, to = to, body = body, subject = subject)
	emailer = Emailer(emailMessage)
	try: 
		emailer.send_email()
	except Exception as exc:
		raise self.retry(exc=exc)
	