from django.shortcuts import render
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
# from cart.models import Cart

from .forms import RegistrationForm
from .models import Account

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

   
def activate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError, ValueError, OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        user.is_active = True
        user.save()
        messages.success(request, "Your account is activated.")
        
        return redirect('login')
        
    else:
        messages.error(request, 'Invalid activation link')
        return redirect('register')
            
    
def login(request):   
    if request.method == 'POST': 
        email = request.POST['email']
        password = request.POST['password']
        user = auth.authenticate(email=email, password=password)
        
        # print(password, email, user)
        
        if user is not None:
            auth.login(request, user)
            return redirect('home')
        else:
            messages.error(request, 'Invalid login credentials.')
            return redirect('login')
            
    # if request.method == 'POST':
    #     email = request.POST['email']
    #     password = request.POST['password']
    #     user = auth.authenticate(email=email, password=password)
        
    #     # for business accounts
    #     # print(user.type)
        
    #     # if user.type == 'business':
    #     #     return render(request, '')
            
    #     # *
        
    #     if user is not None:
    #         if user.type == 'user':
    #             try:
    #                 cart = Cart.objects.get(cart_id=_cart_id(request))
    #                 is_cart_item_exists = CartItem.objects.filter(cart=cart).exists()
    #                 if is_cart_item_exists:
    #                     cart_item = CartItem.objects.filter(cart=cart)
                        
    #                     # getting product_variation by cart id
    #                     product_variation = []
    #                     for item in cart_item:
    #                         variation = item.variations.all()
    #                         product_variation.append(list(variation))
                            
    #                         # get the cart items from the user to access his product_variation
    #                         cart_item = CartItem.objects.filter(user=user)
    #                         ex_var_list = []
    #                         id = []
    #                         for item in cart_item:
    #                             existing_variation = item.variations.all()
    #                             ex_var_list.append(list(existing_variation))
    #                             id.append(item.id)
                            
    #                         # product_variation = [1,2,3,4,6]
    #                         # ex_var_list = [4,6,3,5]
                                
    #                         for pr in product_variation:
    #                             if pr in ex_var_list:
    #                                 index = ex_var_list.index(pr)
    #                                 item_id = id[index]
    #                                 item = CartItem.objects.get(id=item_id)
    #                                 item.quantity += 1
    #                                 item.user = user
    #                                 item.save()
    #                             else:
    #                                 cart_item = CartItem.objects.filter(cart=cart)
    #                                 for item in cart_item:
    #                                     item.user = user
    #                                     item.save()
    #             except:
    #                 pass
    #             auth.login(request, user)
    #             messages.success(request, "You are now logged in.")
    #             url = request.META.get('HTTP_REFERER')
    #             try:
    #                 query = requests.utils.urlparse(url).query
    #                 params = dict(x.split('=') for x in query.split('&'))
    #                 if 'next' in params:
    #                     nextPage = params['next']
    #                     return redirect(nextPage)
    #             except:
    #                 return redirect('home')
            
    #         else:
    #             messages.error(request, "You registered as business account")
    #             return redirect('login')
            
            
    #     else:
    #         messages.error(request, "Invalid login credentials")
    #         return redirect("login")
    
    return render(request, 'accounts/login.html')
    
  
def forgotPassword(request):
    if request.method == 'POST':
        email = request.POST['email']
        if Account.objects.filter(email=email).exists():
            user = Account.objects.get(email__exact = email)
            
            # FORGOT PASSWORD EMAIL SEND
            current_site = get_current_site(request)
            mail_subject = 'Reset Your Password'
            message = render_to_string('accounts/reset_password_email.html', {
                'user': user,
                'domain': current_site,
                'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                'token': default_token_generator.make_token(user),
            })
            to_email = email
            send_email = EmailMessage(mail_subject, message, to=[to_email])
            send_email.send()
            
            messages.success(request, 'Password Reset email has been sent to your email address.')
            return redirect('login')
        else:
            messages.error(request, 'Account does not exist!!')
            return redirect('forgotPassword')
    return render(request, 'accounts/forgotPassword.html')
  

def resetpassword_validate(request, uidb64, token):
    try:
        uid = urlsafe_base64_decode(uidb64).decode()
        user = Account._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError, Account.DoesNotExist):
        user = None
        
    if user is not None and default_token_generator.check_token(user, token):
        request.session['uid'] = uid
        messages.success(request,'Please reset your password.')
        return redirect('resetPassword')
    else:
        messages.error(request, 'This link has been expired!')
        return redirect('login')
  
       
def resetPassword(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        
        if password == confirm_password:
            uid = request.session.get('uid')
            user = Account.objects.get(pk=uid)
            user.set_password(password)
            user.save()
            messages.success(request, 'Password reset successfully')
            return redirect('login')
        else:
            messages.error(request, 'Password do not match!')
            return redirect('resetPassword')
       
    else:     
        return render(request, 'accounts/resetPassword.html')
  