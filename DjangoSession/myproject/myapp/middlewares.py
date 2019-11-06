from .models import myDetails

class BookMiddleware(object):
	def process_request(self, request):
		print("Middleware executed")