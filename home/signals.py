from django.dispatch import receiver
from django.db.models.signals import pre_save
from django.contrib.auth.models import User
from .models import SignalDetails
import threading

# Uncomment this for the first Question
# @receiver(pre_save, sender=User)
# def user_pre_save_signal(sender, instance, **kwargs):
#     print("Signal handler executed")


# Uncomment this for the second question
# @receiver(pre_save, sender=User)
# def user_pre_save_signal(sender, instance, **kwargs):
#     print(f"Signal handler thread ID: {threading.get_ident()}")


@receiver(pre_save, sender=User)
def user_pre_save_signal(sender, instance, **kwargs):
    SignalDetails.objects.create(message="Signal handler executed")
