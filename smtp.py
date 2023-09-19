from abc import abstractmethod
import os
import smtplib

class SMTP:

	@abstractmethod
	def get_server():
		server = smtplib.SMTP(os.getenv("SMTP_HOST"), os.getenv("SMTP_PORT"))
		server.starttls()
		server.login(os.getenv("SMTP_USERNAME"), os.getenv("SMTP_PASSWORD"))
		return server

	@abstractmethod
	def close(server):
		server.quit()