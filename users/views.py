from django.shortcuts import render,redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from blog.models import Post

from django.contrib.auth.models import User

from .forms import UserRegistrationForm,UserUpdateForm,ProfileUpdateForm
def register(request):
    if request.method=="POST":
        form=UserRegistrationForm(request.POST)
        
        
            
        if form.is_valid():
            
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Acount has been created for {username}!')
            return redirect('blog-home')
    else:
        form=UserRegistrationForm()
    
    return render(request,'users/register.html',{'form':form})
@login_required
def profile(request):
    logged_in_user = request.user
    logged_in_user_posts=Post.objects.filter(author=logged_in_user).order_by('-date_posted')
    if request.method=="POST":
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
    
    
    else:
        u_form=UserUpdateForm(instance=request.user)
        p_form=ProfileUpdateForm(instance=request.user.profile)
    context={
        'u_form':u_form,
        'p_form':p_form,
        'posts':logged_in_user_posts}
    return render(request,'users/profile.html',context)





