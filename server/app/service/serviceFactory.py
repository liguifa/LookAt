from .userService import UserService

class ServiceFactory:

	@property
	def userService(self):
		return UserService()