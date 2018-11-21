import bcrypt

class PasswordHasher():
	
	def hashPassword(password):
		return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
	
	def verifyPassword(password, encodedPassword):
		return bcrypt.checkpw(password.encode('utf-8'), encodedPassword.encode('utf-8'))