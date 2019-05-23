from django.urls import path
from .views import send_mail

app_name = "brokers";

urlpatterns = [
	path("send/mail/", send_mail, {})
]