from django.conf import settings
from django.core.mail import send_mail
from django.core.exceptions import ObjectDoesNotExist
from .models import Person

def simple_middleware(get_response):
    print('simple middleware is running')

    def middleware(request):
        if request.method == 'POST':
            username = request.POST.get('username')
            email = request.POST.get('email')

            if username and email:
                try:
                    p = Person.objects.get(username=username)
                    otp = str(p.otp)
                    email_form = settings.EMAIL_HOST_USER
                    recipients_list = [email]

                    send_mail(
                        subject=otp,
                        message='Your OTP code',
                        from_email=email_form,
                        recipient_list=recipients_list,
                    )
                except ObjectDoesNotExist:
                    print("User does not exist")
                    # Handle user not found case

        response = get_response(request)
        print('after view')
        return response

    return middleware
