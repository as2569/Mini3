class Calculator:
	def add(self, num1, num2):
		return num1 + num2

	def sub(self, num1, num2):
		return num1 - num2

	def mul(self, num1, num2):
		return num1 * num2

	def div(self, num1, num2):
		return round(num1 / num2, 3)

	def sqr(self, num1):
		return round(num1 * num1, 3)

	def sqrRoot(self, num1):
		return round(num1 ** (1/2), 3)

