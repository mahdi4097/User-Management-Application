class Response:
	def __init__(self, data: tuple | None, success: bool, response_code: int, message: str = None) -> None:
		self.data = data
		self.success = success
		self.response_code = response_code
		self.message = message
