from django.apps import AppConfig
from django.core.signals import request_finished

class NewappConfig(AppConfig):
	default_auto_field = 'django.db.models.BigAutoField'
	name = 'newApp'

	def ready(self):
		# Implicitly connect a signal handlers decorated with @receiver.
		from . import signals
		# Explicitly connect a signal handler.
		request_finished.connect(signals.my_callback)