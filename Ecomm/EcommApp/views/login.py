from django.views import View
from EcommApp.models.user import User
from django.contrib.auth.hashers import check_password
from django.shortcuts import render,redirect,HttpResponseRedirect

class Login(View):
    return_Url=None
    def get(self,request):
        Login.return_Url=request.GET.get('return_Url')
        return render(request, 'login.html')
    
    def post(self,request):
        email=request.POST.get('email')
        password=request.POST.get('password')
        user=User.get_customer_by_email(email)
        erroe_message=None
        
        if user:
            # Check password
            if check_password(password, user.password):
                # Setting session data for user info
                request.session['user_id'] = user.id
                request.session['user_fname'] = user.fname
                request.session['user_lname'] = user.lname
                request.session['user_email'] = user.email
                request.session['user_phone'] = user.phone
                request.session['user_profileImg'] = user.profileImg.url if user.profileImg else None
                
                print(request.session)
                return redirect('home')  # Redirect to homepage after login
            else:
                erroe_message = "Invalid password!"
        else:
            erroe_message = "Invalid email!"

        print(password,email)

        return render(request,'login.html',{'error':erroe_message})

def logout(request):
    request.session.clear()
    return redirect('login')