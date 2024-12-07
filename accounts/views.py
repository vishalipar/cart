from django.shortcuts import render

# Create your views here.

from django.contrib import auth, messages
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.shortcuts import redirect, render
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_decode, urlsafe_base64_encode
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
# <<<<<<< HEAD


# from cart.models import Cart
# =======
# from cart.models import Cart
# >>>>>>> caf6102fd222ff60697431bf4ce4180c679b7ff9

from .forms import RegistrationForm
from .models import Account

# Create your views here.

# Create your views here.
def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)        
        if form.is_valid():
            
            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            username = email.split('@')[0]
            type = form.cleaned_data['type']
            user = Account.objects.create_user(first_name=first_name,last_name=last_name,email=email,password=password,type=type,username=username)
            user.phone_number = phone_number
            user.save()
            
            # USER ACTIVATION email sending
            current_site = get_current_site(request)
            mail_subject = 'Please activate your account'
            message = render_to_string('accounts/acount_verification_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            # business login
            if user.type == 'business':
                return redirect('/accounts/login/business_login/?command=verification&email=',+email)
            
            return redirect('/accounts/login/?command=verification&email='+email)
        else:
            print('form is invalid',form.errors)
        
    else:
        form = RegistrationForm()
    context = {
        'form':form,
    }
    return render(request, 'accounts/register.html', context)
 