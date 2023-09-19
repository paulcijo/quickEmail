from smtp import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

class EmailMessage:

	def __init__(self, fromVal: str="", to: str="", body: str="", subject: str="", reply_to: str="", cc: str="", bcc: str=""):
		self.body = body
		self.recipient = fromVal
		self.to = to
		self.subject = subject
		self.cc = cc
		self.bcc = bcc
		self.reply_to = reply_to
	
	def get_message(self) -> str:
		message = MIMEMultipart()
		message["From"] = self.recipient
		message["To"] = self.to
		message["Subject"] = self.subject
		message['Reply-To'] = self.reply_to
		message.attach(MIMEText(self.body, "text/html"))
		return message.as_string()
	

class Emailer:

	def __init__(self, email: EmailMessage):
		self._email = email
		self._smtp_server = SMTP.get_server()


	def send_email(self) -> bool:
		self._smtp_server.sendmail(self._email.recipient, self._email.to, self._email.get_message())
		return true