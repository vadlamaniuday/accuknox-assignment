from django.http import HttpResponse
from django.contrib.auth.models import User
from django.db import transaction
import threading

# Uncomment this for the first QUestion
# def trigger_signal_view(request):
#     user = User.objects.first() or User.objects.create_user(
#         username="test_user", password="test_password"
#     )
#     print("Before Signal Triggered")
#     user.save()
#     print("After Signal Triggered")
#     return HttpResponse("Signal triggered")


# Uncomment this for the second QUestion
# def trigger_signal_view(request):
#     user = User.objects.first() or User.objects.create_user(
#         username="test_user", password="test_password"
#     )
#     print(f"View thread ID: {threading.get_ident()}")
#     user.save()
#     return HttpResponse("Signal triggered")


def trigger_signal_view(request):
    with transaction.atomic():
        user = User.objects.first()
        user.save()
    return HttpResponse("Signal triggered")
