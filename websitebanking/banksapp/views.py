from django.shortcuts import render,redirect
from banksapp.forms import UserForm,LoginForm,UserAccountForm
from django.contrib.auth import authenticate,login
from .models import User1,Branchs,Login

def home(request):
    # request.session.clear()
    districts=Branchs.objects.values_list('district',flat=True).distinct()
    print(districts)
    return render(request,"home.html",{'dist':districts})


def register(request):
    if request.method == 'POST':
        form = UserAccountForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            print("user",username)
            if Login.objects.filter(username=username).exists():
                # Username already exists
                return render(request, 'register.html', {'form': form, 'error_message': 'Username already exists.'})
            else:
                # Username is unique, save the form
                user = form.save(commit=False)
                user.password = form.cleaned_data['password']  # Ideally, hash this password
                user.save()
                return redirect('/login')  # Redirect to a success page
    else:
        form = UserAccountForm()
    return render(request, 'register.html', {'form': form})

def personaldet(request):
    usern=request.session.get('username')
    print(usern)
    initial_data={
        'username': usern

    }
    form=UserForm()
    if request.method=='POST':
        form=UserForm(request.POST)
        if form.is_valid():
            print("valid")
            form.save()
            return redirect('/success')
        else:
            print(form.errors)
    else:
        form=UserForm(initial=initial_data)
    return render(request,'personaldet.html',{'form':form})

def success(request):
    return render(request,'success.html')


def login(request):
    msg=None
    form=LoginForm()
    if request.method=='POST':
        # print("1")
        form=LoginForm(request.POST)
        if form.is_valid():
            username1 = form.cleaned_data['username']
            password1 = form.cleaned_data['password']
            print(username1, password1)
            if Login.objects.filter(username=username1).exists():
                try:
                    user = Login.objects.get(username=username1, password=password1)
                    print(user)
                    if user is not None:
                        if(User1.objects.filter(username=username1).exists()):
                            return redirect('/')
                        else:
                            request.session['username']=username1
                            return redirect('/personaldet')
                    else:
                        form.add_error(None, "Invalid user")
                except:
                    msg = "Invalid password"
                    # print("Invalid password")

            else:
                # print("User not exist")
                msg = "User not exist"
    return render(request,'login.html',{'form':form,'msg':msg})









