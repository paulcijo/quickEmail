from abc import abstractmethod
import os
import smtplib

class SMTP:

	server = None

	@abstractmethod
	def get_server():
		if not SMTP.server:
			SMTP.server = smtplib.SMTP(os.getenv("SMTP_HOST"), os.getenv("SMTP_PORT"))
			SMTP.server.starttls()
			SMTP.server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
		return SMTP.server

	def __del__(self):
		if SMTP.server:
			SMTP.server.quit()