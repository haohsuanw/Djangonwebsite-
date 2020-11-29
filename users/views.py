from django.contrib.auth import authenticate
from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib import  messages
# Create your views here.
from actions.models import Action


def profile(request,username):
    actions=Action.objects.all()

    if request.method=='POST' and request.POST.get('type')=="password":
        newpassword=request.POST.get('password')
        name=request.POST.get('name')
        user = get_object_or_404(User, username=name)
        user.set_password(newpassword)
        user.save()
    elif request.method=='POST' and request.POST.get('type')=="data":
        email = request.POST.get('email')
        lastname = request.POST.get('lastname')
        firstname = request.POST.get('firstname')
        name = request.POST.get('name')
        user = get_object_or_404(User, username=name)
        user.email=email
        user.last_name=lastname
        user.first_name=firstname
        user.save()





    user1= get_object_or_404(User,username=username )
    return render(request, "users/user/profile.html",{"user":user1,"actions":actions} )


def register(request):
    if request.method=='POST':
        username=request.POST.get('registerusername')
        email=request.POST.get('registeremail')
        password=request.POST.get('registerpassword')
        first_name=request.POST.get('registerFirstname')
        last_name=request.POST.get('registerLastname')
        try:
            user = User.objects.create_user(username, email, password)
            request.session['is_login'] = True
            request.session['username'] = user.username
            user.last_name = last_name
            user.first_name = first_name
            user.save()
            messages.add_message(request, messages.SUCCESS,
                                 "You successful registered with the username: %s" % user.username)
            return redirect('enzyme:enzyme_offic_home')


        except:
            messages.add_message(request, messages.ERROR,
                                 "This username is already exist,please use another username")
            return redirect('users:enzyme_offic_register')


    else:
        return render(request, "users/user/register.html")


#loginpage

def enzyme_office_login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            request.session['username'] = user.username
            request.session['role'] = user.detail.role
            request.session['is_login'] = True
            messages.add_message(request, messages.SUCCESS, "You Have logged in Successfuly.")
            return redirect('enzyme:enzyme_offic_home')

        else:
            messages.add_message(request, messages.ERROR, "Invaild username or password.")
            return redirect('users:enzyme_offic_loginpage')

    return render(request,"enzymeoffice/enzyme/Login.html")



#logout function
def logout(request):
    request.session['username']= None
    request.session['role']= None
    request.session['is_login'] = False
    return redirect('enzyme:enzyme_offic_home')

def changerole(request):
    if request.method == 'POST':
        name = request.POST['name']
        changedrole = request.POST['role']
        lastname = request.POST['lastname']
        firstname = request.POST['firstname']
        email = request.POST['email']

        changeuser = get_object_or_404(User, username=name)
        changeuser.detail.role=changedrole
        changeuser.first_name=firstname
        changeuser.last_name=lastname
        changeuser.email=email
        changeuser.save()

    userlist = User.objects.all()

    usercomment=[]
    for user in userlist:
        detail=user.detail.role





    if len(userlist)==0:
        commentlist= "x"

    if  request.session['is_login'] is True:
        if len(userlist)>0 and request.session['role']=='admin':
            return render(request, "users/user/role.html", {"commentlist": userlist})
        else:
            return render(request, "enzymeoffice/enzyme/nocomment.html")


