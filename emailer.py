class EmailMessage:

	def __init__(fromVal: str, to: str, body: str, reply_to: str, cc: str, bcc: str):
		self.__body = body
		self.__from = fromVal
		self.__to = to
		self.__cc = cc
		self.__bcc = bcc
		self.__reply_to = reply_to


	@property
	def __body(self):
		return self.___body
	

	@property
	def __from(self):
		return self.__from

	@property
	def __to(self):
		return self.___to
	
	@property
	def __cc(self):
		return self.___cc
	
	@property
	def __bcc(self):
		return self.___bcc

	@property
	def __reply_to(self):
		return self.___reply_to
	

class Emailer:

	def __init__(self, email: EmailMessage):
		self._email = email


	def send_email() -> bool:
		pass