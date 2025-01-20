# from django.contrib.auth.signals import user_logged_in, user_logged_out,user_login_failed
# from django.dispatch import receiver
# from django.contrib.auth.models import User

# @receiver(user_logged_in,sender=User)
# def login_ip_address(sender, request, user, **kwargs):
#     ip = request.META.get('REMOTE_ADDR')
#     request.session['ip']=ip