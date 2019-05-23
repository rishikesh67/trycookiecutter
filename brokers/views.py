from django.shortcuts import render
from .send_mb_mail import send_mb_mail

# Create your views here.
def send_mail(request):
	print("Mail successfully sent")
	send_mb_mail("mail-template1", ["rishikesh@moneybloom.in"])

	return render(request, "brokers/index.html", {})

